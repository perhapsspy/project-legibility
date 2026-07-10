from __future__ import annotations

import hashlib
import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "scripts"))

import validate_bundle as bundle  # noqa: E402


def write_json(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(value, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )


def read_json(path: Path) -> object:
    return json.loads(path.read_text(encoding="utf-8"))


def build_valid_repo(root: Path) -> None:
    """Build the smallest complete bundle accepted by the public contract."""

    plugin_root = root / bundle.PLUGIN_ROOT_REL
    skills_root = plugin_root / "skills"
    for fixture_rel in (
        bundle.EXPECTED_CATALOG_REL,
        bundle.FORBIDDEN_CATALOG_REL,
        bundle.TRIGGER_CASES_REL,
        bundle.NON_TRIGGER_CASES_REL,
    ):
        destination = root / fixture_rel
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(REPO_ROOT / fixture_rel, destination)

    write_json(
        root / bundle.MANIFEST_REL,
        {
            "name": bundle.PLUGIN_NAME,
            "version": "0.1.0",
            "description": "Keep project intent, structure, and context legible.",
            "author": {
                "name": "perhapsspy",
                "url": "https://github.com/perhapsspy",
            },
            "homepage": "https://github.com/perhapsspy/project-legibility#readme",
            "repository": "https://github.com/perhapsspy/project-legibility",
            "license": "MIT",
            "skills": "./skills/",
            "interface": {
                "displayName": "Project Legibility",
                "shortDescription": "Keep projects legible.",
                "longDescription": "Shape, build, verify, and resume project work.",
                "developerName": "perhapsspy",
                "category": "Developer Tools",
                "capabilities": ["Read", "Write"],
                "defaultPrompt": [
                    "Resume this project and implement the next verified change."
                ],
            },
        },
    )
    write_json(
        root / bundle.MARKETPLACE_REL,
        {
            "name": bundle.PLUGIN_NAME,
            "interface": {"displayName": "Project Legibility"},
            "plugins": [
                {
                    "name": bundle.PLUGIN_NAME,
                    "source": {
                        "source": "local",
                        "path": "./plugins/project-legibility",
                    },
                    "policy": {
                        "installation": "AVAILABLE",
                        "authentication": "ON_INSTALL",
                    },
                    "category": "Developer Tools",
                }
            ],
        },
    )

    for skill_id in bundle.EXPECTED_SKILLS:
        skill_dir = skills_root / skill_id
        skill_dir.mkdir(parents=True, exist_ok=True)
        companion_link = ""
        if skill_id == "project-context-migration":
            companion_link = (
                "\nRead [project-context](../project-context/SKILL.md) first.\n"
            )
        (skill_dir / "SKILL.md").write_text(
            "---\n"
            f"name: {skill_id}\n"
            f'description: "Contract fixture for {skill_id}."\n'
            "---\n\n"
            f"# {skill_id}\n"
            f"{companion_link}",
            encoding="utf-8",
        )

    sources = []
    for source_id, skill_ids in bundle.EXPECTED_SOURCE_SKILLS.items():
        skill_entries = []
        for skill_id in skill_ids:
            target_path = f"skills/{skill_id}"
            skill_entries.append(
                {
                    "id": skill_id,
                    "sourcePath": target_path,
                    "targetPath": target_path,
                    "integrity": bundle.compute_tree_integrity(
                        plugin_root / target_path
                    ),
                }
            )
        sources.append(
            {
                "id": source_id,
                "repository": f"{bundle.EXPECTED_REPOSITORIES[source_id]}.git",
                "commit": hashlib.sha1(source_id.encode("utf-8")).hexdigest(),
                "license": "MIT",
                "skills": skill_entries,
            }
        )
    write_json(
        plugin_root / "sources.lock.json", {"lockVersion": 1, "sources": sources}
    )
    (root / bundle.CHANGELOG_REL).write_text(
        "# Changelog\n\n## [0.1.0] - 2026-07-11\n",
        encoding="utf-8",
    )


class TreeIntegrityTests(unittest.TestCase):
    def test_integrity_is_stable_and_content_sensitive(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            (root / "nested").mkdir()
            (root / "b.txt").write_text("b", encoding="utf-8")
            (root / "nested" / "a.txt").write_text("a", encoding="utf-8")

            first = bundle.compute_tree_integrity(root)
            second = bundle.compute_tree_integrity(root)
            self.assertEqual(first, second)
            self.assertRegex(first, bundle.INTEGRITY_PATTERN)

            (root / "nested" / "a.txt").write_text("changed", encoding="utf-8")
            self.assertNotEqual(first, bundle.compute_tree_integrity(root))

    @unittest.skipIf(os.name == "nt", "executable-bit contract is POSIX-specific")
    def test_integrity_tracks_executable_bit(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / "tool.sh"
            path.write_text("#!/bin/sh\n", encoding="utf-8")
            path.chmod(0o644)
            regular = bundle.compute_tree_integrity(path.parent)
            path.chmod(0o755)
            self.assertNotEqual(regular, bundle.compute_tree_integrity(path.parent))


class BundleValidatorTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory()
        self.repo_root = Path(self.temporary.name)
        build_valid_repo(self.repo_root)

    def tearDown(self) -> None:
        self.temporary.cleanup()

    def errors(self, release_tag: str | None = None) -> list[str]:
        return bundle.validate_bundle(self.repo_root, release_tag)

    def assert_error_contains(self, fragment: str) -> None:
        errors = self.errors()
        self.assertTrue(
            any(fragment in error for error in errors),
            f"expected an error containing {fragment!r}, got {errors!r}",
        )

    def test_minimal_complete_bundle_passes(self) -> None:
        self.assertEqual([], self.errors())

    def test_strict_semver_contract(self) -> None:
        for version in ("0.1.0", "1.2.3-beta.1", "1.2.3+build.7"):
            with self.subTest(version=version):
                self.assertIsNotNone(bundle.SEMVER_PATTERN.fullmatch(version))
        for version in ("01.2.3", "1.02.3", "1.2", "v1.2.3", "1.2.3-01"):
            with self.subTest(version=version):
                self.assertIsNone(bundle.SEMVER_PATTERN.fullmatch(version))

    def test_manifest_prompt_limit_is_enforced(self) -> None:
        manifest_path = self.repo_root / bundle.MANIFEST_REL
        manifest = read_json(manifest_path)
        assert isinstance(manifest, dict)
        interface = manifest["interface"]
        assert isinstance(interface, dict)
        interface["defaultPrompt"] = ["one", "two", "three", "four"]
        write_json(manifest_path, manifest)
        self.assert_error_contains("between 1 and 3 prompts")

        interface["defaultPrompt"] = ["x" * 129]
        write_json(manifest_path, manifest)
        self.assert_error_contains("exceeds 128 characters")

    def test_manifest_asset_must_exist_inside_assets(self) -> None:
        manifest_path = self.repo_root / bundle.MANIFEST_REL
        manifest = read_json(manifest_path)
        assert isinstance(manifest, dict)
        interface = manifest["interface"]
        assert isinstance(interface, dict)
        interface["logo"] = "./assets/missing.svg"
        write_json(manifest_path, manifest)
        self.assert_error_contains("points to a missing file")

    def test_skills_only_manifest_rejects_runtime_components(self) -> None:
        manifest_path = self.repo_root / bundle.MANIFEST_REL
        manifest = read_json(manifest_path)
        assert isinstance(manifest, dict)
        manifest["mcpServers"] = {"unsafe": {"command": "run-me"}}
        manifest["apps"] = "./.app.json"
        write_json(manifest_path, manifest)
        errors = self.errors()
        self.assertTrue(any("must omit 'mcpServers'" in error for error in errors))
        self.assertTrue(any("must omit 'apps'" in error for error in errors))

    def test_marketplace_source_and_category_are_exact(self) -> None:
        marketplace_path = self.repo_root / bundle.MARKETPLACE_REL
        marketplace = read_json(marketplace_path)
        assert isinstance(marketplace, dict)
        entry = marketplace["plugins"][0]
        entry["source"]["path"] = "./"
        entry["category"] = "Productivity"
        write_json(marketplace_path, marketplace)
        errors = self.errors()
        self.assertTrue(any("source must be exactly" in error for error in errors))
        self.assertTrue(
            any("category must be 'Developer Tools'" in error for error in errors)
        )

    def test_expected_catalog_must_remain_exact(self) -> None:
        catalog_path = self.repo_root / bundle.EXPECTED_CATALOG_REL
        catalog = read_json(catalog_path)
        assert isinstance(catalog, dict)
        catalog["skills"].pop()
        write_json(catalog_path, catalog)
        self.assert_error_contains("sorted contract catalog")

    def test_routing_fixtures_require_known_skill_and_full_coverage(self) -> None:
        fixture_path = self.repo_root / bundle.TRIGGER_CASES_REL
        fixture = read_json(fixture_path)
        assert isinstance(fixture, dict)
        fixture["cases"][0]["skill"] = "unknown-skill"
        write_json(fixture_path, fixture)
        errors = self.errors()
        self.assertTrue(any("not in the bundle catalog" in error for error in errors))
        self.assertTrue(
            any("must cover every bundled skill" in error for error in errors)
        )

    def test_removed_name_is_rejected_in_active_bundle(self) -> None:
        skill_path = (
            self.repo_root
            / bundle.PLUGIN_ROOT_REL
            / "skills"
            / "source-owner-audit"
            / "SKILL.md"
        )
        skill_path.write_text(
            skill_path.read_text(encoding="utf-8") + "\nLegacy: work-board\n",
            encoding="utf-8",
        )
        self.assert_error_contains("removed skill name 'work-board'")

    def test_historical_docs_are_outside_removed_name_scan(self) -> None:
        history = self.repo_root / "docs" / "history.md"
        history.parent.mkdir(parents=True)
        history.write_text(
            "Historical names: work-board, justified-change, structure-first-docs.\n",
            encoding="utf-8",
        )
        self.assertEqual([], self.errors())

    def test_frontmatter_name_must_match_directory(self) -> None:
        skill_path = (
            self.repo_root
            / bundle.PLUGIN_ROOT_REL
            / "skills"
            / "tighten-docs"
            / "SKILL.md"
        )
        skill_path.write_text(
            skill_path.read_text(encoding="utf-8").replace(
                "name: tighten-docs", "name: different-name"
            ),
            encoding="utf-8",
        )
        self.assert_error_contains("frontmatter name must match directory")

    def test_frontmatter_description_must_be_text(self) -> None:
        skill_path = (
            self.repo_root
            / bundle.PLUGIN_ROOT_REL
            / "skills"
            / "tighten-docs"
            / "SKILL.md"
        )
        skill_path.write_text(
            skill_path.read_text(encoding="utf-8").replace(
                'description: "Contract fixture for tighten-docs."', "description: null"
            ),
            encoding="utf-8",
        )
        self.assert_error_contains("frontmatter field 'description' must be text")

    def test_frontmatter_scalar_types_and_trailing_comment(self) -> None:
        skill_path = (
            self.repo_root
            / bundle.PLUGIN_ROOT_REL
            / "skills"
            / "tighten-docs"
            / "SKILL.md"
        )
        original = skill_path.read_text(encoding="utf-8")
        for invalid in ("123", "[]", "2026-07-11"):
            with self.subTest(value=invalid):
                skill_path.write_text(
                    original.replace(
                        'description: "Contract fixture for tighten-docs."',
                        f"description: {invalid}",
                    ),
                    encoding="utf-8",
                )
                self.assert_error_contains(
                    "frontmatter field 'description' must be text"
                )
        skill_path.write_text(
            original.replace(
                'description: "Contract fixture for tighten-docs."',
                'description: "Contract fixture for tighten-docs." # current description',
            ),
            encoding="utf-8",
        )
        lock_path = self.repo_root / bundle.LOCK_REL
        lock = read_json(lock_path)
        assert isinstance(lock, dict)
        tighten_source = next(
            item for item in lock["sources"] if item["id"] == "tighten-docs"
        )
        tighten_source["skills"][0]["integrity"] = bundle.compute_tree_integrity(
            skill_path.parent
        )
        write_json(lock_path, lock)
        self.assertEqual([], self.errors())

    def test_lock_rejects_unknown_schema_fields(self) -> None:
        lock_path = self.repo_root / bundle.LOCK_REL
        lock = read_json(lock_path)
        assert isinstance(lock, dict)
        lock["generatedAt"] = "now"
        write_json(lock_path, lock)
        self.assert_error_contains("lock root may contain only")

    def test_snapshot_edit_breaks_lock_integrity(self) -> None:
        skill_path = (
            self.repo_root
            / bundle.PLUGIN_ROOT_REL
            / "skills"
            / "structure-first"
            / "SKILL.md"
        )
        skill_path.write_text(
            skill_path.read_text(encoding="utf-8") + "\nDrift.\n", encoding="utf-8"
        )
        self.assert_error_contains("integrity mismatch")

    def test_missing_and_escaping_markdown_links_are_rejected(self) -> None:
        skill_path = (
            self.repo_root
            / bundle.PLUGIN_ROOT_REL
            / "skills"
            / "project-context-migration"
            / "SKILL.md"
        )
        skill_path.write_text(
            skill_path.read_text(encoding="utf-8")
            + "\n[missing](../project-context/MISSING.md)\n"
            + "[escape](../../../README.md)\n",
            encoding="utf-8",
        )
        errors = self.errors()
        self.assertTrue(any("target does not exist" in error for error in errors))
        self.assertTrue(any("escapes bundled skills" in error for error in errors))

    def test_malformed_markdown_url_is_reported_without_crashing(self) -> None:
        skill_path = (
            self.repo_root
            / bundle.PLUGIN_ROOT_REL
            / "skills"
            / "project-context"
            / "SKILL.md"
        )
        skill_path.write_text(
            skill_path.read_text(encoding="utf-8") + "\n[broken](https://[)\n",
            encoding="utf-8",
        )
        self.assert_error_contains("invalid destination")

    def test_markdown_link_with_parentheses_is_resolved_as_one_destination(
        self,
    ) -> None:
        skill_dir = (
            self.repo_root / bundle.PLUGIN_ROOT_REL / "skills" / "project-context"
        )
        target = skill_dir / "reference(with-parentheses).md"
        target.write_text("# Reference\n", encoding="utf-8")
        skill_path = skill_dir / "SKILL.md"
        skill_path.write_text(
            skill_path.read_text(encoding="utf-8")
            + "\n[reference](reference(with-parentheses).md)\n",
            encoding="utf-8",
        )
        lock_path = self.repo_root / bundle.LOCK_REL
        lock = read_json(lock_path)
        assert isinstance(lock, dict)
        project_source = next(
            item for item in lock["sources"] if item["id"] == "project-context"
        )
        project_skill = next(
            item for item in project_source["skills"] if item["id"] == "project-context"
        )
        project_skill["integrity"] = bundle.compute_tree_integrity(skill_dir)
        write_json(lock_path, lock)
        self.assertEqual([], self.errors())

    @unittest.skipIf(os.name == "nt", "symlink contract is POSIX-specific")
    def test_symlink_is_rejected(self) -> None:
        skill_dir = (
            self.repo_root / bundle.PLUGIN_ROOT_REL / "skills" / "agents-md-editor"
        )
        (skill_dir / "alias.md").symlink_to("SKILL.md")
        self.assert_error_contains("symlinks are not allowed")

    @unittest.skipIf(os.name == "nt", "symlink contract is POSIX-specific")
    def test_plugin_root_symlink_is_rejected(self) -> None:
        plugin_root = self.repo_root / bundle.PLUGIN_ROOT_REL
        actual_root = self.repo_root / "actual-plugin"
        plugin_root.rename(actual_root)
        plugin_root.symlink_to(actual_root, target_is_directory=True)
        self.assert_error_contains("plugin root must not be a symlink")

    def test_companion_skills_must_share_project_context_source(self) -> None:
        lock_path = self.repo_root / bundle.LOCK_REL
        lock = read_json(lock_path)
        assert isinstance(lock, dict)
        project_source = next(
            item for item in lock["sources"] if item["id"] == "project-context"
        )
        migration = project_source["skills"].pop()
        lock["sources"][0]["skills"].append(migration)
        write_json(lock_path, lock)
        errors = self.errors()
        self.assertTrue(
            any(
                "source 'project-context' must own exactly" in error for error in errors
            )
        )

    def test_release_tag_must_match_manifest_without_local_suffix(self) -> None:
        self.assertEqual([], self.errors("v0.1.0"))
        mismatch = bundle.validate_bundle(self.repo_root, "v0.2.0")
        self.assertTrue(
            any("does not match release tag" in error for error in mismatch)
        )

        manifest_path = self.repo_root / bundle.MANIFEST_REL
        manifest = read_json(manifest_path)
        assert isinstance(manifest, dict)
        manifest["version"] = "0.1.0+codex.local-20260711"
        write_json(manifest_path, manifest)
        local = bundle.validate_bundle(self.repo_root, "v0.1.0")
        self.assertTrue(
            any("must not contain +codex.local" in error for error in local)
        )

    def test_release_tag_requires_matching_changelog_entry(self) -> None:
        changelog = self.repo_root / bundle.CHANGELOG_REL
        changelog.write_text("# Changelog\n\n## [Unreleased]\n", encoding="utf-8")
        errors = self.errors("v0.1.0")
        self.assertTrue(
            any("missing release heading for [0.1.0]" in error for error in errors)
        )

    def test_cli_aggregates_errors_and_returns_one(self) -> None:
        (self.repo_root / bundle.MARKETPLACE_REL).unlink()
        result = subprocess.run(
            [
                sys.executable,
                str(REPO_ROOT / "scripts" / "validate_bundle.py"),
                "--repo-root",
                str(self.repo_root),
            ],
            check=False,
            capture_output=True,
            text=True,
        )
        self.assertEqual(1, result.returncode)
        self.assertIn("Bundle validation failed", result.stderr)
        self.assertIn("required JSON file is missing", result.stderr)


class RepositorySmokeTests(unittest.TestCase):
    def test_committed_repository_bundle_passes(self) -> None:
        self.assertEqual([], bundle.validate_bundle(REPO_ROOT))

    def test_sync_offline_check_passes(self) -> None:
        result = subprocess.run(
            [sys.executable, "scripts/sync_skills.py", "check", "--offline"],
            cwd=REPO_ROOT,
            check=False,
            capture_output=True,
            text=True,
        )
        self.assertEqual(0, result.returncode, result.stderr or result.stdout)


if __name__ == "__main__":
    unittest.main()
