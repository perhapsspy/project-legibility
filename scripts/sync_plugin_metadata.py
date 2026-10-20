#!/usr/bin/env python3
"""Generate client manifests from the portable plugin manifest."""

from __future__ import annotations

import argparse
import copy
import json
import sys
from pathlib import Path
from typing import Any


PLUGIN_ROOT = Path(__file__).resolve().parents[1] / "plugins/project-legibility"
SCHEMA = "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json"
PORTABLE_FIELDS = {
    "name", "version", "description", "author", "homepage", "repository",
    "license", "keywords",
}
CODEX_PATH = Path(".codex-plugin/plugin.json")
CLAUDE_PATH = Path(".claude-plugin/plugin.json")


def client_manifests(portable: dict[str, Any]) -> dict[Path, dict[str, Any]]:
    """Project only supported identity and client fields into each manifest."""
    if not isinstance(portable, dict) or portable.get("$schema") != SCHEMA:
        raise ValueError("plugin.json must declare the Agent Plugins 1.0 schema")
    if set(portable) != PORTABLE_FIELDS | {"$schema", "extensions"}:
        raise ValueError("plugin.json must contain the supported identity fields and extensions")
    extensions = portable.get("extensions")
    if not isinstance(extensions, dict) or set(extensions) != {"com.openai"}:
        raise ValueError("extensions must contain com.openai")
    openai = extensions["com.openai"]
    if not isinstance(openai, dict) or set(openai) != {"interface"}:
        raise ValueError("com.openai must contain interface for this skills-only plugin")
    interface = openai["interface"]
    if not isinstance(interface, dict) or not isinstance(interface.get("displayName"), str):
        raise ValueError("com.openai.interface must include displayName")
    identity = {key: copy.deepcopy(value) for key, value in portable.items() if key in PORTABLE_FIELDS}
    return {
        CODEX_PATH: {**identity, "skills": "./skills/", "interface": copy.deepcopy(interface)},
        CLAUDE_PATH: {**identity, "displayName": interface["displayName"]},
    }


def sync_metadata(plugin_root: Path, *, write: bool = False) -> list[str]:
    portable = json.loads((plugin_root / "plugin.json").read_text(encoding="utf-8"))
    errors = []
    for relative, expected in client_manifests(portable).items():
        path = plugin_root / relative
        if write:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(json.dumps(expected, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        else:
            try:
                actual = json.loads(path.read_text(encoding="utf-8"))
            except (OSError, ValueError) as exc:
                errors.append(f"{relative}: cannot read generated manifest ({exc})")
                continue
            if actual != expected:
                errors.append(f"{relative}: differs from plugin.json; run scripts/sync_plugin_metadata.py write")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=["check", "write"])
    parser.add_argument("--plugin-root", type=Path, default=PLUGIN_ROOT)
    args = parser.parse_args()
    try:
        errors = sync_metadata(args.plugin_root, write=args.command == "write")
    except (OSError, ValueError) as exc:
        errors = [str(exc)]
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print(f"Client manifest {args.command} passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
