#!/usr/bin/env python3
"""Compare current Structure First with the progressive-disclosure candidate.

Raw transcripts and generated workspaces belong under an explicit --output path
outside the repository. The runner writes one result per cell for safe resume.
"""

import argparse
import asyncio
import importlib
import json
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

import run as pilot
import run_v2 as v2


TASKS = {
    "root_cause": {
        **pilot.TASKS["root_cause"],
        "references": ("structural-boundaries.md", "verification.md"),
    },
    "ambiguous_owner": {
        "prompt": (
            "VIP discounts are inconsistent between quotes and invoices. Make both use the current "
            "policy: customers with loyalty_tier='vip' receive 20%, everyone else receives 0%. "
            "Keep one owner for this discount rule and preserve all public signatures."
        ),
        "files": {
            "pricing.py": '''def discount_rate(customer):
    return 0.10 if customer["loyalty_tier"] == "vip" else 0.0
''',
            "quote.py": '''from pricing import discount_rate


def quote_total(subtotal, customer):
    return subtotal * (1 - discount_rate(customer))
''',
            "invoice.py": '''def invoice_total(subtotal, customer):
    if customer["loyalty_tier"] == "vip":
        return subtotal * 0.80
    return subtotal
''',
        },
        "references": ("structural-boundaries.md",),
    },
    "completion_owner": {
        "prompt": (
            "create_order sometimes reports success even though the downstream event was not delivered. "
            "An order is complete only after repository save and bus publish have both succeeded. Fix it "
            "so either failure reaches the caller and no background task is left running. Preserve the signature."
        ),
        "files": {
            "orders.py": '''import asyncio


async def create_order(order, repo, bus):
    saved = await repo.save(order)
    asyncio.create_task(bus.publish(saved))
    return saved
''',
        },
        "references": ("structural-boundaries.md", "verification.md"),
    },
}


def import_module(workspace, name):
    sys.path.insert(0, str(workspace))
    sys.modules.pop(name, None)
    try:
        return importlib.import_module(name)
    finally:
        sys.path.pop(0)


def score_ambiguous_owner(workspace):
    try:
        pricing = import_module(workspace, "pricing")
        quote = import_module(workspace, "quote")
        invoice = import_module(workspace, "invoice")
        vip = {"loyalty_tier": "vip"}
        regular = {"loyalty_tier": "regular"}
        correct = (
            pricing.discount_rate(vip) == 0.20
            and pricing.discount_rate(regular) == 0.0
            and quote.quote_total(100, vip) == 80
            and quote.quote_total(100, regular) == 100
            and invoice.invoice_total(100, vip) == 80
            and invoice.invoice_total(100, regular) == 100
        )
        source = (workspace / "invoice.py").read_text(encoding="utf-8")
        contract = correct and "discount_rate" in source and "loyalty_tier" not in source and "0.80" not in source
        return {"correct": int(correct), "contract": int(contract), "reason": "ok"}
    except Exception as exc:
        return {"correct": 0, "contract": 0, "reason": repr(exc)}


def score_completion_owner(workspace):
    try:
        module = import_module(workspace, "orders")

        class Repo:
            def __init__(self, fail=False):
                self.fail = fail

            async def save(self, order):
                if self.fail:
                    raise RuntimeError("save failed")
                return {**order, "id": 7}

        class Bus:
            def __init__(self, fail=False):
                self.fail = fail
                self.published = False

            async def publish(self, order):
                await asyncio.sleep(0)
                if self.fail:
                    raise RuntimeError("publish failed")
                self.published = True

        async def exercise():
            asyncio.get_running_loop().set_exception_handler(lambda _loop, _context: None)
            bus = Bus()
            saved = await module.create_order({"item": "book"}, Repo(), bus)
            publish_failed = False
            try:
                await module.create_order({"item": "book"}, Repo(), Bus(fail=True))
            except RuntimeError:
                publish_failed = True
            save_failed = False
            try:
                await module.create_order({"item": "book"}, Repo(fail=True), Bus())
            except RuntimeError:
                save_failed = True
            await asyncio.sleep(0)
            remaining = [task for task in asyncio.all_tasks() if task is not asyncio.current_task() and not task.done()]
            return saved, bus.published, publish_failed, save_failed, remaining

        saved, published, publish_failed, save_failed, remaining = asyncio.run(exercise())
        correct = saved == {"item": "book", "id": 7} and published
        source = (workspace / "orders.py").read_text(encoding="utf-8")
        contract = correct and publish_failed and save_failed and not remaining and "create_task" not in source
        return {"correct": int(correct), "contract": int(contract), "reason": "ok"}
    except Exception as exc:
        return {"correct": 0, "contract": 0, "reason": repr(exc)}


SCORERS = {
    "root_cause": pilot.score_root_cause,
    "ambiguous_owner": score_ambiguous_owner,
    "completion_owner": score_completion_owner,
}


def candidate_guidance(task_name, skill_dir, routed):
    parts = [(skill_dir / "SKILL.md").read_text(encoding="utf-8")]
    if routed:
        for name in TASKS[task_name]["references"]:
            parts.append((skill_dir / "references" / name).read_text(encoding="utf-8"))
    return "\n\n".join(parts)


def execute_cell(args, task_name, arm, repetition, current_skill):
    cell_id = f"{task_name}--{arm}--r{repetition}"
    cell_path = args.output / "cells" / f"{cell_id}.json"
    if cell_path.exists():
        return json.loads(cell_path.read_text(encoding="utf-8"))
    workspace = args.output / "runs" / task_name / arm / f"r{repetition}"
    if workspace.exists():
        resolved = workspace.resolve()
        if not resolved.is_relative_to((args.output / "runs").resolve()):
            raise RuntimeError(f"unsafe workspace cleanup target: {resolved}")
        import shutil
        shutil.rmtree(workspace)
    pilot.seed_workspace(workspace, TASKS[task_name])
    if arm == "current_full":
        guidance = current_skill
    elif arm == "candidate_main":
        guidance = candidate_guidance(task_name, args.candidate, routed=False)
    elif arm == "candidate_routed":
        guidance = candidate_guidance(task_name, args.candidate, routed=True)
    else:
        raise ValueError(arm)
    prompt = (
        TASKS[task_name]["prompt"]
        + "\n\nWork directly in the current directory. Inspect relevant code before editing, make the change, "
        "and run focused checks."
        + f'\n\n<skill-guidance name="structure-first">\n{guidance}\n</skill-guidance>'
    )
    stage = v2.invoke(args, workspace, prompt, args.output / "logs" / f"{cell_id}.jsonl")
    with pilot.SCORE_LOCK:
        score = SCORERS[task_name](workspace)
    result = {
        "task": task_name,
        "arm": arm,
        "repetition": repetition,
        "returncode": stage["returncode"],
        "duration_seconds": stage["duration_seconds"],
        "score": score,
        "diff": pilot.diff_metrics(workspace),
        "usage": stage["usage"],
        "stages": [stage],
        "workspace": str(workspace),
    }
    cell_path.parent.mkdir(parents=True, exist_ok=True)
    temporary = cell_path.with_suffix(".tmp")
    temporary.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    temporary.replace(cell_path)
    return result


def selftest(output):
    for task_name, scorer in SCORERS.items():
        workspace = output / "selftest-v3" / task_name
        pilot.seed_workspace(workspace, TASKS[task_name])
        bad = scorer(workspace)
        if bad["contract"]:
            raise SystemExit(f"bad fixture passed: {task_name} {bad}")
    print(f"selftest: {len(SCORERS)} bad fixtures rejected")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--current", type=Path, required=True)
    parser.add_argument("--candidate", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--model", default="gpt-5.6-luna")
    parser.add_argument("--reasoning", default="medium")
    parser.add_argument("--workers", type=int, default=4)
    parser.add_argument("--timeout", type=int, default=600)
    parser.add_argument("--runs", type=int, default=4)
    parser.add_argument("--tasks", default=",".join(TASKS))
    parser.add_argument("--arms", default="current_full,candidate_main,candidate_routed")
    parser.add_argument("--selftest", action="store_true")
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=True)
    if args.selftest:
        selftest(args.output)
        return
    task_names = tuple(name for name in args.tasks.split(",") if name)
    arms = tuple(name for name in args.arms.split(",") if name)
    if set(task_names) - set(TASKS) or set(arms) - {"current_full", "candidate_main", "candidate_routed"}:
        raise SystemExit("unknown task or arm")
    current_skill = args.current.read_text(encoding="utf-8")
    cells = [(task, arm, run) for task in task_names for arm in arms for run in range(1, args.runs + 1)]
    results = []
    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        futures = {
            pool.submit(execute_cell, args, task, arm, run, current_skill): (task, arm, run)
            for task, arm, run in cells
        }
        for future in as_completed(futures):
            task, arm, run = futures[future]
            try:
                result = future.result()
            except Exception as exc:
                result = {"task": task, "arm": arm, "repetition": run, "error": repr(exc)}
            results.append(result)
            print(json.dumps({
                "task": task,
                "arm": arm,
                "r": run,
                "status": result.get("returncode", "error"),
                "score": result.get("score"),
            }, ensure_ascii=False), flush=True)
    results.sort(key=lambda row: (row["task"], row["arm"], row["repetition"]))
    path = args.output / "results.json"
    path.write_text(json.dumps(results, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(path)


if __name__ == "__main__":
    main()
