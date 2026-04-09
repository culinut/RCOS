# RCOS Update Protocol

Use this protocol when updating the RCOS system itself.

## Goal

Allow safe evolution of:

- RCOS templates
- runbooks
- prompt units
- verifier outputs and usage rules

without introducing drift or contradictory instructions.

It also governs:

- RCOS DNA registry updates
- evolution protocol updates
- seed promotion updates
- release-artifact policy updates

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
   - DNA registry / evolution protocol
   - example seed
   - artifact policy
2. state why
3. list touched files
4. list non-touched files
5. produce full replacements or patches
6. verify cross-file consistency

---

## Seed / Artifact Release Rule

Default policy:

- do not update example seeds and release artifacts in the same routine maintenance step

Allowed exception:

- a human-approved out-of-band synchronization may update both seed and artifact together

If that happens, explicitly record:

- why the exception is needed
- which seed is affected
- which artifact is affected
- why normal delayed cadence is being overridden

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
