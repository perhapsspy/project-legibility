from __future__ import annotations

import copy
import json
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import sync_plugin_metadata as metadata


class PluginMetadataTests(unittest.TestCase):
    def setUp(self):
        self.portable = json.loads((ROOT / "plugins/project-legibility/plugin.json").read_text())

    def test_client_projections_share_identity_and_keep_host_fields_separate(self):
        manifests = metadata.client_manifests(self.portable)
        codex = manifests[metadata.CODEX_PATH]
        claude = manifests[metadata.CLAUDE_PATH]
        for field in metadata.PORTABLE_FIELDS:
            self.assertEqual(codex[field], claude[field])
        self.assertNotIn("extensions", claude)
        self.assertNotIn("interface", claude)
        self.assertNotIn("skills", claude)
        self.assertEqual("./skills/", codex["skills"])
        claude["keywords"].append("changed")
        self.assertNotIn("changed", self.portable["keywords"])

    def test_version_update_requires_regeneration_of_both_clients(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "plugin.json").write_text(json.dumps(self.portable))
            self.assertEqual([], metadata.sync_metadata(root, write=True))
            self.portable["version"] = "0.99.0"
            (root / "plugin.json").write_text(json.dumps(self.portable))
            self.assertEqual(2, len(metadata.sync_metadata(root)))
            metadata.sync_metadata(root, write=True)
            self.assertEqual([], metadata.sync_metadata(root))
            for path in [metadata.CODEX_PATH, metadata.CLAUDE_PATH]:
                self.assertEqual("0.99.0", json.loads((root / path).read_text())["version"])

    def test_unreviewed_components_cannot_enter_native_manifests(self):
        for change in [
            lambda p: p.update(hooks="./hooks/hooks.json"),
            lambda p: p["extensions"]["com.openai"].update(apps="./.app.json"),
            lambda p: p.update(extensions=[]),
        ]:
            with self.subTest(change=change):
                portable = copy.deepcopy(self.portable)
                change(portable)
                with self.assertRaises(ValueError):
                    metadata.client_manifests(portable)

    def test_missing_or_malformed_native_manifest_is_reported(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "plugin.json").write_text(json.dumps(self.portable))
            metadata.sync_metadata(root, write=True)
            (root / metadata.CLAUDE_PATH).write_text("{")
            self.assertTrue(metadata.sync_metadata(root))
            (root / metadata.CLAUDE_PATH).unlink()
            self.assertTrue(metadata.sync_metadata(root))


if __name__ == "__main__":
    unittest.main()
