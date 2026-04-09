# RCOS Runbook (Human + AI Collaboration)

## What is RCOS

RCOS (Repository Context Operating System) is a collaboration system for humans and general-purpose AI working on a codebase.

It is designed to control:

- authority drift
- intent loss
- attention sprawl
- verification gaps

---

# Standard Flow

## Step 0 — Prepare Minimal Context

Required:
- `manifest/project/module_index.yaml`
- current task description
- only the relevant task files

Do not dump the whole repo unless absolutely necessary.

---

## Step 1 — Produce a Change Plan

Use `manifest/templates/CHANGE_PLAN_PROMPT.md`.

Required AI output:
1. Scope Check
2. Context Summary
3. Change Intent
4. Change Plan

No code yet.

---

## Step 2 — Human Review

Check:
- file scope
- authority compliance
- hidden refactors
- missing information

---

## Step 3 — Implementation

Only after approval.

Use either:
- git patch output
- or full-file output

Choose based on reliability.

---

## Step 4 — Verification

Run:

```bash
python3 verify_rcos.py --repo-root .
```

Review:
- `manifest/repo_facts.json`
- `manifest/repo_scan.md`
- `manifest/generated_module_index.yaml`

---

## Step 5 — RCOS Update Impact

After code changes, assess whether project RCOS files must be updated.

At minimum consider:
- `manifest/project/PROJECT_STATUS.md`
- `manifest/project/CODEBASE_MAP.md`
- `manifest/project/PROJECT_ASSUMPTIONS.md`
- `manifest/project/module_index.yaml`

---

# First-Time Setup for an Existing Project

## Goal

Attach RCOS to an existing repository safely.

## Procedure

1. Copy RCOS files into the project:
   - `manifest/templates/`
   - `verify_rcos.py`

2. Create or review:
   - `manifest/project/`

3. Run verifier:
   ```bash
   python3 verify_rcos.py --repo-root .
   ```

4. Review generated facts.

5. Refine `manifest/project/module_index.yaml`.

6. Use `manifest/templates/PROJECT_SPECIFIC_RCOS_PROMPT_UNIT.md` to generate the full project-specific RCOS layer if missing.

---

# New AI Conversation Onboarding

## Minimum Materials

Always provide:
- `manifest/templates/META_INSTRUCTIONS.md`
- `manifest/project/PROJECT_BACKGROUND.md`
- `manifest/project/CODEBASE_MAP.md`
- `manifest/project/PROJECT_STATUS.md`
- `manifest/project/PROJECT_ROADMAP.md`
- `manifest/project/PROJECT_RCOS_EVOLUTION.md` (if it exists)
- `manifest/project/PROJECT_ASSUMPTIONS.md`
- `manifest/project/module_index.yaml`

Plus:
- the current task
- the 1–3 files relevant to that task

## Do Not

- paste the whole repo by default
- rely on previous thread memory
- let the AI infer the project shape from guesswork

---

# Patch Workflow

Use `manifest/templates/PATCH_WORKFLOW.md`.

Short version:
- patch only if context is stable and narrow
- otherwise prefer full-file replacement

---

# Project-Specific RCOS Layer

Project-specific files are stored under:

```text
manifest/project/
```

They should include:
- `PROJECT_BACKGROUND.md`
- `PROJECT_STATUS.md`
- `PROJECT_ASSUMPTIONS.md`
- `CODEBASE_MAP.md`
- `PROJECT_ONBOARDING_PROMPT.md`
- `PROJECT_COLLABORATION_PROMPT.md`
- `PROJECT_RCOS_MAINTENANCE.md`
- `PROJECT_ROADMAP.md`
- `PROJECT_RCOS_EVOLUTION.md`

These files are part of the operating system, not optional notes.

---

# When Project-Specific Files Must Be Updated

Update them when:
- the project goal changes
- the pipeline changes
- module authority changes
- a major feature lands
- runtime assumptions change
- the product surface or target users change
- the recommended implementation order or milestone structure changes

---

# Voluntary Upstream Sync

Sometimes a real project discovers a reusable RCOS improvement.

Examples:
- a new high-value project-specific RCOS file such as `PROJECT_ROADMAP.md`
- a more durable onboarding or maintenance rule
- a better way to track execution order and milestones

When that happens:
1. first stabilize it in the contributor project
2. summarize what is reusable vs what is project-specific
3. tag the contributor project explicitly
4. if syncing an example seed, prefer the seed path that matches the contributor project
5. do not write contributor-project evolution into an unrelated example seed
6. propose syncing it back to the main RCOS repository
7. wait for human confirmation before updating templates, prompts, or example seeds

---

# DNA Cadence

When a repository uses the RCOS DNA system:

- core RCOS updates may happen first
- example seed updates should be delayed and promoted intentionally
- artifact rebuilds should happen on release-worthy changes

Default rule:

- do not update example seeds and artifacts together during routine maintenance

Allowed exception:

- one explicit human-approved out-of-band release may update both together

---

# Failure Modes

If the AI:
- expands scope silently
- duplicates authority logic
- asks too little and guesses too much
- changes code without stating intent

Then stop and return to:
1. Scope Check
2. Change Intent
3. Change Plan

---

# Summary

RCOS works when:
- context is explicit
- scope is narrow
- authority is declared
- verification is routine
- project-specific files stay aligned with the codebase
