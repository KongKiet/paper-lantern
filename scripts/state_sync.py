"""Persist pipeline state on a dedicated git branch (default: pipeline-state).

Stdlib only, so it runs on a bare GitHub runner without the app's dependencies.

  restore    read the allowlisted files from a git ref into the working directory;
             fails (without writing anything) if the required state is missing or invalid
  save       snapshot the allowlisted files from the working directory as a new commit
             on top of the fetched branch tip and (with --push) push it without force
  bootstrap  create the local branch from the local files, once; never pushes

Only an explicit allowlist ever enters the branch: the three state JSON files, the two
run summaries, and data/articles/<safe-name>.md. Trees are built with a temporary index,
so the working tree, the real index and the current branch are never touched.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path

REQUIRED_STATE = ("state/gemini-store.json", "state/ingestion-manifest.json")
OPTIONAL_STATE = ("state/article-files.json",)
OPTIONAL_LOGS = ("logs/last-run.json", "logs/last-successful-run.json")
ARTICLES_DIR = "data/articles"
# Same rule as scraper._SAFE_FILENAME_RE: flat, lower-case slug names only.
_ARTICLE_NAME_RE = re.compile(r"^[a-z0-9][a-z0-9-]*\.md$")
_SECRET_ENV_VARS = ("API_KEY", "GEMINI_API_KEY")
_MIN_SECRET_LEN = 8


class StateSyncError(RuntimeError):
    """Raised when state cannot be restored or saved safely."""


def is_allowed(path: str) -> bool:
    if path in REQUIRED_STATE or path in OPTIONAL_STATE or path in OPTIONAL_LOGS:
        return True
    directory, _, name = path.rpartition("/")
    return directory == ARTICLES_DIR and bool(_ARTICLE_NAME_RE.match(name))


# --- validation -------------------------------------------------------------------------

def _load_json(files: dict[str, bytes], path: str):
    try:
        return json.loads(files[path].decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise StateSyncError(f"{path} is not valid UTF-8 JSON ({type(exc).__name__}).") from None


def validate_snapshot(files: dict[str, bytes]) -> dict:
    """Check that a snapshot is complete and self-consistent; return a short description."""
    unexpected = sorted(p for p in files if not is_allowed(p))
    if unexpected:
        raise StateSyncError(f"Not in the allowlist: {', '.join(unexpected)}")
    missing = [p for p in REQUIRED_STATE if p not in files]
    if missing:
        raise StateSyncError(f"Required state file(s) missing: {', '.join(missing)}")

    store = _load_json(files, "state/gemini-store.json")
    store_name = store.get("store_name") if isinstance(store, dict) else None
    if not isinstance(store_name, str) or not store_name.startswith("fileSearchStores/"):
        raise StateSyncError("state/gemini-store.json has no valid store_name.")

    manifest = _load_json(files, "state/ingestion-manifest.json")
    articles = manifest.get("articles") if isinstance(manifest, dict) else None
    if not isinstance(articles, dict) or not articles:
        raise StateSyncError("state/ingestion-manifest.json has no articles; refusing to use empty state.")
    for article_id, entry in articles.items():
        md_path = entry.get("markdown_path") if isinstance(entry, dict) else None
        if not md_path:
            continue
        if not is_allowed(md_path) or not md_path.startswith(ARTICLES_DIR + "/"):
            raise StateSyncError(f"Manifest entry {article_id} has a non-portable markdown_path: {md_path!r}")
        if md_path not in files:
            raise StateSyncError(f"Manifest entry {article_id} references missing file {md_path}")

    for path in OPTIONAL_STATE + OPTIONAL_LOGS:
        if path in files:
            _load_json(files, path)

    return {
        "store_name": store_name,
        "manifest_articles": len(articles),
        "article_files": sum(1 for p in files if p.startswith(ARTICLES_DIR + "/")),
        "files": len(files),
    }


def check_no_secrets(files: dict[str, bytes], environ=os.environ) -> None:
    values = ((environ.get(name) or "").strip() for name in _SECRET_ENV_VARS)
    secrets = {value for value in values if len(value) >= _MIN_SECRET_LEN}
    for path, content in files.items():
        for secret in secrets:
            if secret.encode("utf-8") in content:
                # Name the file only; never the value.
                raise StateSyncError(f"{path} contains a configured API key; refusing to persist it.")


# --- working directory <-> snapshot ---------------------------------------------------------

def collect_workspace(root: Path) -> tuple[dict[str, bytes], list[str]]:
    """Read every allowlisted file present under root. Returns (files, ignored names)."""
    files: dict[str, bytes] = {}
    ignored: list[str] = []
    candidates = list(REQUIRED_STATE + OPTIONAL_STATE + OPTIONAL_LOGS)
    articles_dir = root / ARTICLES_DIR
    if articles_dir.is_dir():
        for entry in sorted(articles_dir.iterdir()):
            rel = f"{ARTICLES_DIR}/{entry.name}"
            if is_allowed(rel):
                candidates.append(rel)
            elif entry.name != ".gitkeep":
                ignored.append(rel)
    for rel in candidates:
        path = root / rel
        if path.is_symlink():
            raise StateSyncError(f"{rel} is a symlink; refusing to persist it.")
        if path.is_file():
            files[rel] = path.read_bytes()
    return files, ignored


def write_workspace(root: Path, files: dict[str, bytes]) -> None:
    for rel, content in files.items():
        target = root / rel
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(content)
    for directory in ("data/articles", "state", "logs"):
        (root / directory).mkdir(parents=True, exist_ok=True)


# --- git plumbing -------------------------------------------------------------------------

def git(repo: Path, *args: str, input: bytes | None = None, env: dict | None = None, check: bool = True) -> bytes:
    result = subprocess.run(["git", *args], cwd=repo, input=input, capture_output=True,
                            env={**os.environ, **(env or {})})
    if check and result.returncode != 0:
        stderr = result.stderr.decode("utf-8", "replace").strip()
        raise StateSyncError(f"git {args[0]} failed (exit {result.returncode}): {stderr}")
    return result.stdout


def read_ref(repo: Path, ref: str) -> tuple[dict[str, bytes], list[str]]:
    """Read allowlisted blobs from ref. Returns (files, ignored paths)."""
    if git(repo, "rev-parse", "--verify", "--quiet", f"{ref}^{{commit}}", check=False).strip() == b"":
        raise StateSyncError(f"State ref {ref!r} does not exist. Seed the state branch first (see docs/hosted-sync.md).")
    files: dict[str, bytes] = {}
    ignored: list[str] = []
    listing = git(repo, "ls-tree", "-r", "-z", "--full-tree", ref)
    for record in filter(None, listing.split(b"\0")):
        meta, path_bytes = record.split(b"\t", 1)
        mode, kind, sha = meta.decode().split()
        path = path_bytes.decode("utf-8")
        if not is_allowed(path):
            ignored.append(path)
            continue
        if kind != "blob" or mode not in ("100644", "100755"):
            raise StateSyncError(f"{path} on {ref} is not a regular file (mode {mode}).")
        files[path] = git(repo, "cat-file", "blob", sha)
    return files, ignored


def build_tree(repo: Path, files: dict[str, bytes]) -> str:
    with tempfile.TemporaryDirectory() as tmp:
        env = {"GIT_INDEX_FILE": str(Path(tmp) / "index")}
        lines = []
        for path in sorted(files):
            sha = git(repo, "hash-object", "-w", "--no-filters", "--stdin", input=files[path]).decode().strip()
            lines.append(f"100644 {sha}\t{path}\n")
        git(repo, "update-index", "--add", "--index-info", input="".join(lines).encode("utf-8"), env=env)
        return git(repo, "write-tree", env=env).decode().strip()


def commit_tree(repo: Path, tree: str, message: str, parent: str | None = None) -> str:
    args = ["commit-tree", tree, "-m", message]
    if parent:
        args += ["-p", parent]
    return git(repo, *args).decode().strip()


def write_github_output(**values) -> None:
    target = os.environ.get("GITHUB_OUTPUT")
    if target:
        with open(target, "a", encoding="utf-8") as fh:
            for key, value in values.items():
                fh.write(f"{key}={value}\n")


# --- commands -----------------------------------------------------------------------------

def restore(repo: Path, root: Path, ref: str) -> dict:
    files, ignored = read_ref(repo, ref)
    info = validate_snapshot(files)  # validate fully before writing anything
    write_workspace(root, files)
    info["ignored"] = ignored
    return info


def save(repo: Path, root: Path, parent_ref: str, message: str, branch: str | None = None,
         remote: str | None = None) -> dict:
    files, ignored = collect_workspace(root)
    info = validate_snapshot(files)
    check_no_secrets(files)
    parent = git(repo, "rev-parse", "--verify", f"{parent_ref}^{{commit}}").decode().strip()
    tree = build_tree(repo, files)
    info.update(ignored=ignored, parent=parent)
    if tree == git(repo, "rev-parse", f"{parent}^{{tree}}").decode().strip():
        info.update(result="unchanged", commit=parent)
        return info
    commit = commit_tree(repo, tree, message, parent)
    info.update(result="committed", commit=commit)
    if remote and branch:
        # No "+" prefix and no --force: a non-fast-forward update is rejected by the remote.
        git(repo, "push", "--quiet", remote, f"{commit}:refs/heads/{branch}")
        info["result"] = "pushed"
    return info


def bootstrap(repo: Path, root: Path, branch: str, remote: str, message: str) -> dict:
    for ref in (f"refs/heads/{branch}", f"refs/remotes/{remote}/{branch}"):
        if git(repo, "rev-parse", "--verify", "--quiet", ref, check=False).strip():
            raise StateSyncError(f"{ref} already exists; refusing to bootstrap over it.")
    files, ignored = collect_workspace(root)
    info = validate_snapshot(files)
    check_no_secrets(files)
    commit = commit_tree(repo, build_tree(repo, files), message)
    # Empty old value: update-ref fails if the branch appeared in the meantime.
    git(repo, "update-ref", f"refs/heads/{branch}", commit, "")
    info.update(ignored=ignored, result="created", commit=commit)
    return info


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--repo", type=Path, default=Path.cwd(), help="Git repository (default: cwd).")
    parser.add_argument("--root", type=Path, default=None, help="Directory holding data/, state/, logs/ (default: --repo).")
    sub = parser.add_subparsers(dest="command", required=True)
    p_restore = sub.add_parser("restore")
    p_restore.add_argument("--ref", required=True)
    p_save = sub.add_parser("save")
    p_save.add_argument("--parent", required=True, help="Fetched tip of the state branch.")
    p_save.add_argument("--message", required=True)
    p_save.add_argument("--push", action="store_true")
    p_save.add_argument("--remote", default="origin")
    p_save.add_argument("--branch", default="pipeline-state")
    p_boot = sub.add_parser("bootstrap")
    p_boot.add_argument("--branch", default="pipeline-state")
    p_boot.add_argument("--remote", default="origin")
    p_boot.add_argument("--message", default="Seed pipeline state from local run")
    args = parser.parse_args(argv)
    repo = args.repo.resolve()
    root = (args.root or repo).resolve()

    try:
        if args.command == "restore":
            info = restore(repo, root, args.ref)
            print(f"Restored {info['files']} file(s) from {args.ref}: {info['manifest_articles']} manifest "
                  f"article(s), {info['article_files']} Markdown file(s), store {info['store_name']}.")
        elif args.command == "save":
            info = save(repo, root, args.parent, args.message,
                        branch=args.branch if args.push else None, remote=args.remote if args.push else None)
            print(f"State {info['result']}: {info['files']} file(s), {info['manifest_articles']} manifest "
                  f"article(s), commit {info['commit'][:12]}.")
        else:
            info = bootstrap(repo, root, args.branch, args.remote, args.message)
            print(f"Created local branch {args.branch} at {info['commit'][:12]} with {info['files']} file(s): "
                  f"{info['manifest_articles']} manifest article(s), {info['article_files']} Markdown file(s), "
                  f"store {info['store_name']}.\nNothing was pushed. Review it, then: git push {args.remote} {args.branch}")
    except StateSyncError as exc:
        print(f"::error::{args.command} failed: {exc}", file=sys.stderr)
        write_github_output(result="failed")
        return 1

    if info.get("ignored"):
        print(f"Ignored (not allowlisted): {', '.join(info['ignored'])}")
    write_github_output(result=info.get("result", "restored"), commit=info.get("commit", ""),
                        manifest_articles=info["manifest_articles"], article_files=info["article_files"])
    return 0


if __name__ == "__main__":
    sys.exit(main())
