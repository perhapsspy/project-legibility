#!/usr/bin/env python3
"""Run an isolated Codex pilot for Structure First and Ponytail guidance.

The reuse and root-cause task shapes are adapted from Ponytail's MIT-licensed
agentic benchmark at commit 2ed6c52c9d7e5e56942508591085fd45dea277d3.
Keep --output outside the repository because it contains disposable workspaces
and raw JSONL transcripts.
"""

import argparse
import asyncio
import importlib
import json
import os
import shutil
import subprocess
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from threading import Lock


TASKS = {
    "reuse": {
        "prompt": (
            "Implement unique_slug(title, taken) in articles.py. Return a project-compatible "
            "URL slug and append -2, -3, and so on until it is unique. Preserve the existing "
            "public signature. Slugs must match how the rest of this project builds them."
        ),
        "files": {
            "textutils.py": '''import re
import unicodedata


def slugify(title):
    """Project-wide slug format: transliterate accents, lowercase, and hyphenate."""
    ascii_title = unicodedata.normalize("NFKD", title).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "-", ascii_title.lower()).strip("-")
''',
            "articles.py": '''def unique_slug(title, taken):
    """Return an unused project-compatible slug for title."""
    raise NotImplementedError
''',
        },
    },
    "root_cause": {
        "prompt": (
            "Fix the reported transfer bug: an account can be left with a negative balance after "
            "some transfers, which must never happen. Preserve the existing public functions and "
            "valid transfer and withdrawal behavior."
        ),
        "files": {
            "ledger.py": '''balances = {}


def debit(account, cents):
    """Take cents from account."""
    balances[account] = balances.get(account, 0) - cents


def deposit(account, cents):
    balances[account] = balances.get(account, 0) + cents
''',
            "transfers.py": '''from ledger import debit, deposit


def transfer(source, destination, cents):
    debit(source, cents)
    deposit(destination, cents)
''',
            "cash.py": '''from ledger import debit


def withdraw(account, cents):
    debit(account, cents)
    return cents
''',
        },
    },
    "async_lifecycle": {
        "prompt": (
            "Fix SearchController in search.py. A slow earlier request must never overwrite a "
            "newer query, loading must describe the current request through success or failure, "
            "and repeating the equivalent current query while it is in flight must not start a "
            "second fetch. Preserve the class's public API."
        ),
        "files": {
            "search.py": '''class SearchController:
    def __init__(self, fetch_results):
        self.fetch_results = fetch_results
        self.query = None
        self.results = []
        self.loading = False

    async def search(self, query):
        self.query = query
        self.loading = True
        self.results = await self.fetch_results(query)
        self.loading = False
''',
        },
    },
}


def run(cmd, cwd, timeout=60):
    return subprocess.run(
        cmd,
        cwd=cwd,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        timeout=timeout,
        check=False,
    )


def seed_workspace(path, task):
    path.mkdir(parents=True)
    for name, content in task["files"].items():
        (path / name).write_text(content, encoding="utf-8")
    run(["git", "init", "-q"], path)
    run(["git", "config", "user.email", "pilot@example.invalid"], path)
    run(["git", "config", "user.name", "Skill Pilot"], path)
    run(["git", "add", "."], path)
    committed = run(["git", "commit", "-qm", "seed"], path)
    if committed.returncode:
        raise RuntimeError(committed.stdout)


def load_module(workspace, module_name):
    sys.path.insert(0, str(workspace))
    for name in ("articles", "textutils", "ledger", "transfers", "cash", "search"):
        sys.modules.pop(name, None)
    try:
        return importlib.import_module(module_name)
    finally:
        sys.path.pop(0)


def score_reuse(workspace):
    try:
        module = load_module(workspace, "articles")
        basic = module.unique_slug("Hello, World!", set()) == "hello-world"
        unique = module.unique_slug("Hello, World!", {"hello-world", "hello-world-2"}) == "hello-world-3"
        owner = module.unique_slug("Café Olé", set()) == "cafe-ole"
        return {"correct": int(basic and unique), "contract": int(owner), "reason": "ok"}
    except Exception as exc:
        return {"correct": 0, "contract": 0, "reason": repr(exc)}


def score_root_cause(workspace):
    try:
        sys.path.insert(0, str(workspace))
        for name in ("ledger", "transfers", "cash"):
            sys.modules.pop(name, None)
        ledger = importlib.import_module("ledger")
        transfers = importlib.import_module("transfers")
        cash = importlib.import_module("cash")
        ledger.balances.clear()
        ledger.balances.update({"a": 100, "b": 0})
        transfers.transfer("a", "b", 60)
        cash.withdraw("b", 10)
        valid = ledger.balances == {"a": 40, "b": 50}

        ledger.balances.clear()
        ledger.balances.update({"a": 100, "b": 0})
        try:
            transfers.transfer("a", "b", 150)
        except Exception:
            pass
        transfer_safe = ledger.balances == {"a": 100, "b": 0}

        ledger.balances.clear()
        ledger.balances.update({"a": 100})
        try:
            ledger.debit("a", 150)
        except Exception:
            pass
        owner_safe = ledger.balances == {"a": 100}
        result = {
            "correct": int(valid and transfer_safe),
            "contract": int(owner_safe),
            "reason": "ok",
        }
        sys.path.pop(0)
        return result
    except Exception as exc:
        if sys.path and sys.path[0] == str(workspace):
            sys.path.pop(0)
        return {"correct": 0, "contract": 0, "reason": repr(exc)}


async def async_contract(module):
    loop = asyncio.get_running_loop()
    calls = []
    pending = {}

    async def fetch(query):
        calls.append(query)
        pending.setdefault(query, loop.create_future())
        return await pending[query]

    async def wait_pending(query):
        for _ in range(20):
            if query in pending:
                return
            await asyncio.sleep(0)
        raise AssertionError(f"request did not start: {query}")

    controller = module.SearchController(fetch)
    first = asyncio.create_task(controller.search("a"))
    await wait_pending("a")
    second = asyncio.create_task(controller.search("ab"))
    await wait_pending("ab")
    pending["a"].set_result(["old"])
    await first
    stale_ignored = controller.results != ["old"] and controller.loading is True
    pending["ab"].set_result(["new"])
    await second
    latest_wins = controller.results == ["new"] and controller.loading is False

    calls.clear()
    pending.clear()
    same_one = asyncio.create_task(controller.search("same"))
    await wait_pending("same")
    same_two = asyncio.create_task(controller.search("same"))
    await asyncio.sleep(0)
    deduped = calls == ["same"]
    pending["same"].set_result(["same-result"])
    await asyncio.gather(same_one, same_two)

    calls.clear()
    pending.clear()
    failing = asyncio.create_task(controller.search("fail"))
    await wait_pending("fail")
    pending["fail"].set_exception(RuntimeError("boom"))
    try:
        await failing
    except RuntimeError:
        pass
    failure_balanced = controller.loading is False
    return latest_wins, stale_ignored and deduped and failure_balanced


def score_async(workspace):
    try:
        module = load_module(workspace, "search")
        correct, contract = asyncio.run(async_contract(module))
        return {"correct": int(correct), "contract": int(contract), "reason": "ok"}
    except Exception as exc:
        return {"correct": 0, "contract": 0, "reason": repr(exc)}


SCORERS = {
    "reuse": score_reuse,
    "root_cause": score_root_cause,
    "async_lifecycle": score_async,
}
SCORE_LOCK = Lock()


REFERENCE_FILES = {
    "reuse": {
        "good": {
            "articles.py": '''from textutils import slugify


def unique_slug(title, taken):
    base = slugify(title)
    if base not in taken:
        return base
    suffix = 2
    while f"{base}-{suffix}" in taken:
        suffix += 1
    return f"{base}-{suffix}"
''',
        },
        "bad": {
            "articles.py": '''import re


def unique_slug(title, taken):
    base = re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")
    if base not in taken:
        return base
    suffix = 2
    while f"{base}-{suffix}" in taken:
        suffix += 1
    return f"{base}-{suffix}"
''',
        },
    },
    "root_cause": {
        "good": {
            "ledger.py": '''balances = {}


def debit(account, cents):
    if balances.get(account, 0) < cents:
        raise ValueError("insufficient funds")
    balances[account] = balances.get(account, 0) - cents


def deposit(account, cents):
    balances[account] = balances.get(account, 0) + cents
''',
        },
        "bad": {
            "transfers.py": '''from ledger import debit, deposit, balances


def transfer(source, destination, cents):
    if balances.get(source, 0) < cents:
        raise ValueError("insufficient funds")
    debit(source, cents)
    deposit(destination, cents)
''',
        },
    },
    "async_lifecycle": {
        "good": {
            "search.py": '''import asyncio


class SearchController:
    def __init__(self, fetch_results):
        self.fetch_results = fetch_results
        self.query = None
        self.results = []
        self.loading = False
        self._generation = 0
        self._inflight = {}

    async def search(self, query):
        if query == self.query and query in self._inflight:
            return await self._inflight[query]
        self.query = query
        self._generation += 1
        generation = self._generation
        self.loading = True
        task = asyncio.create_task(self.fetch_results(query))
        self._inflight[query] = task
        try:
            results = await task
            if generation == self._generation:
                self.results = results
            return results
        finally:
            if self._inflight.get(query) is task:
                del self._inflight[query]
            if generation == self._generation:
                self.loading = False
''',
        },
        "bad": {
            "search.py": '''class SearchController:
    def __init__(self, fetch_results):
        self.fetch_results = fetch_results
        self.query = None
        self.results = []
        self.loading = False
        self._generation = 0

    async def search(self, query):
        self.query = query
        self._generation += 1
        generation = self._generation
        self.loading = True
        results = await self.fetch_results(query)
        if generation == self._generation:
            self.results = results
            self.loading = False
        return results
''',
        },
    },
}


def selftest(output):
    root = output / "selftest"
    if root.exists():
        shutil.rmtree(root)
    failures = []
    for task_name, variants in REFERENCE_FILES.items():
        for variant, replacements in variants.items():
            workspace = root / task_name / variant
            workspace.mkdir(parents=True)
            files = dict(TASKS[task_name]["files"])
            files.update(replacements)
            for name, content in files.items():
                (workspace / name).write_text(content, encoding="utf-8")
            scored = SCORERS[task_name](workspace)
            expected = {"correct": 1, "contract": int(variant == "good")}
            observed = {key: scored[key] for key in expected}
            print(json.dumps({"task": task_name, "variant": variant, "score": scored}))
            if observed != expected:
                failures.append({"task": task_name, "variant": variant, "expected": expected, "observed": observed})
    if failures:
        raise SystemExit(json.dumps(failures, indent=2))


def diff_metrics(workspace):
    numstat = run(["git", "diff", "--numstat", "HEAD"], workspace).stdout.splitlines()
    added = deleted = files = tests = 0
    for row in numstat:
        parts = row.split("\t")
        if len(parts) != 3:
            continue
        a, d, name = parts
        files += 1
        if "test" in Path(name).name.lower():
            tests += 1
        else:
            added += int(a) if a.isdigit() else 0
            deleted += int(d) if d.isdigit() else 0
    untracked = run(["git", "ls-files", "--others", "--exclude-standard"], workspace).stdout.splitlines()
    for name in untracked:
        if name.startswith("__pycache__/") or "/__pycache__/" in name or name.endswith(".pyc"):
            continue
        files += 1
        content = (workspace / name).read_text(encoding="utf-8", errors="ignore")
        if "test" in Path(name).name.lower():
            tests += 1
        else:
            added += len(content.splitlines())
    return {"added": added, "deleted": deleted, "files": files, "test_files": tests}


def parse_usage(jsonl):
    usage = {}
    for line in jsonl.splitlines():
        try:
            event = json.loads(line)
        except json.JSONDecodeError:
            continue
        candidate = event.get("usage")
        if isinstance(candidate, dict):
            usage = candidate
    return usage


def make_guidance(arm, ponytail, structure):
    if arm == "baseline":
        return ""
    if arm == "ponytail":
        return f"\n\n<skill-guidance name=\"ponytail\">\n{ponytail}\n</skill-guidance>"
    if arm == "structure_first":
        return f"\n\n<skill-guidance name=\"structure-first\">\n{structure}\n</skill-guidance>"
    return (
        "\n\nApply Structure First to identify the responsible owner and observable contract, "
        "then apply Ponytail to minimize the implementation without weakening that contract."
        f"\n\n<skill-guidance name=\"structure-first\">\n{structure}\n</skill-guidance>"
        f"\n\n<skill-guidance name=\"ponytail\">\n{ponytail}\n</skill-guidance>"
    )


def execute_cell(args, task_name, arm, ponytail, structure):
    workspace = args.output / "runs" / task_name / arm
    seed_workspace(workspace, TASKS[task_name])
    prompt = (
        TASKS[task_name]["prompt"]
        + "\n\nWork directly in the current directory. Inspect the relevant code before editing, "
        "make the change, and run any focused checks you consider useful."
        + make_guidance(arm, ponytail, structure)
    )
    command = [
        "codex", "exec",
        "--ephemeral",
        "--ignore-user-config",
        "--ignore-rules",
        "--skip-git-repo-check",
        "--approve-for-me",
        "--model", args.model,
        "-c", f'model_reasoning_effort="{args.reasoning}"',
        "--json",
        "-C", str(workspace),
        prompt,
    ]
    env = dict(os.environ)
    for key in list(env):
        if key.startswith("PONYTAIL_"):
            env.pop(key)
    started = time.monotonic()
    try:
        completed = subprocess.run(
            command,
            cwd=workspace,
            env=env,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            timeout=args.timeout,
            check=False,
        )
        raw = completed.stdout
        returncode = completed.returncode
    except subprocess.TimeoutExpired as exc:
        raw = (exc.stdout or "") + "\nTIMEOUT\n"
        returncode = 124
    duration = round(time.monotonic() - started, 2)
    log_path = args.output / "logs" / f"{task_name}--{arm}.jsonl"
    log_path.parent.mkdir(parents=True, exist_ok=True)
    log_path.write_text(raw, encoding="utf-8")
    # Scorers import generated modules through process-global sys.path and
    # sys.modules. Serialize the short scoring phase while agent cells remain
    # parallel so one workspace cannot contaminate another's import.
    with SCORE_LOCK:
        score = SCORERS[task_name](workspace)
    return {
        "task": task_name,
        "arm": arm,
        "returncode": returncode,
        "duration_seconds": duration,
        "score": score,
        "diff": diff_metrics(workspace),
        "usage": parse_usage(raw),
        "workspace": str(workspace),
        "log": str(log_path),
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--ponytail", type=Path, required=True)
    parser.add_argument("--structure", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--model", default="gpt-5.6-luna")
    parser.add_argument("--reasoning", default="medium")
    parser.add_argument("--workers", type=int, default=4)
    parser.add_argument("--timeout", type=int, default=600)
    parser.add_argument("--selftest", action="store_true")
    parser.add_argument("--tasks", default=",".join(TASKS))
    parser.add_argument("--arms", default="baseline,ponytail,structure_first,combined")
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=True)
    if args.selftest:
        selftest(args.output)
        return
    ponytail = args.ponytail.read_text(encoding="utf-8")
    structure = args.structure.read_text(encoding="utf-8")
    task_names = tuple(name for name in args.tasks.split(",") if name)
    arms = tuple(name for name in args.arms.split(",") if name)
    unknown_tasks = set(task_names) - set(TASKS)
    unknown_arms = set(arms) - {"baseline", "ponytail", "structure_first", "combined"}
    if unknown_tasks or unknown_arms:
        raise SystemExit(f"unknown tasks={sorted(unknown_tasks)} arms={sorted(unknown_arms)}")
    cells = [(task, arm) for task in task_names for arm in arms]
    results = []
    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        futures = {
            pool.submit(execute_cell, args, task, arm, ponytail, structure): (task, arm)
            for task, arm in cells
        }
        for future in as_completed(futures):
            task, arm = futures[future]
            try:
                result = future.result()
            except Exception as exc:
                result = {"task": task, "arm": arm, "error": repr(exc)}
            results.append(result)
            compact = {
                "task": task,
                "arm": arm,
                "status": result.get("returncode", "error"),
                "score": result.get("score"),
                "diff": result.get("diff"),
            }
            print(json.dumps(compact, ensure_ascii=False), flush=True)
    results.sort(key=lambda item: (item["task"], item["arm"]))
    summary = args.output / "results.json"
    summary.write_text(json.dumps(results, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(summary)


if __name__ == "__main__":
    main()
