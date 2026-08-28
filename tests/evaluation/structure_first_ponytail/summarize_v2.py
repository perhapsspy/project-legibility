#!/usr/bin/env python3
"""Summarize a run_v2.py results.json without reading raw transcripts."""

import argparse
import json
import statistics
from collections import defaultdict
from pathlib import Path


def median(values):
    return statistics.median(values)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("results", type=Path)
    args = parser.parse_args()
    rows = json.loads(args.results.read_text(encoding="utf-8"))
    if any("error" in row or row.get("returncode") for row in rows):
        raise SystemExit("results contain failed cells")

    grouped = defaultdict(list)
    by_arm = defaultdict(list)
    for row in rows:
        grouped[(row["task"], row["arm"])].append(row)
        by_arm[row["arm"]].append(row)

    print("| task | arm | contract | net LOC median [range] | duration median |")
    print("|---|---|---:|---:|---:|")
    for (task, arm), cells in sorted(grouped.items()):
        loc = [cell["diff"]["added"] - cell["diff"]["deleted"] for cell in cells]
        duration = [cell["duration_seconds"] for cell in cells]
        passed = sum(cell["score"]["contract"] for cell in cells)
        print(
            f"| {task} | {arm} | {passed}/{len(cells)} | "
            f"{median(loc):g} [{min(loc)}, {max(loc)}] | {median(duration):.1f}s |"
        )

    print("\n| arm | correctness | contract | calls | duration total | non-cached input | output |")
    print("|---|---:|---:|---:|---:|---:|---:|")
    for arm, cells in sorted(by_arm.items()):
        correct = sum(cell["score"]["correct"] for cell in cells)
        contract = sum(cell["score"]["contract"] for cell in cells)
        calls = sum(len(cell["stages"]) for cell in cells)
        duration = sum(cell["duration_seconds"] for cell in cells)
        non_cached = sum(
            cell["usage"].get("input_tokens", 0) - cell["usage"].get("cached_input_tokens", 0)
            for cell in cells
        )
        output = sum(cell["usage"].get("output_tokens", 0) for cell in cells)
        print(
            f"| {arm} | {correct}/{len(cells)} | {contract}/{len(cells)} | {calls} | "
            f"{duration:.0f}s | {non_cached:,} | {output:,} |"
        )


if __name__ == "__main__":
    main()
