#!/usr/bin/env python3
"""Validate the committed Project Legibility plugin bundle.

The validator is intentionally dependency-free so the same contract can run in
local development, CI, and release jobs.  It validates the assembled artifact;
source fetching and reconstruction remain owned by ``sync_skills.py``.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import stat
import sys
from dataclasses import dataclass, field
from pathlib import Path, PurePosixPath
from typing import Any, Iterable
from urllib.parse import unquote, urlsplit


PLUGIN_NAME = "project-legibility"
PLUGIN_ROOT_REL = Path("plugins") / PLUGIN_NAME
MANIFEST_REL = PLUGIN_ROOT_REL / ".codex-plugin" / "plugin.json"
LOCK_REL = PLUGIN_ROOT_REL / "sources.lock.json"
CHANGELOG_REL = Path("CHANGELOG.md")

EXPECTED_SKILLS = (
    "agents-md-editor",
    "codex-token-discipline",
    "design-user-interfaces",
    "interactive-state-flow",
    "project-context",
    "project-context-migration",
    "purpose-fit-design",
    "semantic-boundary-design",
    "source-owner-audit",
    "structure-first",
    "tighten-docs",
)
EXPECTED_SOURCE_SKILLS = {
    "agents-md-editor": ("agents-md-editor",),
    "codex-token-discipline": ("codex-token-discipline",),
    "design-user-interfaces": ("design-user-interfaces",),
    "interactive-state-flow": ("interactive-state-flow",),
    "project-context": ("project-context", "project-context-migration"),
    "purpose-fit-design": ("purpose-fit-design",),
    "semantic-boundary-design": ("semantic-boundary-design",),
    "source-owner-audit": ("source-owner-audit",),
    "structure-first": ("structure-first",),
    "tighten-docs": ("tighten-docs",),
}
EXPECTED_REPOSITORIES = {
    source_id: f"https://github.com/perhapsspy/{source_id}"
    for source_id in EXPECTED_SOURCE_SKILLS
}
FORBIDDEN_SKILLS = (
    "justified-change",
    "structure-first-docs",
    "work-board",
)

EXPECTED_CATALOG_REL = Path("tests") / "catalog" / "expected-skills.json"
FORBIDDEN_CATALOG_REL = Path("tests") / "catalog" / "forbidden-skills.json"
TRIGGER_CASES_REL = Path("tests") / "routing" / "trigger-cases.json"
NON_TRIGGER_CASES_REL = Path("tests") / "routing" / "non-trigger-cases.json"

SEMVER_PATTERN = re.compile(
    r"^(0|[1-9]\d*)\."
    r"(0|[1-9]\d*)\."
    r"(0|[1-9]\d*)"
    r"(?:-(?:0|[1-9]\d*|\d*[A-Za-z-][0-9A-Za-z-]*)"
    r"(?:\.(?:0|[1-9]\d*|\d*[A-Za-z-][0-9A-Za-z-]*))*)?"
    r"(?:\+[0-9A-Za-z-]+(?:\.[0-9A-Za-z-]+)*)?$"
)
RELEASE_TAG_PATTERN = re.compile(r"^v((?:0|[1-9]\d*)\.(?:0|[1-9]\d*)\.(?:0|[1-9]\d*))$")
COMMIT_PATTERN = re.compile(r"^[0-9a-f]{40}$")
INTEGRITY_PATTERN = re.compile(r"^sha256:[0-9a-f]{64}$")
CASE_ID_PATTERN = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
REFERENCE_LINK_PATTERN = re.compile(
    r"^\s{0,3}\[[^\]]+\]:\s*(?P<destination><[^>]+>|\S+)"
)


@dataclass
class ValidationErrors:
    """Collect independent contract failures for one actionable report."""

    items: list[str] = field(default_factory=list)

    def add(self, location: Path | str, message: str) -> None:
        self.items.append(f"{location}: {message}")


def validate_bundle(repo_root: Path, release_tag: str | None = None) -> list[str]:
    """Return every bundle validation error found beneath ``repo_root``."""

    repo_root = repo_root.resolve()
    errors = ValidationErrors()
    plugin_root = repo_root / PLUGIN_ROOT_REL
    skills_root = plugin_root / "skills"

    manifest = load_json(repo_root / MANIFEST_REL, errors)
    lock = load_json(repo_root / LOCK_REL, errors)
    expected_catalog = load_json(repo_root / EXPECTED_CATALOG_REL, errors)
    forbidden_catalog = load_json(repo_root / FORBIDDEN_CATALOG_REL, errors)
    trigger_cases = load_json(repo_root / TRIGGER_CASES_REL, errors)
    non_trigger_cases = load_json(repo_root / NON_TRIGGER_CASES_REL, errors)

    validate_no_symlinks(plugin_root, repo_root, errors)
    validate_manifest(manifest, plugin_root, MANIFEST_REL, release_tag, errors)
    validate_catalog(
        expected_catalog,
        EXPECTED_CATALOG_REL,
        EXPECTED_SKILLS,
        errors,
    )
    validate_catalog(
        forbidden_catalog,
        FORBIDDEN_CATALOG_REL,
        FORBIDDEN_SKILLS,
        errors,
    )
    lock_skills = validate_lock(lock, LOCK_REL, errors)
    validate_bundled_skills(skills_root, repo_root, errors)
    validate_snapshot_integrity(plugin_root, lock_skills, repo_root, errors)
    validate_markdown_links(skills_root, repo_root, errors)
    validate_routing_cases(
        trigger_cases,
        TRIGGER_CASES_REL,
        expected_result="select",
        errors=errors,
    )
    validate_routing_cases(
        non_trigger_cases,
        NON_TRIGGER_CASES_REL,
        expected_result="do-not-select",
        errors=errors,
    )
    validate_removed_names(repo_root, plugin_root, errors)
    if release_tag is not None:
        validate_release_changelog(repo_root / CHANGELOG_REL, release_tag, errors)

    return sorted(errors.items)


def load_json(path: Path, errors: ValidationErrors) -> Any | None:
    try:
        with path.open("r", encoding="utf-8") as handle:
            return json.load(handle)
    except FileNotFoundError:
        errors.add(path, "required JSON file is missing")
    except UnicodeDecodeError as exc:
        errors.add(path, f"is not valid UTF-8 ({exc})")
    except json.JSONDecodeError as exc:
        errors.add(
            path, f"invalid JSON at line {exc.lineno}, column {exc.colno}: {exc.msg}"
        )
    except OSError as exc:
        errors.add(path, f"could not be read ({exc})")
    return None


def validate_manifest(
    manifest: Any,
    plugin_root: Path,
    manifest_path: Path,
    release_tag: str | None,
    errors: ValidationErrors,
) -> None:
    if not isinstance(manifest, dict):
        if manifest is not None:
            errors.add(manifest_path, "manifest root must be a JSON object")
        return

    require_exact(manifest, "name", PLUGIN_NAME, manifest_path, errors)
    version = require_nonempty_string(manifest, "version", manifest_path, errors)
    if version is not None and not SEMVER_PATTERN.fullmatch(version):
        errors.add(manifest_path, f"version must be strict SemVer, got {version!r}")
    require_nonempty_string(manifest, "description", manifest_path, errors)
    require_exact(manifest, "skills", "./skills/", manifest_path, errors)
    require_exact(manifest, "license", "MIT", manifest_path, errors)

    author = manifest.get("author")
    if not isinstance(author, dict):
        errors.add(manifest_path, "author must be an object")
    else:
        require_nonempty_string(author, "name", manifest_path, errors, prefix="author.")
        validate_optional_https_url(
            author, "url", manifest_path, errors, prefix="author."
        )

    repository = require_nonempty_string(manifest, "repository", manifest_path, errors)
    if repository is not None:
        validate_https_url(repository, "repository", manifest_path, errors)
    validate_optional_https_url(manifest, "homepage", manifest_path, errors)

    for unsupported_component in ("hooks", "apps", "mcpServers"):
        if unsupported_component in manifest:
            errors.add(
                manifest_path,
                f"skills-only v0.1 manifest must omit {unsupported_component!r}",
            )

    interface = manifest.get("interface")
    if not isinstance(interface, dict):
        errors.add(manifest_path, "interface must be an object")
    else:
        validate_interface(interface, plugin_root, manifest_path, errors)

    if "[TODO:" in json.dumps(manifest, ensure_ascii=False):
        errors.add(
            manifest_path, "manifest contains an unresolved [TODO: ...] placeholder"
        )

    if release_tag is not None:
        validate_release_version(version, release_tag, manifest_path, errors)


def validate_interface(
    interface: dict[str, Any],
    plugin_root: Path,
    manifest_path: Path,
    errors: ValidationErrors,
) -> None:
    require_exact(
        interface,
        "displayName",
        "Project Legibility",
        manifest_path,
        errors,
        "interface.",
    )
    for field_name in ("shortDescription", "longDescription", "developerName"):
        require_nonempty_string(
            interface,
            field_name,
            manifest_path,
            errors,
            prefix="interface.",
        )
    require_exact(
        interface, "category", "Developer Tools", manifest_path, errors, "interface."
    )

    capabilities = interface.get("capabilities")
    if not isinstance(capabilities, list) or any(
        not isinstance(capability, str) for capability in capabilities
    ):
        errors.add(manifest_path, "interface.capabilities must be a string array")
    elif len(capabilities) != len(set(capabilities)):
        errors.add(manifest_path, "interface.capabilities must not contain duplicates")
    elif set(capabilities) != {"Read", "Write"}:
        errors.add(
            manifest_path, "interface.capabilities must contain exactly Read and Write"
        )

    prompts = interface.get("defaultPrompt")
    if not isinstance(prompts, list):
        errors.add(manifest_path, "interface.defaultPrompt must be an array")
    elif not 1 <= len(prompts) <= 3:
        errors.add(
            manifest_path,
            "interface.defaultPrompt must contain between 1 and 3 prompts",
        )
    else:
        for index, prompt in enumerate(prompts):
            location = f"interface.defaultPrompt[{index}]"
            if not isinstance(prompt, str) or not prompt.strip():
                errors.add(manifest_path, f"{location} must be a non-empty string")
            elif len(prompt) > 128:
                errors.add(manifest_path, f"{location} exceeds 128 characters")

    for url_field in ("websiteURL", "privacyPolicyURL", "termsOfServiceURL"):
        validate_optional_https_url(
            interface, url_field, manifest_path, errors, prefix="interface."
        )

    for asset_field in ("composerIcon", "logo", "logoDark"):
        value = interface.get(asset_field)
        if value is not None:
            validate_existing_relative_path(
                plugin_root,
                value,
                manifest_path,
                f"interface.{asset_field}",
                errors,
                require_file=True,
                required_parent="assets",
            )

    screenshots = interface.get("screenshots")
    if screenshots is not None:
        if not isinstance(screenshots, list):
            errors.add(manifest_path, "interface.screenshots must be an array")
        else:
            for index, screenshot in enumerate(screenshots):
                validate_existing_relative_path(
                    plugin_root,
                    screenshot,
                    manifest_path,
                    f"interface.screenshots[{index}]",
                    errors,
                    require_file=True,
                    required_parent="assets",
                    required_suffix=".png",
                )


def validate_release_version(
    version: str | None,
    release_tag: str,
    manifest_path: Path,
    errors: ValidationErrors,
) -> None:
    match = RELEASE_TAG_PATTERN.fullmatch(release_tag)
    if match is None:
        errors.add(
            manifest_path, f"release tag must have form vX.Y.Z, got {release_tag!r}"
        )
        return
    if version is not None and version != match.group(1):
        errors.add(
            manifest_path,
            f"manifest version {version!r} does not match release tag {release_tag!r}",
        )
    if version is not None and "+codex.local" in version:
        errors.add(
            manifest_path, "release version must not contain +codex.local metadata"
        )


def validate_release_changelog(
    changelog_path: Path,
    release_tag: str,
    errors: ValidationErrors,
) -> None:
    match = RELEASE_TAG_PATTERN.fullmatch(release_tag)
    if match is None:
        return
    version = re.escape(match.group(1))
    try:
        changelog = changelog_path.read_text(encoding="utf-8")
    except FileNotFoundError:
        errors.add(CHANGELOG_REL, "CHANGELOG.md is required for a release")
        return
    except (OSError, UnicodeDecodeError) as exc:
        errors.add(CHANGELOG_REL, f"CHANGELOG.md could not be read ({exc})")
        return
    if (
        re.search(
            rf"^## \[{version}\](?:\s+-\s+\d{{4}}-\d{{2}}-\d{{2}})?\s*$",
            changelog,
            re.MULTILINE,
        )
        is None
    ):
        errors.add(CHANGELOG_REL, f"missing release heading for [{match.group(1)}]")


def validate_catalog(
    catalog: Any,
    catalog_path: Path,
    expected: Iterable[str],
    errors: ValidationErrors,
) -> None:
    if not isinstance(catalog, dict):
        if catalog is not None:
            errors.add(catalog_path, "catalog root must be a JSON object")
        return
    require_exact(catalog, "schemaVersion", 1, catalog_path, errors)
    skills = catalog.get("skills")
    expected_list = sorted(expected)
    if not isinstance(skills, list) or any(
        not isinstance(item, str) for item in skills
    ):
        errors.add(catalog_path, "skills must be a string array")
    elif skills != expected_list:
        errors.add(
            catalog_path,
            f"skills must equal the sorted contract catalog {expected_list!r}",
        )


def validate_lock(
    lock: Any,
    lock_path: Path,
    errors: ValidationErrors,
) -> dict[str, dict[str, str]]:
    """Validate provenance and return valid skill entries keyed by skill id."""

    if not isinstance(lock, dict):
        if lock is not None:
            errors.add(lock_path, "lock root must be a JSON object")
        return {}
    if set(lock) != {"lockVersion", "sources"}:
        errors.add(lock_path, "lock root may contain only lockVersion and sources")
    require_exact(lock, "lockVersion", 1, lock_path, errors)
    sources = lock.get("sources")
    if not isinstance(sources, list):
        errors.add(lock_path, "sources must be an array")
        return {}
    expected_source_count = len(EXPECTED_SOURCE_SKILLS)
    if len(sources) != expected_source_count:
        errors.add(
            lock_path,
            f"sources must contain exactly {expected_source_count} records, got {len(sources)}",
        )

    source_ids: set[str] = set()
    repositories: set[str] = set()
    skill_entries: dict[str, dict[str, str]] = {}
    source_to_skills: dict[str, set[str]] = {}
    for source_index, source in enumerate(sources):
        location = f"sources[{source_index}]"
        if not isinstance(source, dict):
            errors.add(lock_path, f"{location} must be an object")
            continue
        required_source_fields = {"id", "repository", "commit", "license", "skills"}
        allowed_source_fields = required_source_fields | {"tag"}
        if (
            not required_source_fields <= set(source)
            or not set(source) <= allowed_source_fields
        ):
            errors.add(
                lock_path,
                f"{location} must contain id, repository, commit, license, and skills; tag is optional",
            )
        source_id = source.get("id")
        if not isinstance(source_id, str) or not source_id:
            errors.add(lock_path, f"{location}.id must be a non-empty string")
            source_id = f"<invalid-{source_index}>"
        elif source_id in source_ids:
            errors.add(lock_path, f"duplicate source id {source_id!r}")
        else:
            source_ids.add(source_id)

        repository = source.get("repository")
        if not isinstance(repository, str):
            errors.add(lock_path, f"{location}.repository must be a string")
        else:
            normalized_repository = repository.removesuffix(".git")
            if normalized_repository in repositories:
                errors.add(lock_path, f"duplicate repository {repository!r}")
            repositories.add(normalized_repository)
            expected_repository = EXPECTED_REPOSITORIES.get(source_id)
            if (
                expected_repository is None
                or normalized_repository != expected_repository
            ):
                errors.add(
                    lock_path,
                    f"{location}.repository is not the canonical HTTPS source for {source_id!r}",
                )

        commit = source.get("commit")
        if not isinstance(commit, str) or not COMMIT_PATTERN.fullmatch(commit):
            errors.add(
                lock_path, f"{location}.commit must be a lowercase full 40-hex SHA"
            )
        if source.get("license") != "MIT":
            errors.add(lock_path, f"{location}.license must be 'MIT'")
        if "tag" in source and (
            not isinstance(source["tag"], str) or not source["tag"].strip()
        ):
            errors.add(
                lock_path, f"{location}.tag must be a non-empty string when present"
            )

        skills = source.get("skills")
        if not isinstance(skills, list) or not skills:
            errors.add(lock_path, f"{location}.skills must be a non-empty array")
            continue
        source_to_skills.setdefault(source_id, set())
        for skill_index, skill in enumerate(skills):
            skill_location = f"{location}.skills[{skill_index}]"
            if not isinstance(skill, dict):
                errors.add(lock_path, f"{skill_location} must be an object")
                continue
            if set(skill) != {"id", "sourcePath", "targetPath", "integrity"}:
                errors.add(
                    lock_path,
                    f"{skill_location} fields must be exactly id, sourcePath, targetPath, and integrity",
                )
            skill_id = skill.get("id")
            if not isinstance(skill_id, str) or not skill_id:
                errors.add(lock_path, f"{skill_location}.id must be a non-empty string")
                continue
            if skill_id in skill_entries:
                errors.add(lock_path, f"duplicate skill id {skill_id!r} in lock")
            source_to_skills[source_id].add(skill_id)

            expected_path = f"skills/{skill_id}"
            for path_field in ("sourcePath", "targetPath"):
                value = skill.get(path_field)
                if value != expected_path:
                    errors.add(
                        lock_path,
                        f"{skill_location}.{path_field} must be {expected_path!r}",
                    )
            integrity = skill.get("integrity")
            if not isinstance(integrity, str) or not INTEGRITY_PATTERN.fullmatch(
                integrity
            ):
                errors.add(
                    lock_path,
                    f"{skill_location}.integrity must have form sha256:<64 lowercase hex>",
                )
                continue
            skill_entries[skill_id] = {
                "targetPath": str(skill.get("targetPath", "")),
                "integrity": integrity,
            }

    if source_ids != set(EXPECTED_SOURCE_SKILLS):
        errors.add(
            lock_path,
            f"source ids must equal {sorted(EXPECTED_SOURCE_SKILLS)!r}",
        )
    if set(skill_entries) != set(EXPECTED_SKILLS):
        errors.add(lock_path, f"locked skill ids must equal {list(EXPECTED_SKILLS)!r}")
    for source_id, expected_skills in EXPECTED_SOURCE_SKILLS.items():
        actual = source_to_skills.get(source_id, set())
        if actual != set(expected_skills):
            errors.add(
                lock_path,
                f"source {source_id!r} must own exactly {list(expected_skills)!r}",
            )

    return skill_entries


def validate_bundled_skills(
    skills_root: Path,
    repo_root: Path,
    errors: ValidationErrors,
) -> None:
    if not skills_root.is_dir():
        errors.add(
            relative_location(skills_root, repo_root), "skills directory is missing"
        )
        return
    children = list(skills_root.iterdir())
    directories = sorted(child.name for child in children if child.is_dir())
    non_directories = sorted(child.name for child in children if not child.is_dir())
    if directories != list(EXPECTED_SKILLS):
        errors.add(
            relative_location(skills_root, repo_root),
            f"bundled skill directories must equal {list(EXPECTED_SKILLS)!r}, got {directories!r}",
        )
    if non_directories:
        errors.add(
            relative_location(skills_root, repo_root),
            f"skills root may contain directories only, found {non_directories!r}",
        )

    for skill_id in EXPECTED_SKILLS:
        skill_dir = skills_root / skill_id
        if not skill_dir.is_dir():
            continue
        skill_file = skill_dir / "SKILL.md"
        name, description = read_skill_frontmatter(skill_file, repo_root, errors)
        if name is not None and name != skill_id:
            errors.add(
                relative_location(skill_file, repo_root),
                f"frontmatter name must match directory {skill_id!r}, got {name!r}",
            )
        if description is not None and not description.strip():
            errors.add(
                relative_location(skill_file, repo_root),
                "frontmatter description must be non-empty",
            )


def read_skill_frontmatter(
    skill_file: Path,
    repo_root: Path,
    errors: ValidationErrors,
) -> tuple[str | None, str | None]:
    location = relative_location(skill_file, repo_root)
    try:
        text = skill_file.read_text(encoding="utf-8")
    except FileNotFoundError:
        errors.add(location, "SKILL.md is missing")
        return None, None
    except (OSError, UnicodeDecodeError) as exc:
        errors.add(location, f"SKILL.md could not be read as UTF-8 ({exc})")
        return None, None

    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        errors.add(location, "SKILL.md must start with YAML frontmatter")
        return None, None
    try:
        closing_index = next(
            index
            for index, line in enumerate(lines[1:], start=1)
            if line.strip() == "---"
        )
    except StopIteration:
        errors.add(location, "SKILL.md frontmatter is not closed")
        return None, None

    fields: dict[str, str] = {}
    for line in lines[1:closing_index]:
        if not line or line[0].isspace() or ":" not in line:
            continue
        key, raw_value = line.split(":", 1)
        key = key.strip()
        if key not in {"name", "description"}:
            continue
        if key in fields:
            errors.add(location, f"frontmatter field {key!r} is duplicated")
            continue
        fields[key] = parse_frontmatter_scalar(raw_value.strip(), location, key, errors)

    for required in ("name", "description"):
        if required not in fields:
            errors.add(location, f"frontmatter field {required!r} is required")
    return fields.get("name"), fields.get("description")


def parse_frontmatter_scalar(
    value: str,
    location: Path | str,
    field_name: str,
    errors: ValidationErrors,
) -> str:
    value = strip_yaml_comment(value).strip()
    if value.startswith('"'):
        try:
            parsed = json.loads(value)
        except json.JSONDecodeError:
            errors.add(
                location, f"frontmatter field {field_name!r} has invalid quoted text"
            )
            return ""
        if not isinstance(parsed, str):
            errors.add(location, f"frontmatter field {field_name!r} must be text")
            return ""
        return parsed
    if len(value) >= 2 and value.startswith("'") and value.endswith("'"):
        return value[1:-1].replace("''", "'")
    if value in {"|", ">", "|-", ">-", "|+", ">+"}:
        errors.add(
            location, f"frontmatter field {field_name!r} must use a single-line scalar"
        )
        return ""
    if not value or plain_yaml_value_is_non_string(value):
        errors.add(location, f"frontmatter field {field_name!r} must be text")
        return ""
    return value


def strip_yaml_comment(value: str) -> str:
    """Remove a YAML plain comment while preserving hashes inside quotes."""

    in_single_quote = False
    in_double_quote = False
    escaped = False
    index = 0
    while index < len(value):
        character = value[index]
        if escaped:
            escaped = False
            index += 1
            continue
        if in_double_quote and character == "\\":
            escaped = True
        elif not in_double_quote and character == "'":
            if in_single_quote and index + 1 < len(value) and value[index + 1] == "'":
                index += 1
            else:
                in_single_quote = not in_single_quote
        elif not in_single_quote and character == '"':
            in_double_quote = not in_double_quote
        elif (
            character == "#"
            and not in_single_quote
            and not in_double_quote
            and (index == 0 or value[index - 1].isspace())
        ):
            return value[:index].rstrip()
        index += 1
    return value


def plain_yaml_value_is_non_string(value: str) -> bool:
    lowered = value.lower()
    if lowered in {
        "~",
        "null",
        "true",
        "false",
        "yes",
        "no",
        "on",
        "off",
        ".inf",
        "+.inf",
        "-.inf",
        ".nan",
    }:
        return True
    if value[0] in "[{&*!|>@`" or value.startswith(("- ", "? ")):
        return True
    if re.fullmatch(
        r"[-+]?(?:0[xX][0-9a-fA-F_]+|0[oO][0-7_]+|0[bB][01_]+|"
        r"(?:\d[\d_]*(?:\.\d[\d_]*)?|\.\d[\d_]+)(?:[eE][-+]?\d+)?)",
        value,
    ):
        return True
    return bool(re.fullmatch(r"\d{4}-\d{1,2}-\d{1,2}(?:[Tt ].*)?", value))


def validate_snapshot_integrity(
    plugin_root: Path,
    lock_skills: dict[str, dict[str, str]],
    repo_root: Path,
    errors: ValidationErrors,
) -> None:
    for skill_id, entry in sorted(lock_skills.items()):
        target_path = entry["targetPath"]
        target_dir = resolve_posix_path(plugin_root, target_path)
        if target_dir is None or not is_within(target_dir, plugin_root):
            errors.add(
                LOCK_REL, f"unsafe target path for {skill_id!r}: {target_path!r}"
            )
            continue
        if not target_dir.is_dir():
            errors.add(
                relative_location(target_dir, repo_root),
                "locked skill directory is missing",
            )
            continue
        try:
            actual_integrity = compute_tree_integrity(target_dir)
        except (OSError, ValueError) as exc:
            errors.add(
                relative_location(target_dir, repo_root),
                f"integrity could not be computed ({exc})",
            )
            continue
        if actual_integrity != entry["integrity"]:
            errors.add(
                relative_location(target_dir, repo_root),
                f"integrity mismatch: lock has {entry['integrity']}, snapshot has {actual_integrity}",
            )


def compute_tree_integrity(root: Path) -> str:
    """Return the sync contract's deterministic SHA-256 tree integrity."""

    records: list[dict[str, Any]] = []
    for path in sorted(
        root.rglob("*"), key=lambda item: item.relative_to(root).as_posix()
    ):
        relative_path = path.relative_to(root).as_posix()
        if path.is_symlink():
            raise ValueError(f"symlink is not allowed: {relative_path}")
        if path.is_dir():
            continue
        if not path.is_file():
            raise ValueError(f"non-regular file is not allowed: {relative_path}")
        content = path.read_bytes()
        records.append(
            {
                "path": relative_path,
                "executableBit": bool(path.stat().st_mode & stat.S_IXUSR),
                "fileSha256": hashlib.sha256(content).hexdigest(),
            }
        )
    payload = json.dumps(
        records,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=False,
    ).encode("utf-8")
    return f"sha256:{hashlib.sha256(payload).hexdigest()}"


def validate_no_symlinks(
    plugin_root: Path,
    repo_root: Path,
    errors: ValidationErrors,
) -> None:
    if plugin_root.is_symlink():
        errors.add(
            relative_location(plugin_root, repo_root),
            "plugin root must not be a symlink",
        )
        return
    if not plugin_root.exists():
        errors.add(relative_location(plugin_root, repo_root), "plugin root is missing")
        return
    for path in plugin_root.rglob("*"):
        if path.is_symlink():
            errors.add(
                relative_location(path, repo_root),
                "symlinks are not allowed in the bundle",
            )


def validate_markdown_links(
    skills_root: Path,
    repo_root: Path,
    errors: ValidationErrors,
) -> None:
    if not skills_root.is_dir():
        return
    resolved_skills_root = skills_root.resolve()
    for markdown_path in sorted(skills_root.rglob("*.md")):
        if markdown_path.is_symlink() or not markdown_path.is_file():
            continue
        try:
            text = markdown_path.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError) as exc:
            errors.add(
                relative_location(markdown_path, repo_root),
                f"Markdown could not be read ({exc})",
            )
            continue
        for destination in iter_markdown_destinations(text):
            validate_markdown_destination(
                markdown_path,
                destination,
                resolved_skills_root,
                repo_root,
                errors,
            )


def iter_markdown_destinations(text: str) -> Iterable[str]:
    fenced = False
    fence_marker = ""
    for line in text.splitlines():
        stripped = line.lstrip()
        if stripped.startswith("```") or stripped.startswith("~~~"):
            marker = stripped[:3]
            if not fenced:
                fenced = True
                fence_marker = marker
            elif marker == fence_marker:
                fenced = False
                fence_marker = ""
            continue
        if fenced:
            continue
        yield from iter_inline_markdown_destinations(line)
        reference_match = REFERENCE_LINK_PATTERN.match(line)
        if reference_match:
            yield reference_match.group("destination")


def iter_inline_markdown_destinations(line: str) -> Iterable[str]:
    """Yield inline link destinations while preserving balanced parentheses."""

    cursor = 0
    while True:
        marker = line.find("](", cursor)
        if marker < 0:
            return
        index = marker + 2
        while index < len(line) and line[index].isspace():
            index += 1
        if index >= len(line):
            return

        if line[index] == "<":
            closing = line.find(">", index + 1)
            if closing < 0:
                cursor = index + 1
                continue
            yield line[index : closing + 1]
            cursor = closing + 1
            continue

        start = index
        depth = 0
        while index < len(line):
            character = line[index]
            if character == "\\" and index + 1 < len(line):
                index += 2
                continue
            if character == "(":
                depth += 1
            elif character == ")":
                if depth == 0:
                    break
                depth -= 1
            elif character.isspace() and depth == 0:
                break
            index += 1
        if index > start:
            yield line[start:index]
        cursor = max(index + 1, marker + 2)


def validate_markdown_destination(
    markdown_path: Path,
    raw_destination: str,
    skills_root: Path,
    repo_root: Path,
    errors: ValidationErrors,
) -> None:
    destination = raw_destination.strip()
    if destination.startswith("<") and destination.endswith(">"):
        destination = destination[1:-1]
    if not destination or destination.startswith("#"):
        return
    try:
        parsed = urlsplit(destination)
    except ValueError as exc:
        errors.add(
            relative_location(markdown_path, repo_root),
            f"Markdown link has an invalid destination {raw_destination!r} ({exc})",
        )
        return
    if parsed.scheme or parsed.netloc:
        return
    if not parsed.path:
        return
    decoded_path = unquote(parsed.path)
    pure_path = PurePosixPath(decoded_path)
    if pure_path.is_absolute():
        errors.add(
            relative_location(markdown_path, repo_root),
            f"Markdown link must be relative, got {raw_destination!r}",
        )
        return
    candidate = resolve_posix_path(markdown_path.parent, decoded_path)
    if candidate is None or not is_within(candidate, skills_root):
        errors.add(
            relative_location(markdown_path, repo_root),
            f"Markdown link escapes bundled skills: {raw_destination!r}",
        )
        return
    if not candidate.exists():
        errors.add(
            relative_location(markdown_path, repo_root),
            f"Markdown link target does not exist: {raw_destination!r}",
        )


def validate_routing_cases(
    fixtures: Any,
    fixture_path: Path,
    expected_result: str,
    errors: ValidationErrors,
) -> None:
    if not isinstance(fixtures, dict):
        if fixtures is not None:
            errors.add(fixture_path, "routing fixture root must be a JSON object")
        return
    require_exact(fixtures, "schemaVersion", 1, fixture_path, errors)
    cases = fixtures.get("cases")
    if not isinstance(cases, list):
        errors.add(fixture_path, "cases must be an array")
        return

    case_ids: set[str] = set()
    covered_skills: set[str] = set()
    for index, case in enumerate(cases):
        location = f"cases[{index}]"
        if not isinstance(case, dict):
            errors.add(fixture_path, f"{location} must be an object")
            continue
        case_id = case.get("id")
        if not isinstance(case_id, str) or not CASE_ID_PATTERN.fullmatch(case_id):
            errors.add(fixture_path, f"{location}.id must be unique lower kebab-case")
        elif case_id in case_ids:
            errors.add(fixture_path, f"duplicate case id {case_id!r}")
        else:
            case_ids.add(case_id)

        skill_id = case.get("skill")
        if skill_id not in EXPECTED_SKILLS:
            errors.add(fixture_path, f"{location}.skill is not in the bundle catalog")
        else:
            covered_skills.add(skill_id)
        if case.get("expected") != expected_result:
            errors.add(fixture_path, f"{location}.expected must be {expected_result!r}")
        for field_name in ("prompt", "rationale"):
            value = case.get(field_name)
            if not isinstance(value, str) or not value.strip():
                errors.add(
                    fixture_path, f"{location}.{field_name} must be a non-empty string"
                )

    if covered_skills != set(EXPECTED_SKILLS):
        errors.add(
            fixture_path,
            f"routing fixtures must cover every bundled skill, missing {sorted(set(EXPECTED_SKILLS) - covered_skills)!r}",
        )


def validate_removed_names(
    repo_root: Path,
    plugin_root: Path,
    errors: ValidationErrors,
) -> None:
    active_paths: list[Path] = []
    if plugin_root.exists():
        active_paths.extend(path for path in plugin_root.rglob("*") if path.is_file())
    active_paths.extend(
        repo_root / relative_path
        for relative_path in (
            EXPECTED_CATALOG_REL,
            TRIGGER_CASES_REL,
            NON_TRIGGER_CASES_REL,
        )
    )
    for path in sorted(set(active_paths)):
        if not path.is_file() or path.is_symlink():
            continue
        try:
            content = path.read_bytes().lower()
        except OSError as exc:
            errors.add(
                relative_location(path, repo_root),
                f"could not scan removed names ({exc})",
            )
            continue
        for forbidden_name in FORBIDDEN_SKILLS:
            if forbidden_name.encode("utf-8") in content:
                errors.add(
                    relative_location(path, repo_root),
                    f"removed skill name {forbidden_name!r} remains in the active bundle",
                )


def validate_existing_relative_path(
    plugin_root: Path,
    value: Any,
    manifest_path: Path,
    field_name: str,
    errors: ValidationErrors,
    *,
    require_file: bool,
    required_parent: str | None = None,
    required_suffix: str | None = None,
) -> None:
    if not isinstance(value, str) or not value.startswith("./"):
        errors.add(
            manifest_path, f"{field_name} must be a relative path beginning with './'"
        )
        return
    relative_value = value[2:]
    pure_path = PurePosixPath(relative_value)
    if pure_path.is_absolute() or not pure_path.parts or ".." in pure_path.parts:
        errors.add(manifest_path, f"{field_name} contains an unsafe path {value!r}")
        return
    if required_parent is not None and pure_path.parts[0] != required_parent:
        errors.add(
            manifest_path, f"{field_name} must be stored under ./{required_parent}/"
        )
    if required_suffix is not None and pure_path.suffix.lower() != required_suffix:
        errors.add(manifest_path, f"{field_name} must end with {required_suffix}")
    candidate = resolve_posix_path(plugin_root, relative_value)
    if candidate is None or not is_within(candidate, plugin_root):
        errors.add(manifest_path, f"{field_name} escapes the plugin root")
    elif require_file and not candidate.is_file():
        errors.add(manifest_path, f"{field_name} points to a missing file {value!r}")


def require_nonempty_string(
    mapping: dict[str, Any],
    field_name: str,
    location: Path,
    errors: ValidationErrors,
    *,
    prefix: str = "",
) -> str | None:
    value = mapping.get(field_name)
    if not isinstance(value, str) or not value.strip():
        errors.add(location, f"{prefix}{field_name} must be a non-empty string")
        return None
    return value


def require_exact(
    mapping: dict[str, Any],
    field_name: str,
    expected: Any,
    location: Path,
    errors: ValidationErrors,
    prefix: str = "",
) -> None:
    value = mapping.get(field_name)
    if value != expected or isinstance(value, bool) != isinstance(expected, bool):
        errors.add(
            location, f"{prefix}{field_name} must be {expected!r}, got {value!r}"
        )


def validate_optional_https_url(
    mapping: dict[str, Any],
    field_name: str,
    location: Path,
    errors: ValidationErrors,
    *,
    prefix: str = "",
) -> None:
    value = mapping.get(field_name)
    if value is not None:
        validate_https_url(value, f"{prefix}{field_name}", location, errors)


def validate_https_url(
    value: Any,
    field_name: str,
    location: Path,
    errors: ValidationErrors,
) -> None:
    if not isinstance(value, str):
        errors.add(location, f"{field_name} must be an absolute HTTPS URL")
        return
    try:
        parsed = urlsplit(value)
    except ValueError:
        errors.add(location, f"{field_name} must be an absolute HTTPS URL")
        return
    if parsed.scheme != "https" or not parsed.netloc:
        errors.add(location, f"{field_name} must be an absolute HTTPS URL")


def resolve_posix_path(base: Path, value: str) -> Path | None:
    pure_path = PurePosixPath(value)
    if pure_path.is_absolute():
        return None
    return base.joinpath(*pure_path.parts).resolve()


def is_within(path: Path, root: Path) -> bool:
    try:
        path.resolve().relative_to(root.resolve())
    except ValueError:
        return False
    return True


def relative_location(path: Path, repo_root: Path) -> Path:
    try:
        return path.relative_to(repo_root)
    except ValueError:
        return path


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--repo-root",
        type=Path,
        default=Path(__file__).resolve().parents[1],
        help="repository root (defaults to the parent of scripts/)",
    )
    parser.add_argument(
        "--release-tag",
        help="require an exact vX.Y.Z tag-to-manifest version match",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    errors = validate_bundle(args.repo_root, args.release_tag)
    if errors:
        print(f"Bundle validation failed with {len(errors)} error(s):", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1
    print(
        "Bundle validation passed: "
        f"{len(EXPECTED_SOURCE_SKILLS)} sources, {len(EXPECTED_SKILLS)} skills, "
        "manifest and fixtures."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
