#!/usr/bin/env python3
from __future__ import annotations

import argparse
import subprocess
from pathlib import Path

TOOLS = [
    ".rcos/tools/rcos_audit.py",
    ".rcos/tools/patch_guard.py",
]

def run(cmd, cwd):
    proc = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True)
    return proc.returncode, proc.stdout, proc.stderr

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo-root", default=".")
    args = parser.parse_args()
    repo_root = Path(args.repo_root).resolve()

    overall_ok = True
    outputs = []

    for tool in TOOLS:
        tool_path = repo_root / tool
        if not tool_path.exists():
            outputs.append((tool, 1, "", f"Missing tool: {tool}"))
            overall_ok = False
            continue
        code, out, err = run(["python3", str(tool_path), "--repo-root", str(repo_root)], repo_root)
        outputs.append((tool, code, out, err))
        if code != 0:
            overall_ok = False

    print("🔁 RCOS Selfcheck Loop")
    print()

    for tool, code, out, err in outputs:
        print(f"=== {tool} ===")
        if out:
            print(out.rstrip())
        if err:
            print(err.rstrip())
        print()

    if overall_ok:
        print("✅ All RCOS checks passed. Safe to proceed or commit.")
        return 0

    print("❌ RCOS checks failed.")
    print()
    print("AI-facing remediation checklist:")
    print("1. Summarize which check failed and why.")
    print("2. Determine whether the issue is:")
    print("   - missing RCOS project file")
    print("   - out-of-scope edit")
    print("   - missing RCOS update")
    print("   - unauthorized template edit")
    print("3. Propose the smallest possible fix.")
    print("4. Do not expand scope until approved.")
    return 1

if __name__ == "__main__":
    raise SystemExit(main())
