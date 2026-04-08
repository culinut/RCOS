# RCOS Update Protocol

Use this protocol when updating the RCOS system itself.

## Goal

Allow safe evolution of:

- RCOS templates
- runbooks
- prompt units
- verifier outputs and usage rules

without introducing drift or contradictory instructions.

---

## Required Inputs

Before updating RCOS files, provide:

1. current RCOS files being updated
2. change goal
3. invariants that must remain stable
4. scope boundaries

---

## Required Procedure

1. state what layer is being updated:
   - templates
   - project-specific files
   - verifier
   - runbook
2. state why
3. list touched files
4. list non-touched files
5. produce full replacements or patches
6. verify cross-file consistency

---

## Consistency Rule

If prompt files and runbook files disagree, fix the disagreement explicitly.

Do not allow:
- two different output orders
- two different authority rules
- two different scope policies

---

## Versioning

Commit RCOS updates clearly:

```bash
git commit -m "rcos: update <component>"
```
