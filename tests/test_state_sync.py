"""Offline tests for scripts/state_sync.py using throwaway git repositories (a bare repo
plays the remote). No network, no Gemini key."""

from __future__ import annotations

import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

import state_sync  # noqa: E402

STORE = "fileSearchStores/teststore-abc"
IDENTITY = {"GIT_AUTHOR_NAME": "t", "GIT_AUTHOR_EMAIL": "t@example.invalid",
            "GIT_COMMITTER_NAME": "t", "GIT_COMMITTER_EMAIL": "t@example.invalid"}


def run_git(cwd: Path, *args: str) -> str:
    return subprocess.run(["git", *args], cwd=cwd, check=True, capture_output=True, text=True).stdout.strip()


def write_state(root: Path, names=("a.md", "b.md")) -> None:
    (root / "data/articles").mkdir(parents=True, exist_ok=True)
    (root / "state").mkdir(parents=True, exist_ok=True)
    (root / "logs").mkdir(parents=True, exist_ok=True)
    articles = {}
    for i, name in enumerate(names):
        (root / "data/articles" / name).write_bytes(f"# Article {i}\r\nbody\n".encode())
        articles[str(i)] = {"markdown_path": f"data/articles/{name}", "store_name": STORE}
    (root / "state/gemini-store.json").write_text(json.dumps({"store_name": STORE}))
    (root / "state/ingestion-manifest.json").write_text(json.dumps({"version": 1, "articles": articles}))
    (root / "state/article-files.json").write_text(json.dumps({"version": 1, "files": {}}))
    (root / "logs/last-run.json").write_text(json.dumps({"status": "success"}))


class StateSyncTests(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, self.tmp, ignore_errors=True)
        env = mock.patch.dict(os.environ, IDENTITY)
        env.start()
        self.addCleanup(env.stop)
        os.environ.pop("API_KEY", None)
        os.environ.pop("GEMINI_API_KEY", None)
        self.remote = self.tmp / "remote.git"
        run_git(self.tmp, "init", "--bare", "-q", str(self.remote))
        self.repo = self.tmp / "repo"
        run_git(self.tmp, "init", "-q", str(self.repo))
        run_git(self.repo, "remote", "add", "origin", str(self.remote))

    def bootstrap_and_push(self) -> str:
        write_state(self.repo)
        info = state_sync.bootstrap(self.repo, self.repo, "pipeline-state", "origin", "seed")
        run_git(self.repo, "push", "-q", "origin", "pipeline-state")
        return info["commit"]

    def fresh_runner(self) -> Path:
        """A new clone with the state branch fetched the way the workflow does it."""
        clone = self.tmp / f"runner{len(list(self.tmp.iterdir()))}"
        run_git(self.tmp, "clone", "-q", str(self.remote), str(clone))
        run_git(clone, "fetch", "-q", "--no-tags", "--depth=1", "origin",
                "+refs/heads/pipeline-state:refs/remotes/origin/pipeline-state")
        return clone

    def tree(self, ref: str) -> list[str]:
        return run_git(self.repo, "ls-tree", "-r", "--name-only", ref).splitlines()

    def test_bootstrap_includes_only_allowlisted_files(self):
        write_state(self.repo)
        (self.repo / ".env").write_text("API_KEY=secret-value-123\n")
        (self.repo / "logs/pipeline.log").write_text("log")
        (self.repo / "state/other.json").write_text("{}")
        (self.repo / "data/articles/notes.txt").write_text("x")
        (self.repo / "data/articles/.gitkeep").write_text("")
        state_sync.bootstrap(self.repo, self.repo, "pipeline-state", "origin", "seed")
        self.assertEqual(sorted(self.tree("pipeline-state")), [
            "data/articles/a.md", "data/articles/b.md", "logs/last-run.json",
            "state/article-files.json", "state/gemini-store.json", "state/ingestion-manifest.json"])
        # Working tree, index and current branch untouched.
        self.assertEqual(run_git(self.repo, "status", "--porcelain", "--untracked-files=no"), "")
        self.assertNotEqual(run_git(self.repo, "symbolic-ref", "--short", "HEAD"), "pipeline-state")

    def test_bootstrap_refuses_existing_branch(self):
        self.bootstrap_and_push()
        run_git(self.repo, "fetch", "-q", "origin")
        with self.assertRaises(state_sync.StateSyncError):
            state_sync.bootstrap(self.repo, self.repo, "pipeline-state", "origin", "again")

    def test_restore_round_trip_is_byte_exact(self):
        self.bootstrap_and_push()
        runner = self.fresh_runner()
        info = state_sync.restore(runner, runner, state_sync_ref())
        self.assertEqual(info["manifest_articles"], 2)
        for rel in ("data/articles/a.md", "state/ingestion-manifest.json", "logs/last-run.json"):
            self.assertEqual((runner / rel).read_bytes(), (self.repo / rel).read_bytes())

    def test_restore_fails_without_branch_and_writes_nothing(self):
        clone = self.tmp / "empty"
        run_git(self.tmp, "init", "-q", str(clone))
        with self.assertRaises(state_sync.StateSyncError):
            state_sync.restore(clone, clone, state_sync_ref())
        self.assertFalse((clone / "state").exists())

    def test_restore_rejects_manifest_with_missing_article(self):
        write_state(self.repo)
        files, _ = state_sync.collect_workspace(self.repo)
        del files["data/articles/b.md"]
        commit = state_sync.commit_tree(self.repo, state_sync.build_tree(self.repo, files), "broken")
        run_git(self.repo, "update-ref", "refs/remotes/origin/pipeline-state", commit)
        target = self.tmp / "target"
        with self.assertRaisesRegex(state_sync.StateSyncError, "missing file"):
            state_sync.restore(self.repo, target, state_sync_ref())
        self.assertFalse(target.exists())

    def test_restore_rejects_empty_manifest(self):
        files = {"state/gemini-store.json": json.dumps({"store_name": STORE}).encode(),
                 "state/ingestion-manifest.json": json.dumps({"articles": {}}).encode()}
        with self.assertRaisesRegex(state_sync.StateSyncError, "empty state"):
            state_sync.validate_snapshot(files)

    def test_save_unchanged_then_pushes_fast_forward(self):
        seed = self.bootstrap_and_push()
        runner = self.fresh_runner()
        state_sync.restore(runner, runner, state_sync_ref())
        (runner / "logs/pipeline.log").write_text("not persisted")
        info = state_sync.save(runner, runner, state_sync_ref(), "noop", "pipeline-state", "origin")
        self.assertEqual((info["result"], info["commit"]), ("unchanged", seed))

        # Partial progress: a new article tracked plus an updated run summary.
        write_state(runner, names=("a.md", "b.md", "c.md"))
        (runner / "logs/last-successful-run.json").write_text("{}")
        info = state_sync.save(runner, runner, state_sync_ref(), "run 2", "pipeline-state", "origin")
        self.assertEqual(info["result"], "pushed")
        self.assertEqual(run_git(self.remote, "rev-parse", "pipeline-state"), info["commit"])
        self.assertEqual(run_git(self.remote, "rev-parse", "pipeline-state^"), seed)
        names = run_git(self.remote, "ls-tree", "-r", "--name-only", "pipeline-state").splitlines()
        self.assertIn("data/articles/c.md", names)
        self.assertNotIn("logs/pipeline.log", names)

    def test_save_never_force_pushes_over_newer_remote(self):
        self.bootstrap_and_push()
        stale = self.fresh_runner()
        state_sync.restore(stale, stale, state_sync_ref())
        other = self.fresh_runner()
        state_sync.restore(other, other, state_sync_ref())
        write_state(other, names=("a.md", "b.md", "c.md"))
        winner = state_sync.save(other, other, state_sync_ref(), "other", "pipeline-state", "origin")["commit"]

        write_state(stale, names=("a.md", "b.md", "d.md"))
        with self.assertRaises(state_sync.StateSyncError):
            state_sync.save(stale, stale, state_sync_ref(), "stale", "pipeline-state", "origin")
        self.assertEqual(run_git(self.remote, "rev-parse", "pipeline-state"), winner)

    def test_save_refuses_invalid_state_and_leaves_branch(self):
        seed = self.bootstrap_and_push()
        runner = self.fresh_runner()
        state_sync.restore(runner, runner, state_sync_ref())
        (runner / "state/ingestion-manifest.json").write_text("{truncated")
        with self.assertRaises(state_sync.StateSyncError):
            state_sync.save(runner, runner, state_sync_ref(), "bad", "pipeline-state", "origin")
        self.assertEqual(run_git(self.remote, "rev-parse", "pipeline-state"), seed)

    def test_save_refuses_files_containing_api_key(self):
        self.bootstrap_and_push()
        runner = self.fresh_runner()
        state_sync.restore(runner, runner, state_sync_ref())
        (runner / "logs/last-run.json").write_text(json.dumps({"error": "key=sk-test-secret-0001"}))
        with mock.patch.dict(os.environ, {"API_KEY": "sk-test-secret-0001"}):
            with self.assertRaisesRegex(state_sync.StateSyncError, "logs/last-run.json") as ctx:
                state_sync.save(runner, runner, state_sync_ref(), "leak", "pipeline-state", "origin")
        self.assertNotIn("sk-test-secret-0001", str(ctx.exception))

    def test_allowlist(self):
        for ok in ("state/gemini-store.json", "logs/last-successful-run.json", "data/articles/how-to-x.md"):
            self.assertTrue(state_sync.is_allowed(ok), ok)
        for bad in (".env", "logs/pipeline.log", "data/articles/../x.md", "data/articles/sub/x.md",
                    "data/articles/X.md", "state/credentials.json", "data/articles/.gitkeep"):
            self.assertFalse(state_sync.is_allowed(bad), bad)


def state_sync_ref() -> str:
    return "refs/remotes/origin/pipeline-state"


if __name__ == "__main__":
    unittest.main()
