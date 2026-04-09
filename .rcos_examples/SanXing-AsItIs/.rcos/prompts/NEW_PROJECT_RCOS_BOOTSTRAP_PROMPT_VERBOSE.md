# New Project RCOS Bootstrap Prompt (Verbose)

```text
You are bootstrapping a brand-new repository into an RCOS-controlled project.

Important:
- Do not assume any memory from previous conversations.
- Use minimal context first.
- You may read additional files only when necessary after evaluating scope.
- For any non-trivial task, do not implement until the human explicitly approves after your plan.

Read these files first, in this order:
1. `.rcos/manifest/templates/PROJECT_SPECIFIC_RCOS_PROMPT_UNIT.md`
2. `.rcos/manifest/templates/META_INSTRUCTIONS.md`
3. `.rcos/manifest/templates/coding_contract.md`
4. `.rcos/manifest/templates/RCOS_RUNBOOK.md`
5. `.rcos/manifest/templates/CHANGE_PLAN_PROMPT.md`

Your job has two linked goals:
1. create or scaffold the initial codebase of the new repository
2. bootstrap the project-specific RCOS layer under `.rcos/manifest/project/`

Required output directory for project-specific RCOS files:
- `.rcos/manifest/project/PROJECT_BACKGROUND.md`
- `.rcos/manifest/project/PROJECT_STATUS.md`
- `.rcos/manifest/project/PROJECT_ASSUMPTIONS.md`
- `.rcos/manifest/project/CODEBASE_MAP.md`
- `.rcos/manifest/project/PROJECT_ONBOARDING_PROMPT.md`
- `.rcos/manifest/project/PROJECT_COLLABORATION_PROMPT.md`
- `.rcos/manifest/project/PROJECT_RCOS_MAINTENANCE.md`
- `.rcos/manifest/project/CURRENT_BASELINE.md`
- `.rcos/manifest/project/module_index.yaml`

Execution contract:
- Treat `.rcos/` docs as part of the real system, not optional notes.
- Keep `.rcos` docs aligned with the code you generate.
- Do not silently expand scope.
- Do not read unrelated files unless necessary.
- If critical product or architecture facts are missing, ask for the minimum clarifications first.
- If the repository contains copied files from another successful RCOS project, treat them only as an example seed.
- Example seed content must stay in clearly non-authoritative paths such as:
  - `.rcos_examples/<seed-project>/`
  - `.rcos/examples/<seed-project>/`
- Do not reuse the old project's factual content as the new project's truth source.
- Do not blindly inherit old project names, goals, module names, authority maps, status descriptions, or assumptions.
- If copied example files are currently in active authority paths, first propose moving them into an example directory before treating the repo as initialized.

Before implementation, your output order must be:
1. Scope Check
2. Context Summary
3. Change Intent
4. Change Plan

Then stop and wait for explicit approval.

Only after approval may you:
- create the initial repo structure
- implement the initial code
- generate the RCOS project files
- align authority in `.rcos/manifest/project/module_index.yaml`

After implementation, you must provide:
1. Verification
2. RCOS Update Impact

At the end of initialization, explicitly confirm:
- PROJECT_STATUS.md matches the generated codebase
- CODEBASE_MAP.md matches the generated structure
- PROJECT_ASSUMPTIONS.md matches actual runtime and product assumptions
- module_index.yaml matches the actual authority layout
- any example seed content is isolated from the new project's active truth paths

If you understand, first summarize:
- your understanding of the initialization task
- what minimum information you still need
- your bootstrap plan

Then wait for approval.

The instructions above are written in English for clarity. All subsequent communication and generated content should use Chinese as the primary language unless the user explicitly requests otherwise.
```
