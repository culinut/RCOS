This project uses RCOS (Repository Context Operating Systems).

Important:

- There exists a `.rcos/manifest/` directory containing system and project-level documentation.
- These documents define architecture, assumptions, and collaboration rules.
- You MUST prioritize these over inferred understanding.


You are operating under RCOS strict mode.

Core principles:
1. Never default to scanning the full repository.
2. Start every task with:
   - Scope Check
   - Context Summary
   - Change Intent
   - Change Plan
3. Do not write code before plan approval.
4. Treat `.rcos/manifest/project/*` and `.rcos/manifest/templates/*` as source-of-truth context, not optional notes.
5. After any approved code change, always output:

## RCOS Update Impact

Check whether the change requires updates to:
- .rcos/manifest/project/PROJECT_STATUS.md
- .rcos/manifest/project/CODEBASE_MAP.md
- .rcos/manifest/project/PROJECT_ASSUMPTIONS.md
- .rcos/manifest/project/module_index.yaml

6. If information is missing, ask instead of guessing.
7. If scope expansion seems necessary, explicitly propose:
   - why
   - which files
   - risk
8. Avoid editing `.rcos/manifest/templates/*` unless the task is explicitly about RCOS system maintenance.
9. Prefer minimal, well-scoped edits over opportunistic refactors.
