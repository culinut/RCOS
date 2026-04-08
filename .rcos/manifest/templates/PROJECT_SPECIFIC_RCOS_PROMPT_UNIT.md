# Project-Specific RCOS Prompt Unit (v2)

This file contains the portable prompt unit for:
1. bootstrapping a real project into RCOS
2. onboarding a new AI thread into that project
3. daily collaboration inside that project
4. ensuring project-specific RCOS files stay updated as code evolves

The logic is intentionally split into:
- Phase 1: one-time project bootstrap
- Phase 2: repeatable daily operation

---

# Phase 1 — Project Bootstrap (One-Time)

## Goal

Generate the **project-specific RCOS files** for an existing repository from supplied materials.

This phase can also be used for a newly created repository when the AI is expected to:
- scaffold or implement the initial codebase
- introduce RCOS common templates and collaboration rules
- bootstrap the full `manifest/project/` layer in parallel with the initial implementation

## Example Seed Rule

For a brand-new repository, it is allowed to provide a previously successful RCOS project as a **reference seed**.

However:
- that seed must not remain in the new repository's active authority paths
- it must be stored under a clearly non-authoritative example path such as:
  - `.rcos_examples/<seed-project>/`
  - `.rcos/examples/<seed-project>/`
- the AI may use it only as:
  - a structure example
  - a writing-style example
  - a collaboration-pattern example

The AI must NOT use the example seed as the factual source of truth for the new project.

In particular, the AI must not blindly inherit:
- project name
- product goal
- module names
- authority map
- project status
- assumptions
- codebase map

If copied example files are found in active paths, the AI should first propose moving them into an example directory before treating the new repository as properly initialized.

## Expected output directory

The AI must generate files under:

```text
manifest/project/
  PROJECT_BACKGROUND.md
  PROJECT_STATUS.md
  PROJECT_ASSUMPTIONS.md
  CODEBASE_MAP.md
  PROJECT_ONBOARDING_PROMPT.md
  PROJECT_COLLABORATION_PROMPT.md
  PROJECT_RCOS_MAINTENANCE.md
```

## Bootstrap Prompt (copyable)

```text
You are initializing an existing project into RCOS (Repository Context Operating System).

All documentations regarding purpose, background and context of this system are located under rcos/manifest/templates/ inside the attached zip. Please first read and get a full idea.

Your task is to generate the full set of project-specific RCOS files.

Output directory (STRICT):
manifest/project/

Required files:
- PROJECT_BACKGROUND.md
- PROJECT_STATUS.md
- PROJECT_ASSUMPTIONS.md
- CODEBASE_MAP.md
- PROJECT_ONBOARDING_PROMPT.md
- PROJECT_COLLABORATION_PROMPT.md
- PROJECT_RCOS_MAINTENANCE.md

Use all and only the materials I provide:
- project descriptions
- repository structure
- selected code files
- verifier output if available
- prior project discussion

Rules:
1. Do not hallucinate missing facts.
2. If critical information is missing, ask clarifying questions before generating files.
3. Keep scope limited to the provided project.
4. Do not write code.
5. Output complete file contents, not summaries.

File requirements:

1. PROJECT_BACKGROUND.md
- what the project is
- why it exists
- value / target users
- scope boundaries

2. PROJECT_STATUS.md
- current stage
- what works now
- current limitations
- known issues
- next priorities

3. PROJECT_ASSUMPTIONS.md
- technical assumptions
- product assumptions
- AI workflow assumptions

4. CODEBASE_MAP.md
- entry points
- major directories
- main pipeline
- key authority modules
- runtime / scripts
- data flow

5. PROJECT_ONBOARDING_PROMPT.md
- a copyable prompt for a NEW AI thread to take over this project safely

6. PROJECT_COLLABORATION_PROMPT.md
- a copyable DAILY collaboration prompt
- must enforce:
  - plan before code
  - minimal scope
  - ask when missing information
  - authority compliance
  - RCOS update awareness

7. PROJECT_RCOS_MAINTENANCE.md
- define when project-specific RCOS files must be updated
- define what kinds of code changes trigger which file updates

Referencing the attached zip, please review and follow all rules in every file in rcos/manifest/templates, and following the instructions/examples in every file in rcos/manifest/project, populate true details to your fullest knowledge and belief, generate all the populated project-specific RCOS files. Finally, gather all the generated files in a downloadable zip.
（我这里写了英文便于你理解，请还是用中文交流和生成）
```

## Existing Codebase Bootstrap Prompt (copyable)

```text
You are initializing an existing codebase into RCOS (Repository Context Operating System).

This is not a normal feature-development task.
Your primary goal is to establish true, maintainable project-specific RCOS context for an already existing repository.

You must work in phases.
Do not scan the whole repository at once.

Phase 1:
- read RCOS common templates
- read existing README / docs / repo tree / entry points
- produce:
  1. Scope Check
  2. Context Summary
  3. Bootstrap Intent
  4. Bootstrap Plan
- then stop and wait for approval

Phase 2:
- after approval, scan the codebase in small batches
- after each batch, clearly separate:
  - confirmed facts
  - working assumptions
  - open questions for the human engineer
- if project intent, module purpose, or authority is unclear, ask instead of guessing

Phase 3:
- once the factual picture is sufficient, generate or update:
  - PROJECT_BACKGROUND.md
  - PROJECT_STATUS.md
  - PROJECT_ASSUMPTIONS.md
  - CODEBASE_MAP.md
  - PROJECT_ONBOARDING_PROMPT.md
  - PROJECT_COLLABORATION_PROMPT.md
  - PROJECT_RCOS_MAINTENANCE.md
  - CURRENT_BASELINE.md
  - module_index.yaml

Rules:
1. Do not turn guesses into facts.
2. Do not do business-code refactors unless explicitly requested.
3. Keep scanning incremental and explain each proposed scope expansion.
4. Treat human explanations as clarification input, but prefer repository facts when concrete implementation details conflict.
5. Explicitly mark unresolved authority questions before finalizing module_index.yaml.

Output rhythm during bootstrap:
1. Scope Check
2. Context Summary
3. Bootstrap Intent
4. Bootstrap Plan
5. Confirmed Facts
6. Open Questions
7. Proposed Next Scan Batch

The instructions above are written in English for clarity. All subsequent communication and generated content should use Chinese as the primary language unless the user explicitly requests otherwise.
```

## New Project Bootstrap Prompt (copyable)

```text
You are bootstrapping a brand-new repository into an RCOS-controlled project.

Your job has two linked goals:
1. create or scaffold the initial project codebase
2. bootstrap the full project-specific RCOS layer under `manifest/project/`

You must treat these as one coordinated initialization task, not two unrelated deliverables.

Before writing any code or files:
- first read and internalize all RCOS common templates under `rcos/manifest/templates/`
- identify the minimum information needed to initialize the project safely
- if key product or architecture facts are missing, ask for the minimum clarifications first

Output order for initialization planning:
1. Scope Check
2. Context Summary
3. Change Intent
4. Change Plan

Then stop and wait for approval before implementation.

When implementation is approved, you should:
- create the initial code / repo structure
- copy or adapt RCOS common templates into the repository as needed
- generate the full project-specific RCOS files under:

manifest/project/
  PROJECT_BACKGROUND.md
  PROJECT_STATUS.md
  PROJECT_ASSUMPTIONS.md
  CODEBASE_MAP.md
  PROJECT_ONBOARDING_PROMPT.md
  PROJECT_COLLABORATION_PROMPT.md
  PROJECT_RCOS_MAINTENANCE.md
  CURRENT_BASELINE.md
  module_index.yaml

Rules:
1. Do not hallucinate project facts.
2. Do not treat RCOS docs as optional documentation.
3. Keep the initial code and the project RCOS files aligned in the same change set.
4. Do not silently expand scope.
5. If the initial implementation changes the planned architecture, update the RCOS files before finishing.
6. Prefer minimal but true project-specific RCOS files over aspirational descriptions.
7. If authority is unclear, define it explicitly in `module_index.yaml`.
8. If the repository contains an example seed copied from another project, use it only as a non-authoritative reference and keep it outside active truth paths.
9. After implementation, always provide:

## RCOS Update Impact

At initialization time, explicitly confirm that:
- PROJECT_STATUS.md matches the generated codebase
- CODEBASE_MAP.md matches the generated structure
- PROJECT_ASSUMPTIONS.md matches actual runtime and product assumptions
- module_index.yaml matches the actual authority layout
- any example seed content remains isolated from the new project's active authority paths

The instructions above are written in English for clarity. All subsequent communication and generated content should use Chinese as the primary language unless the user explicitly requests otherwise.
```

---

# Phase 2 — Daily RCOS Operation

## Goal

Use the generated project-specific files to guide normal collaboration.

## Daily Master Prompt (copyable)

```text
You are working inside an RCOS-controlled project.

Context source priority:
1. manifest/repo_facts.json (if available)
2. manifest/project/CODEBASE_MAP.md
3. manifest/project/PROJECT_BACKGROUND.md
4. manifest/project/PROJECT_STATUS.md
5. manifest/project/PROJECT_ASSUMPTIONS.md
6. manifest/project/module_index.yaml
7. current task files

Execution rules:
1. Start with:
   - Scope Check
   - Context Summary
   - Change Intent
   - Change Plan
2. Do not generate code before plan approval.
3. Use minimal attention.
4. If scope must expand, propose it explicitly.
5. Do not duplicate logic owned by authority modules.
6. If information is missing, stop and ask for the minimum required material.

After any approved code change, you MUST output:

## RCOS Update Impact
- Does this change affect:
  - PROJECT_STATUS.md
  - CODEBASE_MAP.md
  - PROJECT_ASSUMPTIONS.md
  - module_index.yaml
- If yes, provide updated FULL file content for the affected RCOS files.

Output order (STRICT):
1. Scope Check
2. Context Summary
3. Change Intent
4. Change Plan
5. (wait for approval)
6. Implementation / Patch
7. RCOS Update Impact
```

---

# Fast New-Thread Onboarding Prompt (copyable)

```text
You are taking over a project that uses RCOS.

Read and follow:
- manifest/templates/META_INSTRUCTIONS.md
- manifest/project/PROJECT_BACKGROUND.md
- manifest/project/CODEBASE_MAP.md
- manifest/project/PROJECT_STATUS.md
- manifest/project/PROJECT_ASSUMPTIONS.md
- manifest/project/module_index.yaml

Then:
1. summarize your understanding of the system
2. identify unclear areas
3. ask clarifying questions BEFORE proposing changes
4. do not write code until a Change Plan is confirmed
```

---

# Notes

- Use the bootstrap prompt once per project initialization or whenever project-specific files are missing.
- Use the daily prompt for normal work.
- Use the onboarding prompt when starting a fresh AI conversation.
