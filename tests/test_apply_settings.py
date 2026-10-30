import json
import os
from pathlib import Path
import runpy
import subprocess
import sys
import tempfile
import unittest


SCRIPT = Path(__file__).resolve().parents[1] / "scripts/apply-settings"
MERGE = runpy.run_path(str(SCRIPT))["merge"]


class ApplySettingsTests(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.root = Path(self.directory.name)
        self.claude = self.root / "claude"
        self.codex = self.root / "codex"

    def run_script(self, *args):
        return subprocess.run(
            [sys.executable, str(SCRIPT), *args],
            env={**os.environ, "CLAUDE_CONFIG_DIR": str(self.claude), "CODEX_HOME": str(self.codex)},
            text=True, capture_output=True,
        )

    def existing_files(self):
        self.claude.mkdir()
        self.codex.mkdir()
        self.settings = self.claude / "settings.json"
        self.config = self.codex / "config.toml"
        self.settings.write_text('{"local": {"token": "private-value"}, "outputStyle": "Other"}\n')
        self.config.write_text('# Local settings\nmodel = "local-model"\n\n[features]\ndefault_mode_request_user_input = false # Keep this comment\nother = true\n')
        self.config.chmod(0o640)

    def test_merge_preserves_unrelated_keys_and_replaces_arrays(self):
        target = {"nested": {"local": 7, "shared": False}, "items": [1, 2], "number": 1}
        MERGE(target, {"nested": {"shared": True}, "items": [3], "number": True})
        self.assertEqual(target, {"nested": {"local": 7, "shared": True}, "items": [3], "number": True})
        self.assertIs(target["number"], True)

    def test_dry_run_does_not_create_directories(self):
        result = self.run_script("--dry-run")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertFalse(self.claude.exists())
        self.assertFalse(self.codex.exists())

    def test_merge_backups_comments_and_repeat_run(self):
        self.existing_files()
        original = self.config.read_bytes()
        dry = self.run_script("--dry-run")
        self.assertEqual(dry.returncode, 0, dry.stderr)
        self.assertNotIn("private-value", dry.stdout)
        self.assertEqual(self.config.read_bytes(), original)
        self.assertFalse(list(self.root.rglob("*.backup-*")))
        result = self.run_script()
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(json.loads(self.settings.read_text())["local"], {"token": "private-value"})
        self.assertIn('default_mode_request_user_input = true # Keep this comment', self.config.read_text())
        self.assertIn('model = "local-model"', self.config.read_text())
        self.assertIn('other = true', self.config.read_text())
        self.assertEqual(self.config.stat().st_mode & 0o777, 0o640)
        backup = list(self.codex.glob("*.backup-*"))
        self.assertEqual(len(backup), 1)
        self.assertEqual(backup[0].read_bytes(), original)
        self.assertEqual(backup[0].stat().st_mode & 0o777, 0o600)
        before = {p: (p.read_bytes(), p.stat().st_mtime_ns) for p in self.root.rglob("*") if p.is_file()}
        result = self.run_script()
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stdout.count("Unchanged:"), 3)
        self.assertEqual(before, {p: (p.read_bytes(), p.stat().st_mtime_ns) for p in self.root.rglob("*") if p.is_file()})

    def test_invalid_toml_prevents_all_writes(self):
        self.existing_files()
        self.config.write_text("[invalid\n")
        original = self.settings.read_bytes()
        result = self.run_script()
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(self.settings.read_bytes(), original)
        self.assertFalse(list(self.root.rglob("*.backup-*")))

    def test_invalid_json_is_rejected(self):
        self.existing_files()
        for text in ['[]', '{"a": 1, "a": 2}', '{"a": NaN}', '{']:
            with self.subTest(text=text):
                self.settings.write_text(text)
                self.assertNotEqual(self.run_script().returncode, 0)
                self.assertEqual(self.settings.read_text(), text)

    def test_existing_symlink_is_preserved(self):
        self.existing_files()
        actual = self.root / "actual.toml"
        self.config.rename(actual)
        self.config.symlink_to(actual)
        result = self.run_script()
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertTrue(self.config.is_symlink())
        self.assertIn('default_mode_request_user_input = true', actual.read_text())


if __name__ == "__main__":
    unittest.main()
