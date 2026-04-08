# RCOS Patch Workflow

## Goal

Produce patches that are:

- reviewable
- applyable
- scope-bounded
- consistent with RCOS authority rules

---

## Output Order

1. Scope Check
2. Context Summary
3. Change Plan
4. Patch
5. Verification
6. RCOS Update Impact

---

## Patch Rules

- Use unified diff format if possible.
- Modify only files declared in the plan.
- Do not include “bonus cleanup”.
- If patch accuracy is uncertain, say so and downgrade to full-file output.
- If line-accurate patching is unsafe because current file content is unknown, request the smallest needed excerpts.

---

## Human Apply Flow

```bash
git checkout -b rcos-change-<name>
git apply patch.diff
git add .
git commit -m "rcos: <description>"
```

If `git apply` fails and the AI lacked exact file content, prefer:
- requesting exact file excerpts
- or switching to full-file replacement

---

## When to Prefer Full-File Output

Prefer full-file output over patch when:

- file has recently been heavily reorganized
- exact current content is unknown
- imports and structure may shift
- patch brittleness is high
- the user explicitly values correctness over minimal diff
