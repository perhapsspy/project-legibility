from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import release  # noqa: E402


class FakeRunner:
    def __init__(self, responses=None):
        self.calls = []
        self.responses = responses or {}

    def run(self, args, *, cwd=None, check=True):
        command = tuple(str(x) for x in args)
        self.calls.append((command, Path(cwd) if cwd else None, check))
        value = self.responses.get(" ".join(command), "")
        code = 0
        if isinstance(value, list):
            value = value.pop(0) if value else ""
        if isinstance(value, tuple):
            value, code = value
        if code and check:
            raise release.ReleaseError("fixture failure")
        return release.CommandResult(value, code)


class ReleaseTests(unittest.TestCase):
    def test_help_and_version(self):
        args = release.parse_args(["publish", "--version", "0.8.1", "--catalog-root", "/tmp"])
        self.assertEqual("publish", args.command)
        with self.assertRaises(release.ReleaseError):
            release.validate_version("v0.8.1")

    def test_catalog_preflight_happens_before_irreversible_publication(self):
        events = []
        head = "a" * 40
        catalog = Path("/tmp/catalog").resolve()
        orch = release.ReleaseOrchestrator(runner=FakeRunner())
        orch._project_preflight = lambda version: head
        orch._catalog_preflight = lambda root: events.append("catalog-preflight") or catalog
        orch._tag_commit = lambda tag: None
        orch._sync_project_main = lambda *args, **kwargs: events.append("project-main")
        orch._publish_tag = lambda *args: events.append("tag")
        orch._publish_catalog_prepared = lambda *args: events.append("catalog")
        orch.publish("0.8.2", catalog)
        self.assertEqual(
            ["catalog-preflight", "project-main", "tag", "catalog"], events
        )

    def test_dirty_or_wrong_branch_is_rejected(self):
        runner = FakeRunner({"git branch --show-current": "feature"})
        with self.assertRaisesRegex(release.ReleaseError, "main"):
            release.ReleaseOrchestrator(runner=runner)._project_preflight("0.8.1")
        runner = FakeRunner({"git branch --show-current": "main", "git status --porcelain": " M file"})
        with self.assertRaisesRegex(release.ReleaseError, "clean"):
            release.ReleaseOrchestrator(runner=runner)._project_preflight("0.8.1")

    def test_conflicting_tag_is_hard_failure(self):
        runner = FakeRunner({"git ls-remote origin refs/tags/v0.8.1 refs/tags/v0.8.1^{}": "b" * 40 + "\trefs/tags/v0.8.1\n"})
        orch = release.ReleaseOrchestrator(runner=runner)
        orch._wait_ci = lambda *args: None
        with self.assertRaisesRegex(release.ReleaseError, "already points"):
            orch._publish_tag("0.8.1", "a" * 40)

    def test_wait_ci_requires_exact_sha(self):
        head = "a" * 40
        key = f"gh run list --workflow ci.yml --commit {head} --json headSha,status,conclusion,databaseId --limit 20"
        runner = FakeRunner({key: json.dumps([{"headSha": "b" * 40, "conclusion": "success"}, {"headSha": head, "conclusion": "success"}])})
        release.ReleaseOrchestrator(runner=runner, ci_timeout=0, sleeper=lambda _: None)._wait_ci("ci.yml", head)

    def test_waiters_prefer_success_over_older_failure(self):
        head = "a" * 40
        ci_key = f"gh run list --workflow ci.yml --commit {head} --json headSha,status,conclusion,databaseId --limit 20"
        release_key = "gh run list --workflow release.yml --json headSha,status,conclusion --limit 20"
        runner = FakeRunner({ci_key: json.dumps([{"headSha": head, "conclusion": "failure"}, {"headSha": head, "conclusion": "success"}]), release_key: json.dumps([{"headSha": head, "conclusion": "failure"}, {"headSha": head, "conclusion": "success"}]), "gh release view v0.8.1": ""})
        orch = release.ReleaseOrchestrator(runner=runner, ci_timeout=0, sleeper=lambda _: None)
        orch._wait_ci("ci.yml", head)
        orch._wait_release("v0.8.1", head)

    def test_waiters_keep_active_run_ahead_of_terminal_failure(self):
        head = "a" * 40
        ci_key = f"gh run list --workflow ci.yml --commit {head} --json headSha,status,conclusion,databaseId --limit 20"
        release_key = "gh run list --workflow release.yml --json headSha,status,conclusion --limit 20"
        active = [{"headSha": head, "status": "in_progress", "conclusion": None}, {"headSha": head, "status": "completed", "conclusion": "failure"}]
        success = [{"headSha": head, "status": "completed", "conclusion": "success"}]
        runner = FakeRunner({ci_key: [json.dumps(active), json.dumps(success)], release_key: [json.dumps(active), json.dumps(success)], "gh release view v0.8.1": [('', 1), ('', 0)]})
        orch = release.ReleaseOrchestrator(runner=runner, ci_timeout=1, ci_poll_interval=0, sleeper=lambda _: None)
        orch._wait_ci("ci.yml", head)
        orch._wait_release("v0.8.1", head)

    def test_correct_remote_tag_still_requires_ci_and_release(self):
        head = "a" * 40
        runner = FakeRunner({"git ls-remote origin refs/tags/v0.8.1 refs/tags/v0.8.1^{}": head + "\trefs/tags/v0.8.1\n"})
        events = []
        orch = release.ReleaseOrchestrator(runner=runner)
        orch._wait_ci = lambda *args: events.append("ci")
        orch._wait_release = lambda *args: events.append("release")
        orch._publish_tag("0.8.1", head)
        self.assertEqual(["ci", "release"], events)

    def test_local_tag_is_reused_after_push_failure(self):
        head = "a" * 40
        key = "git rev-list -n 1 v0.8.1"
        runner = FakeRunner({key: head, "git push origin v0.8.1": ("", 1)})
        orch = release.ReleaseOrchestrator(runner=runner)
        orch._wait_ci = lambda *args: None
        with self.assertRaises(release.ReleaseError):
            orch._publish_tag("0.8.1", head)
        runner.responses["git push origin v0.8.1"] = ""
        orch._wait_release = lambda *args: None
        orch._publish_tag("0.8.1", head)
        tag_creates = [call for call, _, _ in runner.calls if call[:2] == ("git", "tag")]
        self.assertEqual([], tag_creates)

    def test_catalog_patch_only_changes_target_and_is_idempotent(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            path = root / ".agents/plugins/marketplace.json"
            path.parent.mkdir(parents=True)
            path.write_text(json.dumps({"plugins": [{"name": "project-legibility", "source": {"sha": "old"}}, {"name": "other", "source": {"sha": "keep"}}]}, indent=2) + "\n")
            runner = FakeRunner({"git branch --show-current": "main", "git status --porcelain": "", "git pull --ff-only origin main": "", "git diff --name-only": str(release.MARKETPLACE), "git rev-parse HEAD": "c" * 40})
            orch = release.ReleaseOrchestrator(runner=runner)
            orch._verify_repo_identity = lambda *args: None
            waits = []
            orch._wait_ci = lambda *args, **kwargs: waits.append((args, kwargs))
            orch._publish_catalog(root, "a" * 40)
            data = json.loads(path.read_text())
            self.assertEqual("a" * 40, data["plugins"][0]["source"]["sha"])
            self.assertEqual("keep", data["plugins"][1]["source"]["sha"])
            before = len([c for c in runner.calls if c[0][:2] == ("git", "commit")])
            orch._publish_catalog(root, "a" * 40)
            after = len([c for c in runner.calls if c[0][:2] == ("git", "commit")])
            self.assertEqual(before, after)
            self.assertEqual(root.resolve(), waits[-1][1]["repo"])

    def test_catalog_validation_failure_restores_worktree(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            path = root / ".agents/plugins/marketplace.json"
            path.parent.mkdir(parents=True)
            path.write_text(json.dumps({"plugins": [{"name": "project-legibility", "source": {"sha": "old"}}]}, indent=2) + "\n")
            validator = f"{sys.executable} scripts/validate_marketplace.py --verify-remote"
            runner = FakeRunner({"git branch --show-current": "main", "git status --porcelain": "", "git pull --ff-only origin main": "", "git diff --name-only": str(release.MARKETPLACE), validator: ("", 1)})
            orch = release.ReleaseOrchestrator(runner=runner)
            orch._verify_repo_identity = lambda *args: None
            with self.assertRaises(release.ReleaseError):
                orch._publish_catalog(root, "a" * 40)
            self.assertTrue(any(call[:4] == ("git", "restore", "--staged", "--worktree") for call, _, _ in runner.calls))

    def test_already_pinned_local_commit_is_pushed_after_previous_push_failure(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            path = root / ".agents/plugins/marketplace.json"
            path.parent.mkdir(parents=True)
            path.write_text(json.dumps({"plugins": [{"name": "project-legibility", "source": {"sha": "old"}}]}, indent=2) + "\n")
            push_key = "git push origin main"
            runner = FakeRunner({"git branch --show-current": "main", "git status --porcelain": "", "git pull --ff-only origin main": "", "git rev-parse HEAD": "c" * 40, "git diff --name-only": str(release.MARKETPLACE), "git ls-remote origin refs/heads/main": "b" * 40 + "\trefs/heads/main", push_key: [("", 1), ""]})
            orch = release.ReleaseOrchestrator(runner=runner)
            orch._verify_repo_identity = lambda *args: None
            orch._wait_ci = lambda *args, **kwargs: None
            with self.assertRaises(release.ReleaseError):
                orch._publish_catalog(root, "a" * 40)
            orch._publish_catalog(root, "a" * 40)
            pushes = [call for call, _, _ in runner.calls if call[:3] == ("git", "push", "origin")]
            self.assertEqual(2, len(pushes))

    def test_origin_path_is_checked_without_ssh_config_for_github(self):
        runner = FakeRunner({"git remote get-url origin": "git@github.com:perhapsspy/project-legibility.git", "git remote get-url --push origin": "git@github.com:perhapsspy/project-legibility.git", "gh repo view --json nameWithOwner --jq .nameWithOwner": "perhapsspy/project-legibility"})
        release.ReleaseOrchestrator(runner=runner)._verify_repo_identity(Path("/tmp"), "perhapsspy/project-legibility")
        self.assertFalse(any(c[0][0] == "ssh" for c in runner.calls))

    def test_origin_ssh_alias_must_resolve_to_github(self):
        base = {"git remote get-url origin": "git@github-perhapsspy:perhapsspy/project-legibility.git", "git remote get-url --push origin": "git@github-perhapsspy:perhapsspy/project-legibility.git", "gh repo view --json nameWithOwner --jq .nameWithOwner": "perhapsspy/project-legibility"}
        runner = FakeRunner({**base, "ssh -G github-perhapsspy": "hostname github.com\n"})
        release.ReleaseOrchestrator(runner=runner)._verify_repo_identity(Path("/tmp"), "perhapsspy/project-legibility")
        runner = FakeRunner({**base, "ssh -G github-perhapsspy": "hostname example.com\n"})
        with self.assertRaisesRegex(release.ReleaseError, "origin fetch host"):
            release.ReleaseOrchestrator(runner=runner)._verify_repo_identity(Path("/tmp"), "perhapsspy/project-legibility")

    def test_new_release_rejects_stale_local_main_but_resume_allows_it(self):
        head = "a" * 40
        remote = "b" * 40
        responses = {
            "git ls-remote origin refs/heads/main": remote + "\trefs/heads/main\n",
            "git fetch origin main": "",
            f"git merge-base --is-ancestor {head} origin/main": "",
        }
        orch = release.ReleaseOrchestrator(runner=FakeRunner(responses))
        with self.assertRaisesRegex(release.ReleaseError, "ahead of local HEAD"):
            orch._sync_project_main(head)
        orch._sync_project_main(head, allow_remote_ahead=True)

    def test_origin_push_target_must_match_repository(self):
        runner = FakeRunner({"git remote get-url origin": "git@github.com:perhapsspy/project-legibility.git", "git remote get-url --push origin": "git@github.com:someone-else/project-legibility.git"})
        with self.assertRaisesRegex(release.ReleaseError, "origin push path"):
            release.ReleaseOrchestrator(runner=runner)._verify_repo_identity(Path("/tmp"), "perhapsspy/project-legibility")


if __name__ == "__main__":
    unittest.main()
