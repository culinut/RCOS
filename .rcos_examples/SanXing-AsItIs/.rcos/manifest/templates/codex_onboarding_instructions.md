You are taking over a project that uses RCOS (Repository Context Operating System).

Before doing anything, you MUST read and follow ALL RCOS documents under:

.rcos/manifest/

Especially:

* .rcos/manifest/templates/META_INSTRUCTIONS.md
* .rcos/manifest/project/PROJECT_BACKGROUND.md
* .rcos/manifest/project/CODEBASE_MAP.md
* .rcos/manifest/project/PROJECT_STATUS.md
* .rcos/manifest/project/PROJECT_ASSUMPTIONS.md
* .rcos/manifest/project/module_index.yaml

---

# 🔴 Core Principle (CRITICAL)

RCOS exists to allow accurate collaboration WITHOUT loading the entire codebase into memory.

You MUST:

* Use MINIMAL necessary context
* DO NOT scan or read the entire repo by default
* ONLY read additional files when you explicitly determine they are necessary

You ARE allowed to read any file — but ONLY after:

→ performing a Scope Check
→ justifying why the file is needed

---

# 🧠 Project Context Alignment Rules

You must treat:

* `.rcos/` documentation
* project-level assumptions
* CODEBASE_MAP
* module_index

as **part of the source of truth of the system**, not just comments.

This means:

* If code contradicts RCOS → you must surface it
* If assumptions are outdated → you must propose updates
* If you change code → you MUST reflect that in RCOS files

RCOS docs are **co-equal with code**.

---

# 🔁 RCOS Maintenance Obligation

After ANY confirmed code change, you MUST output:

## RCOS Update Impact

Check whether the change affects:

* PROJECT_STATUS.md
* CODEBASE_MAP.md
* PROJECT_ASSUMPTIONS.md
* module_index.yaml

If YES:

→ Provide updated FULL file content
→ These must be committed together with code changes

You MAY create new RCOS documents if helpful.

---

# ⚙️ Collaboration Protocol

You MUST follow:

1. Scope Check
2. Context Summary
3. Change Intent
4. Change Plan

DO NOT write code until plan is confirmed.

---

# ❓ Missing Information Rule

If information is insufficient:

→ STOP
→ Ask clarification questions

DO NOT guess.

---

# 🔧 About Code Changes

RCOS originally requires git patch output.

However, in this environment:

* You MAY directly modify files after plan approval
* You MUST clearly explain what was changed
* You MUST still follow RCOS structure and intent

---

# 📌 Now proceed:

1. Summarize your understanding of the system
2. Identify unclear areas
3. Ask clarification questions

DO NOT propose changes yet.
