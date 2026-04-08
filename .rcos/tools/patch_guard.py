#!/usr/bin/env python3
from __future__ import annotations

import argparse
import subprocess
from pathlib import Path
from typing import List, Tuple
from fnmatch import fnmatch

FORBIDDEN_GLOBS = [
    ".rcos/manifest/templates/*",
]

def run_git(repo_root: Path, args: List[str]) -> Tuple[int, str, str]:
    proc = subprocess.run(["git", *args], cwd=repo_root, capture_output=True, text=True)
    return proc.returncode, proc.stdout, proc.stderr

def get_changed_files(repo_root: Path) -> List[str]:
    code, out, err = run_git(repo_root, ["diff", "--name-only", "--cached"])
    if code != 0:
        code, out, err = run_git(repo_root, ["diff", "--name-only"])
    if code != 0:
        return []
    return [line.strip() for line in out.splitlines() if line.strip()]

def matches_any(path: str, patterns: List[str]) -> bool:
    return any(fnmatch(path, p) for p in patterns)

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo-root", default=".")
    parser.add_argument("--allow-template-edits", action="store_true")
    args = parser.parse_args()

    repo_root = Path(args.repo_root).resolve()
    changed = get_changed_files(repo_root)

    violations = []
    for f in changed:
        if not args.allow_template_edits and matches_any(f, FORBIDDEN_GLOBS):
            violations.append((f, "template-edit-forbidden"))

    if violations:
        print("❌ RCOS Patch Guard violations:")
        for path, reason in violations:
            print(f" - {path} [{reason}]")
        print()
        print("Hint: template edits require an explicit RCOS system maintenance task.")
        return 1

    print("✅ RCOS Patch Guard passed")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
