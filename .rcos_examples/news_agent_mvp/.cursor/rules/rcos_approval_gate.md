# RCOS Approval Gate

This repository uses an approval-first RCOS workflow for non-trivial tasks.

## Purpose

Prevent AI from making code or documentation changes before the human has reviewed the intended scope and plan.

## Rule

For any non-trivial task, the AI must stop after producing:

1. Scope Check
2. Context Summary
3. Change Intent
4. Change Plan

No implementation is allowed until the human explicitly approves proceeding.

## Allowed Before Approval

- Read only the minimum files needed to understand the task
- Consult `.rcos/manifest/` files as source-of-truth context
- Identify missing information
- Propose the smallest necessary scope expansion
- Produce a plan

## Not Allowed Before Approval

- Editing code files
- Editing RCOS files
- Creating new files
- Running write-producing refactors or formatting changes
- Performing hidden cleanup outside the approved scope

## Scope Rule

- Do not silently expand scope
- If more files are needed, state:
  - why
  - which files
  - what risk this adds

## After Approval

Once approval is given:

- implement only the approved scope
- keep authority aligned with `manifest/project/module_index.yaml`
- avoid opportunistic refactors
- verify the changed area
- report `RCOS Update Impact`

## Priority

If there is any tension between speed and process, prefer the approval gate.
