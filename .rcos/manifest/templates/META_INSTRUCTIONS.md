# RCOS Meta Instructions

## What RCOS is

RCOS stands for **Repository Context Operating System**.

It is not a model, not a framework, and not a code generator. It is a collaboration protocol for humans and general-purpose AI systems working on a codebase.

RCOS exists to control four failure modes that commonly appear in AI-assisted software development:

1. **Authority drift**  
   The AI duplicates or re-implements logic that already has an authority module.

2. **Intent loss**  
   The AI outputs code without first stating what it intends to change and why.

3. **Attention sprawl**  
   Too many unrelated files are pulled into context, causing scope expansion and inconsistent edits.

4. **Verification gaps**  
   The AI makes assumptions about the repository that are not grounded in objective facts.

RCOS solves these by requiring explicit structure, explicit plans, minimal attention, and fact-first verification.

---

## Source of Truth Priority

When available, use this priority order:

1. `manifest/repo_facts.json`
2. `manifest/generated_module_index.yaml`
3. `manifest/project/module_index.yaml`
4. current source files
5. human unstated assumptions
6. AI inference

If higher-priority sources conflict with lower-priority sources, prefer the higher-priority source and explicitly mention the conflict.

---

## Required Output Order

For any non-trivial repo task, output in this order:

1. Scope Check
2. Context Summary
3. Change Intent
4. Change Plan
5. Implementation or Patch
6. Verification
7. RCOS Update Impact

Do not skip early stages unless the user explicitly asks for a direct answer and the task is trivial.

---

## Scope Rules

Default to **minimal attention**.

This means:

- read only the files needed for the current task
- do not widen scope unless necessary
- if scope must expand, state:
  - why
  - which files are added
  - what risk that creates

Never silently expand the scope of a change.

---

## Authority Rules

Treat `manifest/project/module_index.yaml` as the current declared authority map.

If a module is marked as authority for a logic area:

- do not duplicate that logic elsewhere
- do not redefine it in an orchestration file
- do not create a second “temporary” implementation

If the authority map appears incomplete or inconsistent, stop and ask for clarification, or propose a module-index update before code changes.

---

## Code Generation Rules

Before modifying code, always establish three context layers:

1. current task description
2. relevant code files only
3. `manifest/project/module_index.yaml`

If verifier output is available, treat it as a high-priority factual source:

- `manifest/repo_facts.json`
- `manifest/repo_scan.md`
- `manifest/generated_module_index.yaml`

Prefer **full-file output** when:

- structure has changed
- imports may shift
- a patch would likely be brittle
- the target AI tool is not reliable at line-accurate diff production

Prefer **git patch output** when:

- scope is narrow
- baseline is stable
- the touched files are known and limited
- the user explicitly wants patch-based application

---

## Missing Information Rule

If essential information is missing, do not guess.

Instead output:

- what is missing
- why it matters
- the smallest additional material needed

Examples:

- missing file content
- missing current path after repo reorg
- missing verifier output
- missing baseline branch / commit

---

## RCOS Maintenance Rule

After any approved code change, always assess whether RCOS project files must also be updated.

At minimum, check impact on:

- `manifest/project/PROJECT_STATUS.md`
- `manifest/project/CODEBASE_MAP.md`
- `manifest/project/PROJECT_ASSUMPTIONS.md`
- `manifest/project/module_index.yaml` (if authority changed)

If an update is needed, say so explicitly in an `RCOS Update Impact` section.

---

## Portable Usage Rule

These instructions are written for general AI systems and new conversation threads.

Therefore:

- do not rely on previous chat memory
- do not rely on hidden assumptions
- do not assume the AI has scanned the repo unless provided evidence
- always anchor to manifest files first

---

## RCOS DNA Rule

If the repository uses RCOS DNA tracking artifacts such as:

- `manifest/RCOS_DNA_REGISTRY.yaml`
- `manifest/templates/RCOS_EVOLUTION_PROTOCOL.md`
- `manifest/project/PROJECT_RCOS_EVOLUTION.md`

then treat them as part of the collaboration truth layer.

In particular:

- do not assume core DNA, example seeds, and artifacts must update together
- distinguish:
  - promoted core DNA
  - delayed seed promotion
  - release-level artifact updates
- if a tenant project has local RCOS innovations, summarize them locally before proposing upstream promotion
