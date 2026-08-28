#!/usr/bin/env python3
"""Run the repeated Structure First versus Ponytail comparison.

Raw JSONL and generated workspaces belong under an explicit --output path
outside the repository. The runner writes one result file per cell so an
interrupted batch can resume without paying for completed cells again.
"""

import argparse
import csv
import importlib
import json
import os
import shutil
import subprocess
import sys
import tempfile
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from html.parser import HTMLParser
from pathlib import Path

import run as pilot


RUNTIME_CORE = """# Structure First runtime core

Find the owner. Trace the flow. Change the smallest responsible unit. Verify the contract.

1. Choose the current owner of the behavior or rule, not the reported symptom.
2. State the minimum observable completion condition.
3. Trace caller → decision/state → write/effect → completion, including only boundaries needed by the requested behavior.
4. Name the structural demand: flow, lifecycle, ownership, composition, migration, or boundary contract.
5. Prefer a local clarification. Change structure only when total complexity falls or an independent responsibility becomes materially easier to verify.
6. Keep one non-competing resolution path for each settled decision, writer, effect, and completion rule. Remove the old path when ownership moves; otherwise name a migration owner and exit condition.
7. Verify observable behavior at the most stable responsible unit, not helper internals.

For async state, make freshness, equivalent-input no-op, and balanced success/failure completion one owned contract. When one domain meaning crosses representations, keep interpretation at one owner; other units transport or project it without re-inferring it. Do not add future-use options, dependencies, wrappers, or abstractions.
"""


NEW_TASKS = {
    "native": {
        "prompt": (
            "Replace the existing booking date text field in form.html with an accessible calendar "
            "date picker. It must accept dates from 2026-09-01 through 2026-12-31 and preserve the "
            "booking_date form field name. Do not change the server contract."
        ),
        "files": {
            "form.html": '''<!doctype html>
<html lang="en">
  <body>
    <form action="/book" method="post">
      <label for="booking-date">Booking date</label>
      <input id="booking-date" name="booking_date" type="text">
      <button type="submit">Book</button>
    </form>
  </body>
</html>
''',
        },
    },
    "stdlib": {
        "prompt": (
            "Implement export_rows(rows, path) in csv_export.py. rows is a non-empty list of "
            "dictionaries with the same key order. Write a UTF-8 CSV with one header row that "
            "round-trips commas, quotes, newlines, and Unicode. Preserve the public signature."
        ),
        "files": {
            "csv_export.py": '''def export_rows(rows, path):
    """Write rows to path as UTF-8 CSV."""
    raise NotImplementedError
''',
            "requirements.txt": "fastapi==0.115.0\n",
        },
    },
    "migration": {
        "prompt": (
            "The new codec has been verified production-equivalent. Complete the migration so "
            "render_record uses only the new codec, remove the legacy execution path and dependency, "
            "and preserve the public output."
        ),
        "files": {
            "codec.py": '''import json


def encode(record):
    return json.dumps(record, sort_keys=True, separators=(",", ":"))
''',
            "legacy_codec.py": '''import json


def encode(record):
    return json.dumps(record, sort_keys=True, separators=(",", ":"))
''',
            "service.py": '''import os

from codec import encode as encode_new
from legacy_codec import encode as encode_legacy


def render_record(record):
    if os.getenv("USE_NEW_CODEC") == "1":
        return encode_new(record)
    return encode_legacy(record)
''',
            "requirements.txt": "fastapi==0.115.0\nlegacy-codec==1.0.0\n",
        },
    },
    "representation": {
        "prompt": (
            "Customers report that archived private records can appear in CSV exports. Fix the bug "
            "so list, detail, and export use the same current visibility policy: a record is visible "
            "iff it is not archived and is public or owned by the current user. Preserve return shapes."
        ),
        "files": {
            "policy.py": '''def can_view(record, user):
    return not record["archived"] and (
        record["public"] or record["owner_id"] == user["id"]
    )
''',
            "api.py": '''import policy


def list_records(records, user):
    return [record for record in records if policy.can_view(record, user)]


def detail_record(record, user):
    return record if policy.can_view(record, user) else None
''',
            "exporter.py": '''def export_rows(records, user):
    return [
        {"id": record["id"], "title": record["title"]}
        for record in records
        if record["public"] or record["owner_id"] == user["id"]
    ]
''',
        },
    },
}


TASKS = {
    "root_cause": pilot.TASKS["root_cause"],
    "async_lifecycle": pilot.TASKS["async_lifecycle"],
    **NEW_TASKS,
}


class FormParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.inputs = []
        self.scripts = []

    def handle_starttag(self, tag, attrs):
        values = dict(attrs)
        if tag == "input":
            self.inputs.append(values)
        elif tag == "script":
            self.scripts.append(values)


def score_native(workspace):
    try:
        source = (workspace / "form.html").read_text(encoding="utf-8")
        parser = FormParser()
        parser.feed(source)
        field = next(item for item in parser.inputs if item.get("name") == "booking_date")
        implemented = field.get("type") == "date" or field.get("aria-haspopup") == "dialog"
        js_files = [path for path in workspace.rglob("*.js") if ".git" not in path.parts]
        native = (
            field.get("type") == "date"
            and field.get("min") == "2026-09-01"
            and field.get("max") == "2026-12-31"
            and not parser.scripts
            and not js_files
        )
        return {"correct": int(implemented), "contract": int(native), "reason": "ok"}
    except Exception as exc:
        return {"correct": 0, "contract": 0, "reason": repr(exc)}


def import_from(workspace, module_name, clear):
    sys.path.insert(0, str(workspace))
    for name in clear:
        sys.modules.pop(name, None)
    try:
        return importlib.import_module(module_name)
    finally:
        sys.path.pop(0)


def score_stdlib(workspace):
    try:
        module = import_from(workspace, "csv_export", ("csv_export",))
        with tempfile.TemporaryDirectory() as directory:
            simple_path = Path(directory) / "simple.csv"
            module.export_rows([{"name": "Alice", "note": "ok"}], simple_path)
            with simple_path.open(newline="", encoding="utf-8") as handle:
                simple = list(csv.reader(handle))
            correct = simple == [["name", "note"], ["Alice", "ok"]]

            complex_path = Path(directory) / "complex.csv"
            expected = [
                {"name": "김,민수", "note": 'line 1\n"quoted"'},
                {"name": "Zoë", "note": "plain"},
            ]
            module.export_rows(expected, complex_path)
            with complex_path.open(newline="", encoding="utf-8") as handle:
                actual = list(csv.DictReader(handle))
        requirements = (workspace / "requirements.txt").read_text(encoding="utf-8")
        contract = actual == expected and requirements == "fastapi==0.115.0\n"
        return {"correct": int(correct), "contract": int(contract), "reason": "ok"}
    except Exception as exc:
        return {"correct": 0, "contract": 0, "reason": repr(exc)}


def score_migration(workspace):
    try:
        module = import_from(workspace, "service", ("service", "codec", "legacy_codec"))
        expected = '{"a":1,"b":2}'
        correct = module.render_record({"b": 2, "a": 1}) == expected
        service = (workspace / "service.py").read_text(encoding="utf-8").lower()
        requirements = (workspace / "requirements.txt").read_text(encoding="utf-8").lower()
        contract = (
            not (workspace / "legacy_codec.py").exists()
            and "legacy" not in service
            and "use_new_codec" not in service
            and "legacy" not in requirements
        )
        return {"correct": int(correct), "contract": int(contract), "reason": "ok"}
    except Exception as exc:
        return {"correct": 0, "contract": 0, "reason": repr(exc)}


def score_representation(workspace):
    try:
        sys.path.insert(0, str(workspace))
        for name in ("policy", "api", "exporter"):
            sys.modules.pop(name, None)
        policy = importlib.import_module("policy")
        api = importlib.import_module("api")
        exporter = importlib.import_module("exporter")
        user = {"id": 7}
        records = [
            {"id": 1, "title": "public", "public": True, "archived": False, "owner_id": 9},
            {"id": 2, "title": "owned", "public": False, "archived": False, "owner_id": 7},
            {"id": 3, "title": "archived", "public": False, "archived": True, "owner_id": 7},
            {"id": 4, "title": "private", "public": False, "archived": False, "owner_id": 9},
        ]
        visible = [records[0], records[1]]
        correct = (
            api.list_records(records, user) == visible
            and api.detail_record(records[0], user) == records[0]
            and api.detail_record(records[3], user) is None
            and exporter.export_rows(records, user)
            == [{"id": 1, "title": "public"}, {"id": 2, "title": "owned"}]
        )
        source = (workspace / "exporter.py").read_text(encoding="utf-8")
        contract = correct and "can_view" in source and "owner_id" not in source and 'record["public"]' not in source
        sys.path.pop(0)
        return {"correct": int(correct), "contract": int(contract), "reason": "ok"}
    except Exception as exc:
        if sys.path and sys.path[0] == str(workspace):
            sys.path.pop(0)
        return {"correct": 0, "contract": 0, "reason": repr(exc)}


SCORERS = {
    "root_cause": pilot.score_root_cause,
    "async_lifecycle": pilot.score_async,
    "native": score_native,
    "stdlib": score_stdlib,
    "migration": score_migration,
    "representation": score_representation,
}


REFERENCES = {
    "root_cause": pilot.REFERENCE_FILES["root_cause"],
    "async_lifecycle": pilot.REFERENCE_FILES["async_lifecycle"],
    "native": {
        "good": {"form.html": '''<form><label for="booking-date">Booking date</label><input id="booking-date" name="booking_date" type="date" min="2026-09-01" max="2026-12-31"><button>Book</button></form>\n'''},
        "bad": {"form.html": '''<form><label for="booking-date">Booking date</label><input id="booking-date" name="booking_date" type="text" aria-haspopup="dialog"><button>Book</button></form>\n''', "calendar.js": "// custom calendar placeholder\n"},
    },
    "stdlib": {
        "good": {"csv_export.py": '''import csv


def export_rows(rows, path):
    with open(path, "w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=rows[0])
        writer.writeheader()
        writer.writerows(rows)
'''},
        "bad": {"csv_export.py": '''def export_rows(rows, path):
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(",".join(rows[0]) + "\\n")
        for row in rows:
            handle.write(",".join(str(row[key]) for key in rows[0]) + "\\n")
'''},
    },
    "migration": {
        "good": {"service.py": '''from codec import encode


def render_record(record):
    return encode(record)
''', "requirements.txt": "fastapi==0.115.0\n", "legacy_codec.py": None},
        "bad": {"service.py": '''import os

from codec import encode as encode_new
from legacy_codec import encode as encode_legacy


def render_record(record):
    if os.getenv("USE_LEGACY_CODEC") == "1":
        return encode_legacy(record)
    return encode_new(record)
'''},
    },
    "representation": {
        "good": {"exporter.py": '''import policy


def export_rows(records, user):
    return [
        {"id": record["id"], "title": record["title"]}
        for record in records
        if policy.can_view(record, user)
    ]
'''},
        "bad": {"exporter.py": '''def export_rows(records, user):
    return [
        {"id": record["id"], "title": record["title"]}
        for record in records
        if not record["archived"] and (record["public"] or record["owner_id"] == user["id"])
    ]
'''},
    },
}


def selftest(output):
    root = output / "selftest-v2"
    if root.exists():
        shutil.rmtree(root)
    failures = []
    for task_name, variants in REFERENCES.items():
        for variant, replacements in variants.items():
            workspace = root / task_name / variant
            workspace.mkdir(parents=True)
            files = dict(TASKS[task_name]["files"])
            for name, content in replacements.items():
                if content is None:
                    files.pop(name, None)
                else:
                    files[name] = content
            for name, content in files.items():
                (workspace / name).write_text(content, encoding="utf-8")
            with pilot.SCORE_LOCK:
                scored = SCORERS[task_name](workspace)
            expected = {"correct": 1, "contract": int(variant == "good")}
            observed = {key: scored[key] for key in expected}
            print(json.dumps({"task": task_name, "variant": variant, "score": scored}))
            if observed != expected:
                failures.append({"task": task_name, "variant": variant, "expected": expected, "observed": observed})
    if failures:
        raise SystemExit(json.dumps(failures, indent=2))


def guidance(arm, ponytail, structure):
    if arm == "baseline":
        return ""
    if arm == "ponytail":
        return f'\n\n<skill-guidance name="ponytail">\n{ponytail}\n</skill-guidance>'
    if arm == "structure_full":
        return f'\n\n<skill-guidance name="structure-first">\n{structure}\n</skill-guidance>'
    if arm == "structure_core":
        return f'\n\n<skill-guidance name="structure-first-runtime-core">\n{RUNTIME_CORE}\n</skill-guidance>'
    if arm == "combined":
        return (
            "\n\nApply Structure First to identify the responsible owner and observable contract, "
            "then apply Ponytail to minimize implementation without weakening that contract."
            f'\n\n<skill-guidance name="structure-first">\n{structure}\n</skill-guidance>'
            f'\n\n<skill-guidance name="ponytail">\n{ponytail}\n</skill-guidance>'
        )
    raise ValueError(arm)


def invoke(args, workspace, prompt, log_path):
    command = [
        "codex", "exec", "--ephemeral", "--ignore-user-config", "--ignore-rules",
        "--skip-git-repo-check", "--approve-for-me", "--model", args.model,
        "-c", f'model_reasoning_effort="{args.reasoning}"', "--json", "-C", str(workspace), prompt,
    ]
    env = dict(os.environ)
    for key in list(env):
        if key.startswith("PONYTAIL_"):
            env.pop(key)
    started = time.monotonic()
    try:
        completed = subprocess.run(
            command, cwd=workspace, env=env, text=True, stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT, timeout=args.timeout, check=False,
        )
        raw, returncode = completed.stdout, completed.returncode
    except subprocess.TimeoutExpired as exc:
        raw, returncode = (exc.stdout or "") + "\nTIMEOUT\n", 124
    log_path.parent.mkdir(parents=True, exist_ok=True)
    log_path.write_text(raw, encoding="utf-8")
    return {
        "returncode": returncode,
        "duration_seconds": round(time.monotonic() - started, 2),
        "usage": pilot.parse_usage(raw),
        "log": str(log_path),
    }


def sum_usage(stages):
    result = {}
    for stage in stages:
        for key, value in stage.get("usage", {}).items():
            if isinstance(value, (int, float)):
                result[key] = result.get(key, 0) + value
    return result


def execute_cell(args, task_name, arm, repetition, ponytail, structure):
    cell_id = f"{task_name}--{arm}--r{repetition}"
    cell_path = args.output / "cells" / f"{cell_id}.json"
    if cell_path.exists():
        return json.loads(cell_path.read_text(encoding="utf-8"))
    workspace = args.output / "runs" / task_name / arm / f"r{repetition}"
    runs_root = (args.output / "runs").resolve()
    if workspace.exists():
        resolved = workspace.resolve()
        if not resolved.is_relative_to(runs_root):
            raise RuntimeError(f"unsafe workspace cleanup target: {resolved}")
        shutil.rmtree(workspace)
    pilot.seed_workspace(workspace, TASKS[task_name])
    task_prompt = (
        TASKS[task_name]["prompt"]
        + "\n\nWork directly in the current directory. Inspect relevant code before editing, "
        "make the change, and run any focused checks you consider useful."
    )
    stages = []
    if arm == "staged":
        stages.append(invoke(
            args, workspace,
            task_prompt + f'\n\n<skill-guidance name="structure-first">\n{structure}\n</skill-guidance>',
            args.output / "logs" / f"{cell_id}--structure.jsonl",
        ))
        if stages[-1]["returncode"] == 0:
            stages.append(invoke(
                args, workspace,
                task_prompt
                + "\n\nReview the current implementation and git diff, then simplify it in place. "
                "Preserve every requested observable behavior and boundary contract established by "
                "the existing diff; remove only unnecessary implementation, dependencies, or abstraction."
                + f'\n\n<skill-guidance name="ponytail">\n{ponytail}\n</skill-guidance>',
                args.output / "logs" / f"{cell_id}--ponytail.jsonl",
            ))
    else:
        stages.append(invoke(
            args, workspace, task_prompt + guidance(arm, ponytail, structure),
            args.output / "logs" / f"{cell_id}.jsonl",
        ))
    with pilot.SCORE_LOCK:
        score = SCORERS[task_name](workspace)
    result = {
        "task": task_name,
        "arm": arm,
        "repetition": repetition,
        "returncode": next((stage["returncode"] for stage in stages if stage["returncode"]), 0),
        "duration_seconds": round(sum(stage["duration_seconds"] for stage in stages), 2),
        "score": score,
        "diff": pilot.diff_metrics(workspace),
        "usage": sum_usage(stages),
        "stages": stages,
        "workspace": str(workspace),
    }
    cell_path.parent.mkdir(parents=True, exist_ok=True)
    temporary = cell_path.with_suffix(".tmp")
    temporary.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    temporary.replace(cell_path)
    return result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--ponytail", type=Path, required=True)
    parser.add_argument("--structure", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--model", default="gpt-5.6-luna")
    parser.add_argument("--reasoning", default="medium")
    parser.add_argument("--workers", type=int, default=4)
    parser.add_argument("--timeout", type=int, default=600)
    parser.add_argument("--runs", type=int, default=4)
    parser.add_argument("--tasks", default=",".join(TASKS))
    parser.add_argument("--arms", default="baseline,ponytail,structure_full,structure_core,combined,staged")
    parser.add_argument("--selftest", action="store_true")
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=True)
    if args.selftest:
        selftest(args.output)
        return
    ponytail = args.ponytail.read_text(encoding="utf-8")
    structure = args.structure.read_text(encoding="utf-8")
    task_names = tuple(name for name in args.tasks.split(",") if name)
    arms = tuple(name for name in args.arms.split(",") if name)
    allowed_arms = {"baseline", "ponytail", "structure_full", "structure_core", "combined", "staged"}
    unknown_tasks = set(task_names) - set(TASKS)
    unknown_arms = set(arms) - allowed_arms
    if unknown_tasks or unknown_arms:
        raise SystemExit(f"unknown tasks={sorted(unknown_tasks)} arms={sorted(unknown_arms)}")
    cells = [
        (task, arm, repetition)
        for task in task_names for arm in arms for repetition in range(1, args.runs + 1)
    ]
    results = []
    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        futures = {
            pool.submit(execute_cell, args, task, arm, repetition, ponytail, structure): (task, arm, repetition)
            for task, arm, repetition in cells
        }
        for future in as_completed(futures):
            task, arm, repetition = futures[future]
            try:
                result = future.result()
            except Exception as exc:
                result = {"task": task, "arm": arm, "repetition": repetition, "error": repr(exc)}
            results.append(result)
            compact = {
                "task": task,
                "arm": arm,
                "r": repetition,
                "status": result.get("returncode", "error"),
                "score": result.get("score"),
                "diff": result.get("diff"),
            }
            print(json.dumps(compact, ensure_ascii=False), flush=True)
    results.sort(key=lambda item: (item["task"], item["arm"], item["repetition"]))
    summary = args.output / "results.json"
    summary.write_text(json.dumps(results, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(summary)


if __name__ == "__main__":
    main()
