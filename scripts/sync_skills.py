#!/usr/bin/env python3
"""Rebuild Project Legibility from pinned canonical skill repositories."""

from __future__ import annotations

import argparse
import hashlib
import io
import json
import os
import re
import shutil
import stat
import subprocess
import sys
import tarfile
import tempfile
import uuid
from pathlib import Path, PurePosixPath
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[1]
PLUGIN_ROOT = REPO_ROOT / "plugins" / "project-legibility"
LOCK_PATH = PLUGIN_ROOT / "sources.lock.json"
SKILLS_ROOT = PLUGIN_ROOT / "skills"
NOTICES_PATH = PLUGIN_ROOT / "THIRD_PARTY_NOTICES.md"

COMMIT_RE = re.compile(r"^[0-9a-f]{40}$")
INTEGRITY_RE = re.compile(r"^sha256:[0-9a-f]{64}$")
SLUG_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


class SyncError(RuntimeError):
    """A user-actionable source or bundle contract failure."""


def run_git(repo: Path | None, *args: str, capture_bytes: bool = False) -> str | bytes:
    command = ["git"]
    if repo is not None:
        command.extend(["-C", str(repo)])
    command.extend(args)
    try:
        completed = subprocess.run(
            command,
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=not capture_bytes,
        )
    except FileNotFoundError as exc:
        raise SyncError("git is required but was not found on PATH") from exc
    except subprocess.CalledProcessError as exc:
        stderr = exc.stderr
        if isinstance(stderr, bytes):
            stderr = stderr.decode("utf-8", errors="replace")
        detail = (stderr or "git command failed").strip()
        raise SyncError(f"{' '.join(command)}: {detail}") from exc
    return completed.stdout if capture_bytes else completed.stdout.strip()


def load_lock() -> dict[str, Any]:
    try:
        lock = json.loads(LOCK_PATH.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise SyncError(f"missing lock file: {LOCK_PATH}") from exc
    except json.JSONDecodeError as exc:
        raise SyncError(f"invalid lock JSON at line {exc.lineno}: {exc.msg}") from exc
    validate_lock_shape(lock)
    return lock


def validate_lock_shape(lock: Any) -> None:
    if not isinstance(lock, dict) or lock.get("lockVersion") != 1:
        raise SyncError("sources.lock.json must be an object with lockVersion 1")
    require_exact_keys(lock, {"lockVersion", "sources"}, "lock root")
    sources = lock.get("sources")
    if not isinstance(sources, list) or not sources:
        raise SyncError("sources.lock.json sources must be a non-empty array")

    source_ids: set[str] = set()
    skill_ids: set[str] = set()
    target_paths: set[str] = set()
    for source in sources:
        if not isinstance(source, dict):
            raise SyncError("each source record must be an object")
        require_exact_keys(
            source,
            {"id", "repository", "commit", "license", "skills"},
            "source record",
        )
        source_id = require_slug(source.get("id"), "source id")
        if source_id in source_ids:
            raise SyncError(f"duplicate source id: {source_id}")
        source_ids.add(source_id)

        repository = source.get("repository")
        if not isinstance(repository, str) or not repository.startswith("https://"):
            raise SyncError(f"{source_id}: repository must be a public HTTPS URL")
        if not repository.endswith(f"/perhapsspy/{source_id}.git"):
            raise SyncError(
                f"{source_id}: repository is not the expected canonical source"
            )
        commit = source.get("commit")
        if not isinstance(commit, str) or not COMMIT_RE.fullmatch(commit):
            raise SyncError(
                f"{source_id}: commit must be a lowercase full 40-character SHA"
            )
        if source.get("license") != "MIT":
            raise SyncError(f"{source_id}: license must be MIT")
        skills = source.get("skills")
        if not isinstance(skills, list) or not skills:
            raise SyncError(f"{source_id}: skills must be a non-empty array")
        for skill in skills:
            if not isinstance(skill, dict):
                raise SyncError(f"{source_id}: every skill record must be an object")
            require_exact_keys(
                skill,
                {"id", "sourcePath", "targetPath", "integrity"},
                f"{source_id} skill record",
            )
            skill_id = require_slug(skill.get("id"), f"{source_id} skill id")
            if skill_id in skill_ids:
                raise SyncError(f"duplicate skill id: {skill_id}")
            skill_ids.add(skill_id)
            expected_path = f"skills/{skill_id}"
            for field in ("sourcePath", "targetPath"):
                if skill.get(field) != expected_path:
                    raise SyncError(f"{skill_id}: {field} must be {expected_path!r}")
            target_path = skill["targetPath"]
            if target_path in target_paths:
                raise SyncError(f"duplicate target path: {target_path}")
            target_paths.add(target_path)
            integrity = skill.get("integrity")
            if not isinstance(integrity, str) or not INTEGRITY_RE.fullmatch(integrity):
                raise SyncError(
                    f"{skill_id}: integrity must have form sha256:<64 lowercase hex>"
                )


def require_exact_keys(
    mapping: dict[str, Any],
    allowed: set[str],
    label: str,
) -> None:
    missing = sorted(allowed - mapping.keys())
    unknown = sorted(mapping.keys() - allowed)
    if missing or unknown:
        raise SyncError(
            f"{label} fields are invalid; missing={missing}, unknown={unknown}"
        )


def require_slug(value: Any, label: str) -> str:
    if not isinstance(value, str) or not SLUG_RE.fullmatch(value):
        raise SyncError(f"{label} must be lower kebab-case")
    return value


def command_update(projects_root: Path) -> None:
    lock = load_lock()
    for source in lock["sources"]:
        repo = local_repo_path(projects_root, source["id"])
        verify_update_checkout(repo, source)
        source["commit"] = str(run_git(repo, "rev-parse", "HEAD"))

    with tempfile.TemporaryDirectory(prefix="project-legibility-update-") as temp:
        assembled = Path(temp) / "skills"
        assemble_from_lock(
            lock, assembled, projects_root=projects_root, verify_integrity=False
        )
        update_integrities(lock, assembled)
        install_generated(assembled, lock, render_notices(lock))
    print(
        f"Updated source lock and generated bundle from {len(lock['sources'])} local repositories."
    )


def command_sync(projects_root: Path | None) -> None:
    lock = load_lock()
    with tempfile.TemporaryDirectory(prefix="project-legibility-sync-") as temp:
        assembled = Path(temp) / "skills"
        assemble_from_lock(
            lock, assembled, projects_root=projects_root, verify_integrity=True
        )
        install_generated(assembled, None, render_notices(lock))
    source_label = str(projects_root) if projects_root else "pinned remote repositories"
    print(f"Regenerated bundle from {source_label}.")


def command_check(projects_root: Path | None, offline: bool) -> None:
    lock = load_lock()
    validate_committed_snapshot(lock)
    compare_text(NOTICES_PATH, render_notices(lock), "generated third-party notices")
    if offline:
        print(
            "Offline bundle check passed: lock, snapshot integrity, and notices agree."
        )
        return

    with tempfile.TemporaryDirectory(prefix="project-legibility-check-") as temp:
        assembled = Path(temp) / "skills"
        assemble_from_lock(
            lock, assembled, projects_root=projects_root, verify_integrity=True
        )
        compare_trees(assembled, SKILLS_ROOT)
    source_label = str(projects_root) if projects_root else "pinned remote repositories"
    print(f"Source bundle check passed against {source_label}.")


def local_repo_path(projects_root: Path, source_id: str) -> Path:
    repo = projects_root.expanduser().resolve() / source_id
    if not (repo / ".git").exists():
        raise SyncError(f"{source_id}: expected Git checkout at {repo}")
    return repo


def verify_update_checkout(repo: Path, source: dict[str, Any]) -> None:
    source_id = source["id"]
    status_output = str(run_git(repo, "status", "--porcelain"))
    if status_output:
        raise SyncError(f"{source_id}: canonical checkout must be clean before update")
    branch = str(run_git(repo, "branch", "--show-current"))
    if branch != "main":
        raise SyncError(f"{source_id}: update checkout must be on main, got {branch!r}")
    verify_local_origin(repo, source)

    head = str(run_git(repo, "rev-parse", "HEAD"))
    remote_main = str(
        run_git(None, "ls-remote", source["repository"], "refs/heads/main")
    )
    remote_sha = remote_main.split()[0] if remote_main else ""
    if head != remote_sha:
        raise SyncError(
            f"{source_id}: local HEAD {head} is not pushed as canonical remote main {remote_sha or '<missing>'}"
        )


def assemble_from_lock(
    lock: dict[str, Any],
    destination: Path,
    *,
    projects_root: Path | None,
    verify_integrity: bool,
) -> None:
    destination.mkdir(parents=True, exist_ok=False)
    with tempfile.TemporaryDirectory(prefix="project-legibility-sources-") as temp:
        remote_root = Path(temp)
        for source in lock["sources"]:
            if projects_root is None:
                repo = fetch_remote_source(source, remote_root)
            else:
                repo = local_repo_path(projects_root, source["id"])
                verify_local_origin(repo, source)
                verify_commit_exists(repo, source["commit"], source["id"])
            for skill in source["skills"]:
                target_dir = destination / PurePosixPath(skill["targetPath"]).name
                export_skill(repo, source["commit"], skill["sourcePath"], target_dir)
                integrity = compute_tree_integrity(target_dir)
                if verify_integrity and integrity != skill["integrity"]:
                    raise SyncError(
                        f"{skill['id']}: locked integrity {skill['integrity']} does not match source {integrity}"
                    )


def fetch_remote_source(source: dict[str, Any], remote_root: Path) -> Path:
    repo = remote_root / source["id"]
    run_git(None, "init", "--quiet", str(repo))
    run_git(repo, "remote", "add", "origin", source["repository"])
    run_git(repo, "fetch", "--quiet", "--depth", "1", "origin", source["commit"])
    fetched = str(run_git(repo, "rev-parse", "FETCH_HEAD"))
    if fetched != source["commit"]:
        raise SyncError(
            f"{source['id']}: fetched {fetched}, expected {source['commit']}"
        )
    return repo


def verify_commit_exists(repo: Path, commit: str, source_id: str) -> None:
    try:
        run_git(repo, "cat-file", "-e", f"{commit}^{{commit}}")
    except SyncError as exc:
        raise SyncError(
            f"{source_id}: locked commit {commit} is not available locally"
        ) from exc


def verify_local_origin(repo: Path, source: dict[str, Any]) -> None:
    origin = str(run_git(repo, "remote", "get-url", "origin"))
    expected_suffix = f"perhapsspy/{source['id']}.git"
    if not origin.endswith(expected_suffix):
        raise SyncError(
            f"{source['id']}: origin {origin!r} is not the expected canonical repository"
        )


def export_skill(repo: Path, commit: str, source_path: str, destination: Path) -> None:
    archive = run_git(
        repo, "archive", "--format=tar", commit, source_path, capture_bytes=True
    )
    assert isinstance(archive, bytes)
    prefix = PurePosixPath(source_path)
    files_written = 0
    with tarfile.open(fileobj=io.BytesIO(archive), mode="r:") as tar:
        for member in tar.getmembers():
            member_path = PurePosixPath(member.name)
            if member_path.is_absolute() or ".." in member_path.parts:
                raise SyncError(f"{source_path}: unsafe archive path {member.name!r}")
            if (
                member.isdir()
                and member_path.parts == prefix.parts[: len(member_path.parts)]
            ):
                continue
            if member_path.parts[: len(prefix.parts)] != prefix.parts:
                raise SyncError(
                    f"{source_path}: archive member escaped source path: {member.name!r}"
                )
            relative_parts = member_path.parts[len(prefix.parts) :]
            if not relative_parts:
                continue
            target = destination.joinpath(*relative_parts)
            if member.isdir():
                target.mkdir(parents=True, exist_ok=True)
                continue
            if member.issym() or member.islnk():
                raise SyncError(
                    f"{source_path}: symlink and hardlink entries are not allowed"
                )
            if not member.isfile():
                raise SyncError(
                    f"{source_path}: non-regular archive entry {member.name!r}"
                )
            extracted = tar.extractfile(member)
            if extracted is None:
                raise SyncError(f"{source_path}: could not read {member.name!r}")
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(extracted.read())
            target.chmod(0o755 if member.mode & 0o111 else 0o644)
            files_written += 1
    if files_written == 0 or not (destination / "SKILL.md").is_file():
        raise SyncError(f"{source_path}: exported skill is empty or missing SKILL.md")


def update_integrities(lock: dict[str, Any], assembled: Path) -> None:
    for source in lock["sources"]:
        for skill in source["skills"]:
            skill_dir = assembled / PurePosixPath(skill["targetPath"]).name
            skill["integrity"] = compute_tree_integrity(skill_dir)


def compute_tree_integrity(root: Path) -> str:
    records: list[dict[str, Any]] = []
    for path in sorted(
        root.rglob("*"), key=lambda item: item.relative_to(root).as_posix()
    ):
        relative = path.relative_to(root).as_posix()
        if path.is_symlink():
            raise SyncError(f"symlink is not allowed: {relative}")
        if path.is_dir():
            continue
        if not path.is_file():
            raise SyncError(f"non-regular file is not allowed: {relative}")
        records.append(
            {
                "path": relative,
                "executableBit": bool(path.stat().st_mode & stat.S_IXUSR),
                "fileSha256": hashlib.sha256(path.read_bytes()).hexdigest(),
            }
        )
    payload = json.dumps(
        records,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")
    return f"sha256:{hashlib.sha256(payload).hexdigest()}"


def validate_committed_snapshot(lock: dict[str, Any]) -> None:
    expected = sorted(
        skill["id"] for source in lock["sources"] for skill in source["skills"]
    )
    if not SKILLS_ROOT.is_dir():
        raise SyncError(f"generated skills directory is missing: {SKILLS_ROOT}")
    actual = sorted(path.name for path in SKILLS_ROOT.iterdir() if path.is_dir())
    extras = sorted(path.name for path in SKILLS_ROOT.iterdir() if not path.is_dir())
    if actual != expected or extras:
        raise SyncError(
            f"generated skill catalog mismatch: expected {expected}, got {actual}, files {extras}"
        )
    for source in lock["sources"]:
        for skill in source["skills"]:
            skill_dir = SKILLS_ROOT / skill["id"]
            integrity = compute_tree_integrity(skill_dir)
            if integrity != skill["integrity"]:
                raise SyncError(
                    f"{skill['id']}: snapshot integrity {integrity} does not match lock {skill['integrity']}"
                )


def render_notices(lock: dict[str, Any]) -> str:
    lines = [
        "# Third-party notices",
        "",
        "This file is generated from `sources.lock.json`. Do not edit it directly.",
        "",
        "Project Legibility bundles unchanged skill directories from the following canonical repositories.",
        "All listed sources use the MIT License; the license text is included in `LICENSE`.",
        "",
        "| Canonical source | Commit | Bundled skills | License |",
        "|---|---|---|---|",
    ]
    for source in lock["sources"]:
        skills = ", ".join(f"`{skill['id']}`" for skill in source["skills"])
        repository = source["repository"].removesuffix(".git")
        commit = source["commit"]
        lines.append(
            f"| [{source['id']}]({repository}) | [`{commit[:12]}`]({repository}/commit/{commit}) | {skills} | {source['license']} |"
        )
    lines.append("")
    return "\n".join(lines)


def compare_text(path: Path, expected: str, label: str) -> None:
    try:
        actual = path.read_text(encoding="utf-8")
    except FileNotFoundError as exc:
        raise SyncError(f"{label} is missing: {path}") from exc
    if actual != expected:
        raise SyncError(f"{label} differs from sources.lock.json: {path}")


def tree_records(root: Path) -> dict[str, tuple[bytes, bool]]:
    records: dict[str, tuple[bytes, bool]] = {}
    for path in sorted(root.rglob("*")):
        relative = path.relative_to(root).as_posix()
        if path.is_symlink():
            raise SyncError(f"symlink is not allowed: {root}/{relative}")
        if path.is_dir():
            continue
        if not path.is_file():
            raise SyncError(f"non-regular file is not allowed: {root}/{relative}")
        records[relative] = (
            path.read_bytes(),
            bool(path.stat().st_mode & stat.S_IXUSR),
        )
    return records


def compare_trees(expected_root: Path, actual_root: Path) -> None:
    expected = tree_records(expected_root)
    actual = tree_records(actual_root)
    if expected.keys() != actual.keys():
        missing = sorted(expected.keys() - actual.keys())
        extra = sorted(actual.keys() - expected.keys())
        raise SyncError(
            f"generated snapshot file set differs; missing={missing}, extra={extra}"
        )
    for relative in expected:
        if expected[relative] != actual[relative]:
            raise SyncError(
                f"generated snapshot differs from canonical source: {relative}"
            )


def install_generated(
    assembled: Path,
    lock: dict[str, Any] | None,
    notices: str,
) -> None:
    token = uuid.uuid4().hex
    next_skills = PLUGIN_ROOT / f".skills.next-{token}"
    next_notices = PLUGIN_ROOT / f".notices.next-{token}"
    next_lock = PLUGIN_ROOT / f".lock.next-{token}"
    backup_skills = PLUGIN_ROOT / f".skills.backup-{token}"
    backup_notices = PLUGIN_ROOT / f".notices.backup-{token}"
    backup_lock = PLUGIN_ROOT / f".lock.backup-{token}"

    shutil.copytree(assembled, next_skills, copy_function=shutil.copy2)
    next_notices.write_text(notices, encoding="utf-8")
    if lock is not None:
        next_lock.write_text(
            json.dumps(lock, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
        )

    replacements = [
        (SKILLS_ROOT, next_skills, backup_skills),
        (NOTICES_PATH, next_notices, backup_notices),
    ]
    if lock is not None:
        replacements.append((LOCK_PATH, next_lock, backup_lock))
    installed: list[tuple[Path, Path]] = []
    try:
        for destination, staged, backup in replacements:
            if destination.exists():
                os.replace(destination, backup)
            installed.append((destination, backup))
            os.replace(staged, destination)
    except Exception:
        for destination, backup in reversed(installed):
            if destination.exists():
                remove_path(destination)
            if backup.exists():
                os.replace(backup, destination)
        raise
    finally:
        for path in (
            next_skills,
            next_notices,
            next_lock,
            backup_skills,
            backup_notices,
            backup_lock,
        ):
            remove_path(path)


def remove_path(path: Path) -> None:
    if path.is_dir() and not path.is_symlink():
        shutil.rmtree(path, ignore_errors=True)
    else:
        try:
            path.unlink()
        except FileNotFoundError:
            pass


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)

    update = subparsers.add_parser(
        "update", help="pin clean pushed local main checkouts and regenerate"
    )
    update.add_argument("--projects-root", type=Path, required=True)

    sync = subparsers.add_parser("sync", help="regenerate from the existing lock")
    sync.add_argument("--projects-root", type=Path)

    check = subparsers.add_parser(
        "check", help="verify the committed lock and generated bundle"
    )
    check.add_argument("--projects-root", type=Path)
    check.add_argument("--offline", action="store_true")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    try:
        if args.command == "update":
            command_update(args.projects_root)
        elif args.command == "sync":
            command_sync(args.projects_root)
        elif args.command == "check":
            if args.offline and args.projects_root is not None:
                raise SyncError("--offline cannot be combined with --projects-root")
            command_check(args.projects_root, args.offline)
        else:  # pragma: no cover - argparse prevents this branch
            raise SyncError(f"unsupported command: {args.command}")
    except SyncError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
