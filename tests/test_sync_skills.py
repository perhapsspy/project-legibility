from __future__ import annotations

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

import sync_skills as sync  # noqa: E402
import validate_bundle as bundle  # noqa: E402


@unittest.skipUnless(shutil.which("git"), "git is required")
class GitArchiveTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary.name)
        self.repo = self.root / "source"
        self.repo.mkdir()
        self.git("init", "-b", "main")
        self.git("config", "user.name", "Project Legibility Tests")
        self.git("config", "user.email", "tests@example.invalid")

        skill = self.repo / "skills" / "example"
        (skill / "scripts").mkdir(parents=True)
        (skill / "SKILL.md").write_text(
            "---\nname: example\ndescription: Example fixture.\n---\n",
            encoding="utf-8",
        )
        tool = skill / "scripts" / "tool.py"
        tool.write_text("#!/usr/bin/env python3\nprint('ok')\n", encoding="utf-8")
        tool.chmod(0o755)
        self.git("add", ".")
        self.git("commit", "-m", "Add example skill")

    def tearDown(self) -> None:
        self.temporary.cleanup()

    def git(self, *args: str) -> str:
        result = subprocess.run(
            ["git", "-C", str(self.repo), *args],
            check=True,
            capture_output=True,
            text=True,
        )
        return result.stdout.strip()

    def test_export_preserves_content_and_executable_contract(self) -> None:
        destination = self.root / "exported"
        sync.export_skill(
            self.repo,
            self.git("rev-parse", "HEAD"),
            "skills/example",
            destination,
        )

        self.assertTrue((destination / "SKILL.md").is_file())
        self.assertTrue((destination / "scripts" / "tool.py").stat().st_mode & 0o100)
        self.assertEqual(
            sync.compute_tree_integrity(destination),
            bundle.compute_tree_integrity(destination),
        )

    @unittest.skipIf(os.name == "nt", "symlink archive contract is POSIX-specific")
    def test_export_rejects_symlink(self) -> None:
        link = self.repo / "skills" / "example" / "alias.md"
        link.symlink_to("SKILL.md")
        self.git("add", ".")
        self.git("commit", "-m", "Add unsafe symlink")

        with self.assertRaisesRegex(sync.SyncError, "symlink and hardlink"):
            sync.export_skill(
                self.repo,
                self.git("rev-parse", "HEAD"),
                "skills/example",
                self.root / "rejected",
            )


class SyncContractTests(unittest.TestCase):
    def test_lock_shape_rejects_unknown_fields(self) -> None:
        lock = json.loads(
            (REPO_ROOT / "plugins/project-legibility/sources.lock.json").read_text(
                encoding="utf-8"
            )
        )
        lock["unexpected"] = True
        with self.assertRaisesRegex(sync.SyncError, r"unknown=\['unexpected'\]"):
            sync.validate_lock_shape(lock)

    def test_compare_trees_detects_content_and_mode_drift(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            expected = root / "expected"
            actual = root / "actual"
            expected.mkdir()
            actual.mkdir()
            (expected / "file.txt").write_text("same", encoding="utf-8")
            (actual / "file.txt").write_text("same", encoding="utf-8")
            sync.compare_trees(expected, actual)

            (actual / "file.txt").write_text("different", encoding="utf-8")
            with self.assertRaisesRegex(sync.SyncError, "differs from canonical"):
                sync.compare_trees(expected, actual)

            (actual / "file.txt").write_text("same", encoding="utf-8")
            if os.name != "nt":
                (actual / "file.txt").chmod(0o755)
                with self.assertRaisesRegex(sync.SyncError, "differs from canonical"):
                    sync.compare_trees(expected, actual)


if __name__ == "__main__":
    unittest.main()
