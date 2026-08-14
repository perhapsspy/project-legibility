#!/usr/bin/env python3
"""Publish an already reviewed Project Legibility release.

Preparation (source pins, version, changelog, review and commit) happens before
this command. Publication reconciles observable Git/GitHub state; rerunning it
is the recovery mechanism and no journal is written.
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
import time
from pathlib import Path
from typing import Callable, Sequence
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]
MARKETPLACE = Path(".agents/plugins/marketplace.json")
VERSION_RE = re.compile(r"^\d+\.\d+\.\d+(?:[-+][0-9A-Za-z.-]+)?$")


class ReleaseError(RuntimeError):
    """An actionable release precondition or external-command failure."""


class CommandResult:
    def __init__(self, stdout: str = "", returncode: int = 0):
        self.stdout, self.returncode = stdout, returncode


class CommandRunner:
    def run(self, args: Sequence[str], *, cwd: Path | None = None, check: bool = True) -> CommandResult:
        try:
            result = subprocess.run(list(args), cwd=cwd, text=True, capture_output=True, check=False)
        except OSError as exc:
            raise ReleaseError(f"could not run {' '.join(args)}: {exc}") from exc
        output = (result.stdout or "").strip()
        if result.returncode and check:
            raise ReleaseError(f"{' '.join(args)}: {(result.stderr or result.stdout or 'command failed').strip()}")
        return CommandResult(output, result.returncode)


def validate_version(version: str) -> str:
    if not VERSION_RE.fullmatch(version):
        raise ReleaseError(f"invalid version: {version!r}")
    return version


def _sha(value: str) -> str:
    value = value.strip()
    if not re.fullmatch(r"[0-9a-f]{40}", value):
        raise ReleaseError(f"expected a full commit SHA, got {value!r}")
    return value


class ReleaseOrchestrator:
    def __init__(self, *, repo_root: Path = ROOT, runner: CommandRunner | None = None,
                 sleeper: Callable[[float], None] = time.sleep, ci_timeout: float = 300,
                 ci_poll_interval: float = 3) -> None:
        self.root = Path(repo_root).resolve()
        self.runner = runner or CommandRunner()
        self.sleeper = sleeper
        self.ci_timeout = ci_timeout
        self.ci_poll_interval = ci_poll_interval

    def command(self, args: Sequence[str], *, cwd: Path | None = None, check: bool = True) -> str:
        return self.runner.run(args, cwd=cwd or self.root, check=check).stdout

    def _project_preflight(self, version: str) -> str:
        if self.command(["git", "branch", "--show-current"]) != "main":
            raise ReleaseError("project checkout must be on main")
        if self.command(["git", "status", "--porcelain"]):
            raise ReleaseError("project checkout must be clean; publish a reviewed commit first")
        head = _sha(self.command(["git", "rev-parse", "HEAD"]))
        manifest = self.root / "plugins/project-legibility/.codex-plugin/plugin.json"
        try:
            actual = json.loads(manifest.read_text(encoding="utf-8"))["version"]
        except (OSError, KeyError, json.JSONDecodeError) as exc:
            raise ReleaseError(f"cannot read plugin version: {manifest}") from exc
        if actual != version:
            raise ReleaseError(f"manifest version is {actual!r}, expected {version!r}")
        self.command([sys.executable, "scripts/validate_bundle.py", "--release-tag", f"v{version}"])
        self._verify_repo_identity(self.root, "perhapsspy/project-legibility")
        return head

    def _verify_repo_identity(self, repo: Path, expected: str) -> None:
        resolved_hosts: dict[str, str] = {}
        for label, args in (
            ("fetch", ["git", "remote", "get-url", "origin"]),
            ("push", ["git", "remote", "get-url", "--push", "origin"]),
        ):
            origin = self.command(args, cwd=repo)
            parsed = urlsplit(origin if "://" in origin else f"ssh://{origin.replace(':', '/', 1)}")
            host = parsed.hostname or ""
            if parsed.scheme == "ssh" and host != "github.com":
                if host not in resolved_hosts:
                    config = self.command(["ssh", "-G", host], cwd=repo)
                    resolved_hosts[host] = next(
                        (line.split(maxsplit=1)[1] for line in config.splitlines() if line.startswith("hostname ")),
                        "",
                    )
                host = resolved_hosts[host]
            if host != "github.com":
                raise ReleaseError(f"origin {label} host {host!r} is not 'github.com'")
            path = parsed.path.strip("/").removesuffix(".git")
            if path != expected:
                raise ReleaseError(f"origin {label} path {path!r} is not {expected!r}")
        actual = self.command(["gh", "repo", "view", "--json", "nameWithOwner", "--jq", ".nameWithOwner"], cwd=repo)
        if actual != expected:
            raise ReleaseError(f"GitHub repository identity mismatch: {actual!r}")

    def _remote_head(self, repo: Path) -> str:
        line = self.command(["git", "ls-remote", "origin", "refs/heads/main"], cwd=repo)
        return line.split()[0] if line else ""

    def _sync_project_main(self, head: str, *, allow_remote_ahead: bool = False) -> None:
        remote = self._remote_head(self.root)
        if remote == head:
            return
        self.command(["git", "fetch", "origin", "main"], cwd=self.root)
        contains = self.runner.run(["git", "merge-base", "--is-ancestor", head, "origin/main"], cwd=self.root, check=False)
        if contains.returncode == 0:
            if allow_remote_ahead:
                return
            raise ReleaseError("project main is ahead of local HEAD; prepare a release from current main")
        ahead = self.runner.run(["git", "merge-base", "--is-ancestor", "origin/main", head], cwd=self.root, check=False)
        if ahead.returncode != 0:
            raise ReleaseError("project main and local HEAD have diverged")
        self.command(["git", "push", "origin", f"{head}:main"], cwd=self.root)

    def _tag_commit(self, tag: str) -> str | None:
        output = self.command(["git", "ls-remote", "origin", f"refs/tags/{tag}", f"refs/tags/{tag}^{{}}"], cwd=self.root)
        values = [line.split()[0] for line in output.splitlines() if line.split()]
        return values[-1] if values else None

    def _local_tag_commit(self, tag: str) -> str | None:
        result = self.runner.run(["git", "rev-list", "-n", "1", tag], cwd=self.root, check=False)
        return result.stdout.strip() if result.returncode == 0 and result.stdout.strip() else None

    def _wait_ci(self, workflow: str, head: str, *, repo: Path | None = None) -> None:
        repo = repo or self.root
        deadline = time.monotonic() + self.ci_timeout
        while True:
            data = json.loads(self.command(["gh", "run", "list", "--workflow", workflow, "--commit", head,
                                             "--json", "headSha,status,conclusion,databaseId", "--limit", "20"], cwd=repo) or "[]")
            exact = [run for run in data if run.get("headSha") == head]
            if any(run.get("conclusion") == "success" for run in exact):
                return
            if any(run.get("status") in {"queued", "in_progress"} for run in exact):
                if time.monotonic() >= deadline:
                    raise ReleaseError(f"timed out waiting for {workflow} at {head}")
                self.sleeper(self.ci_poll_interval)
                continue
            if any(run.get("conclusion") in {"failure", "cancelled", "timed_out"} for run in exact):
                raise ReleaseError(f"{workflow} failed for {head}")
            if time.monotonic() >= deadline:
                raise ReleaseError(f"timed out waiting for {workflow} at {head}")
            self.sleeper(self.ci_poll_interval)

    def _wait_release(self, tag: str, head: str) -> None:
        deadline = time.monotonic() + self.ci_timeout
        while True:
            release_view = self.runner.run(["gh", "release", "view", tag], cwd=self.root, check=False)
            if release_view.returncode == 0:
                return
            data = json.loads(self.command(["gh", "run", "list", "--workflow", "release.yml", "--json",
                                             "headSha,status,conclusion", "--limit", "20"]) or "[]")
            exact = [run for run in data if run.get("headSha") == head]
            if any(run.get("conclusion") == "success" for run in exact):
                self.command(["gh", "release", "view", tag], cwd=self.root)
                return
            if any(run.get("status") in {"queued", "in_progress"} for run in exact):
                if time.monotonic() >= deadline:
                    raise ReleaseError(f"timed out waiting for release {tag}")
                self.sleeper(self.ci_poll_interval)
                continue
            if any(run.get("conclusion") in {"failure", "cancelled", "timed_out"} for run in exact):
                raise ReleaseError(f"release workflow failed for {tag}")
            if time.monotonic() >= deadline:
                raise ReleaseError(f"timed out waiting for release {tag}")
            self.sleeper(self.ci_poll_interval)

    def _publish_tag(self, version: str, head: str) -> None:
        tag = f"v{version}"
        # A correct tag is not proof that its CI and GitHub Release completed.
        self._wait_ci("ci.yml", head)
        existing = self._tag_commit(tag)
        if existing:
            if existing != head:
                raise ReleaseError(f"tag {tag} already points to {existing}, expected {head}")
            self._wait_release(tag, head)
            return
        local = self._local_tag_commit(tag)
        if local:
            if local != head:
                raise ReleaseError(f"local tag {tag} already points to {local}, expected {head}")
        else:
            self.command(["git", "tag", "-a", tag, head, "-m", f"Release {tag}"], cwd=self.root)
        self.command(["git", "push", "origin", tag], cwd=self.root)
        self._wait_release(tag, head)

    def _catalog_preflight(self, catalog: Path) -> Path:
        catalog = catalog.resolve()
        if self.command(["git", "branch", "--show-current"], cwd=catalog) != "main":
            raise ReleaseError("catalog checkout must be on main")
        if self.command(["git", "status", "--porcelain"], cwd=catalog):
            raise ReleaseError("catalog checkout must be clean")
        self._verify_repo_identity(catalog, "perhapsspy/codex-plugins")
        self.command(["git", "pull", "--ff-only", "origin", "main"], cwd=catalog)
        return catalog

    def _publish_catalog(self, catalog: Path, head: str) -> None:
        catalog = self._catalog_preflight(catalog)
        self._publish_catalog_prepared(catalog, head)

    def _publish_catalog_prepared(self, catalog: Path, head: str) -> None:
        path = catalog / MARKETPLACE
        data = json.loads(path.read_text(encoding="utf-8"))
        target = next((item for item in data["plugins"] if item.get("name") == "project-legibility"), None)
        if not target:
            raise ReleaseError("catalog has no project-legibility entry")
        if target["source"].get("sha") == head:
            local_head = self.command(["git", "rev-parse", "HEAD"], cwd=catalog)
            remote_head = self.command(["git", "ls-remote", "origin", "refs/heads/main"], cwd=catalog).split()
            if not remote_head or remote_head[0] != local_head:
                self.command(["git", "push", "origin", "main"], cwd=catalog)
            self._wait_ci("ci.yml", local_head, repo=catalog)
            return
        target["source"]["sha"] = head
        path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
        changed = self.command(["git", "diff", "--name-only"], cwd=catalog).splitlines()
        if changed != [str(MARKETPLACE)]:
            raise ReleaseError(f"catalog update touched unexpected files: {changed}")
        try:
            self.command([sys.executable, "scripts/validate_marketplace.py", "--verify-remote"], cwd=catalog)
            self.command(["git", "add", str(MARKETPLACE)], cwd=catalog)
            self.command(["git", "commit", "-m", f"Update project-legibility to {head[:12]}"], cwd=catalog)
        except ReleaseError:
            self.command(["git", "restore", "--staged", "--worktree", "--", str(MARKETPLACE)], cwd=catalog, check=False)
            raise
        self.command(["git", "push", "origin", "main"], cwd=catalog)
        self._wait_ci("ci.yml", self.command(["git", "rev-parse", "HEAD"], cwd=catalog), repo=catalog)

    def publish(self, version: str, catalog_root: Path) -> str:
        version = validate_version(version)
        head = self._project_preflight(version)
        catalog = self._catalog_preflight(catalog_root)
        self.command(["gh", "api", "user"], cwd=self.root)
        tag_commit = self._tag_commit(f"v{version}")
        if tag_commit and tag_commit != head:
            raise ReleaseError(f"tag v{version} already points to {tag_commit}, expected {head}")
        self._sync_project_main(head, allow_remote_ahead=tag_commit == head)
        self._publish_tag(version, head)
        self._publish_catalog_prepared(catalog, head)
        print(f"published v{version} from {head}")
        return head


def parse_args(argv: Sequence[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Publish a reviewed, committed release.")
    sub = parser.add_subparsers(dest="command", required=True)
    publish = sub.add_parser("publish", help="push main, tag/release, and catalog pin")
    publish.add_argument("--version", required=True)
    publish.add_argument("--catalog-root", type=Path, required=True)
    return parser.parse_args(argv)


def main(argv: Sequence[str] | None = None) -> int:
    args = parse_args(argv)
    try:
        ReleaseOrchestrator().publish(args.version, args.catalog_root)
    except ReleaseError as exc:
        print(f"release failed: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
