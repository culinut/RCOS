# Coding Contract (RCOS)

This file defines the behavioral contract for human + AI collaboration in an RCOS-controlled repository.

## 1. Authority

A logic area should have one primary owner module whenever possible.

Examples of authority areas:

- freshness scoring
- weighted scoring
- enrichment / localization
- final summarization
- orchestration
- UI rendering
- configuration loading

If a module owns an area, other modules should call it rather than re-implement it.

---

## 2. Separation of Concerns

Each file should ideally do one of the following:

- orchestration
- computation / scoring
- enrichment / transformation
- interface / API routing
- configuration
- runtime / scripts
- UI rendering
- documentation / prompts / manifest

Do not mix these layers unless there is a clear reason and it is recorded.

---

## 3. Intent Before Code

AI must not jump directly to code for non-trivial changes.

Required sequence:

1. Scope Check
2. Context Summary
3. Change Intent
4. Change Plan
5. Code / Patch
6. Verification
7. RCOS Update Impact

---

## 4. Minimal Scope

Each task should read and modify the minimum number of files necessary.

If more files are needed, the AI must propose a scope expansion before proceeding.

---

## 5. No Hidden Refactors

Refactors must be explicit.

Do not “clean up”, “reorganize”, “modernize”, or “improve” unrelated areas unless explicitly requested.

---

## 6. Verification Over Guessing

If repository facts are available from the verifier, use them.

If facts are missing, ask for the minimum additional evidence instead of guessing.

---

## 7. RCOS Files Are Part of the System

Manifest files are not decorative documentation. They are part of the collaboration system.

If code changes invalidate any of these:

- project background
- codebase map
- assumptions
- module authority

the RCOS files must be updated or explicitly flagged for update.
