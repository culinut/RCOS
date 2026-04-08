# Change Plan Prompt

Use this prompt whenever you want an AI to plan a modification before writing code.

```text
You are working inside an RCOS-controlled repository.

Context:
- `manifest/repo_facts.json` (if available)
- `manifest/generated_module_index.yaml` (if available)
- `manifest/project/module_index.yaml`
- current task files only
- current task goal

Your job is to produce a Change Plan before any code.

Required output:

1. Scope Check
2. Context Summary
3. Change Intent
4. Change Plan

Rules:
- list only necessary files
- explicitly list read-only files
- explicitly list files not to touch
- do not duplicate logic already owned by an authority module
- do not generate code yet
- if scope must expand, explain why
- if information is missing, request the minimum additional material
```
