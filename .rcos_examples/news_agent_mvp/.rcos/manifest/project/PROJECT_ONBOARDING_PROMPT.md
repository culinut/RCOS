# Project Onboarding Prompt

```text
You are taking over an RCOS-controlled repository: `news_agent_mvp`.

Important:
- Do not assume any memory from previous conversations.
- Use minimal context first, but you may read additional code files only when necessary after evaluating scope.
- Follow RCOS strictly.
- For any non-trivial task, do not implement until the human explicitly approves after your plan.

Read these files first, in this order:

1. `.cursor/rules/rcos_enforced.md`
2. `.cursor/rules/rcos_approval_gate.md`

3. `.rcos/manifest/templates/META_INSTRUCTIONS.md`
4. `.rcos/manifest/templates/coding_contract.md`
5. `.rcos/manifest/templates/RCOS_RUNBOOK.md`
6. `.rcos/manifest/templates/CHANGE_PLAN_PROMPT.md`

7. `.rcos/manifest/project/PROJECT_BACKGROUND.md`
8. `.rcos/manifest/project/PROJECT_ASSUMPTIONS.md`
9. `.rcos/manifest/project/PROJECT_STATUS.md`
10. `.rcos/manifest/project/CODEBASE_MAP.md`
11. `.rcos/manifest/project/CURRENT_BASELINE.md`
12. `.rcos/manifest/project/module_index.yaml`

If verifier artifacts exist, treat them as higher-priority factual sources:
- `.rcos/manifest/repo_facts.json`
- `.rcos/manifest/repo_scan.md`
- `.rcos/manifest/generated_module_index.yaml`

After reading them:
- summarize the project
- summarize the RCOS workflow you will follow
- summarize the approval gate you must obey
- state what is confirmed fact vs what is still unverified
- wait for the next task

Collaboration contract you must obey:
- Treat `.rcos/` documents as part of the real system, not optional notes.
- Keep `.rcos` docs aligned with code changes.
- Do not silently expand scope.
- Do not read unrelated files unless necessary.
- For non-trivial tasks, your output order must be:
  1. Scope Check
  2. Context Summary
  3. Change Intent
  4. Change Plan
- Then stop and wait for explicit approval.
- Only after approval may you implement.
- After implementation, do verification and report `RCOS Update Impact`.

Current high-value confirmed project context:
- This repo is a Python + FastAPI news summary MVP, better described as a single-turn agentic workflow, not a full autonomous agent.
- Current pipeline: inline planner -> `get_hotlist` -> relevance scoring -> enrichment -> summarizer.
- Planner authority is still effectively in `app/services/agent.py`, not fully migrated to `app/services/planner.py`.
- Freshness authority must stay centralized in `app/services/freshness.py`.
- `app/services/scoring.py` should consume freshness results and must not duplicate freshness logic.
- `fetch_url` exists but is not yet part of the main summarization pipeline.
- `.env.example` is not a reliable description of the actual runtime configuration.

Recent implemented behavior that must be preserved:
- Active logging writes to `logs/server.log`.
- Hourly rollover produces `logs/server.log.YYYY-MM-DD-HH`.
- Older hourly logs are archived to `logs/archive/yyyy/mm/dd/hh/server.log.YYYY-MM-DD-HH`.
- Startup housekeeping now reconciles stale active `server.log` after restart or long suspension before writing fresh logs.
- Archival writes an explicit log line.
- `/log` now supports archive browsing:
  - latest view for current `server.log`
  - archive mode with year/month selectors limited to actually available archive entries
  - clickable highlighted days with logs
  - hour dropdown populated only from existing hourly files
  - button to return to latest `server.log`
- `/log/raw` still only returns the active `server.log`.

If you need to inspect the most recently changed code for these areas, read only these files first:
- `app/core/logging.py`
- `app/api/routes.py`
- `app/web/log_page.py`
- `app/services/freshness.py`
- `app/services/scoring.py`

Do not jump ahead. Read only the files above first, summarize, and wait.

The instructions above are written in English for clarity. All subsequent communication and generated content should use Chinese as the primary language unless the user explicitly requests otherwise.
```
