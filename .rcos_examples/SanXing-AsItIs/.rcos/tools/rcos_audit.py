#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import subprocess
from pathlib import Path
from typing import Dict, List, Tuple

PROJECT_REQUIRED = [
    ".rcos/manifest/project/PROJECT_STATUS.md",
    ".rcos/manifest/project/CODEBASE_MAP.md",
    ".rcos/manifest/project/PROJECT_ASSUMPTIONS.md",
    ".rcos/manifest/project/module_index.yaml",
]

RCOS_DOC_UPDATE_HINTS = {
    "CODEBASE_MAP.md": [
        "app/",
        "agent_api.py",
        "mcp_news_server.py",
        "scripts/",
        ".cursor/",
    ],
    "PROJECT_STATUS.md": [
        "app/",
        "agent_api.py",
        "mcp_news_server.py",
        "scripts/",
        "README.md",
    ],
    "PROJECT_ASSUMPTIONS.md": [
        "app/services/",
        "app/config/",
        "agent_api.py",
        "mcp_news_server.py",
        "requirements.txt",
        "pyproject.toml",
    ],
    "module_index.yaml": [
        "app/",
        "agent_api.py",
        "mcp_news_server.py",
    ],
}

IGNORE_DIRS = {".git", ".venv", "venv", "__pycache__", ".mypy_cache", ".pytest_cache", "node_modules"}

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

def file_exists(repo_root: Path, rel: str) -> bool:
    return (repo_root / rel).exists()

def classify_needed_doc_updates(changed_files: List[str]) -> Dict[str, List[str]]:
    needed: Dict[str, List[str]] = {}
    for doc, patterns in RCOS_DOC_UPDATE_HINTS.items():
        hits = []
        for f in changed_files:
            for pat in patterns:
                if f == pat or f.startswith(pat):
                    hits.append(f)
                    break
        if hits:
            needed[doc] = hits
    return needed

def headers_missing(repo_root: Path) -> List[str]:
    missing = []
    for path in repo_root.rglob("*.py"):
        if any(part in IGNORE_DIRS for part in path.parts):
            continue
        if path.parts and path.parts[0] == ".rcos":
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except Exception:
            continue
        first = text.lstrip()[:120]
        if not (first.startswith('"""') or first.startswith("'''")):
            missing.append(str(path.relative_to(repo_root)))
    return sorted(missing)

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo-root", default=".")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    repo_root = Path(args.repo_root).resolve()

    report = {
        "repo_root": str(repo_root),
        "required_files_missing": [],
        "changed_files": [],
        "suggested_rcos_updates": {},
        "python_files_missing_header": [],
        "status": "ok",
    }

    for rel in PROJECT_REQUIRED:
        if not file_exists(repo_root, rel):
            report["required_files_missing"].append(rel)

    changed = get_changed_files(repo_root)
    report["changed_files"] = changed
    report["suggested_rcos_updates"] = classify_needed_doc_updates(changed)
    report["python_files_missing_header"] = headers_missing(repo_root)

    if report["required_files_missing"]:
        report["status"] = "fail"

    if args.json:
        print(json.dumps(report, ensure_ascii=False, indent=2))
        return 1 if report["status"] != "ok" else 0

    print("🔍 RCOS Audit")
    print(f"Repo root: {repo_root}")
    print()

    if report["required_files_missing"]:
        print("❌ Missing required RCOS project files:")
        for f in report["required_files_missing"]:
            print(f" - {f}")
        print()
    else:
        print("✅ Required RCOS project files exist")
        print()

    if changed:
        print("📝 Detected changed files:")
        for f in changed:
            print(f" - {f}")
        print()
    else:
        print("ℹ️ No changed files detected from git diff")
        print()

    if report["suggested_rcos_updates"]:
        print("📌 Suggested RCOS document updates:")
        for doc, hits in report["suggested_rcos_updates"].items():
            print(f" - {doc}")
            for h in hits:
                print(f"    · because of: {h}")
        print()
    else:
        print("✅ No RCOS project document updates suggested by heuristic")
        print()

    if report["python_files_missing_header"]:
        print("⚠️ Python files missing module header block:")
        for f in report["python_files_missing_header"]:
            print(f" - {f}")
        print()
    else:
        print("✅ All scanned Python files have module header blocks")
        print()

    if report["required_files_missing"]:
        print("❌ RCOS Audit failed")
        return 1

    print("✅ RCOS Audit passed")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
