# RCOS Bootstrap Pack

中文版简介: [README.zh-CN.md](./README.zh-CN.md)

Guide what AI reads — and you control what it does.

## An operating system for AI-assisted software development

RCOS (Repository Context Operating System) is a repository context framework for human + AI software collaboration. It is designed to help teams keep context explicit, scope controlled, authority boundaries clear, and code/documentation aligned as AI becomes part of the development workflow.

A key part of that value is that much of the working context can be generated and maintained by the AI itself, reducing human documentation overhead while also using context maintenance as a way to refresh and stabilize codebase awareness.

This repository contains reusable assets for introducing RCOS into new projects or existing codebases.

It is not meant to host one specific product. Instead, it provides reusable RCOS infrastructure, including:

- core RCOS templates
- project-specific RCOS bootstrap prompts
- new-conversation onboarding prompts
- day-to-day collaboration prompts
- existing-codebase RCOS bootstrap prompts and checklists
- a bootstrap pack that can be extracted directly into a new repository
- an example seed project for structure and writing reference

RCOS now also supports a DNA-oriented evolution model:

- tenant projects may produce reusable RCOS DNA
- the core RCOS layer, example seeds, and artifacts evolve on different cadences
- upstream sync and downstream intake should be explicit rather than automatic

## Table Of Contents

- [What It Feels Like](#what-it-feels-like)
- [What RCOS Is](#what-rcos-is)
- [Why RCOS Exists](#why-rcos-exists)
- [Quick Start](#quick-start)
- [Example Workflow](#example-workflow)
- [What RCOS Is Not](#what-rcos-is-not)
- [Repository Purpose](#repository-purpose)
- [Use Cases](#use-cases)
- [Main Contents](#main-contents)
- [Directory Structure](#directory-structure)
- [Recommended Starting Points](#recommended-starting-points)
- [Bootstrapping a New Project](#bootstrapping-a-new-project)
- [Adding RCOS to an Existing Codebase](#adding-rcos-to-an-existing-codebase)
- [Onboarding a New Conversation](#onboarding-a-new-conversation)
- [Bootstrap Pack and Example Seed](#bootstrap-pack-and-example-seed)
- [Prompt Navigation](#prompt-navigation)
- [Maintenance Notes](#maintenance-notes)
- [License](#license)

## What It Feels Like

If you've ever felt that AI coding works until it suddenly doesn't, RCOS is designed for that moment.

Without RCOS:

- AI scans large parts of the repository and loses focus
- context drifts across conversations
- changes conflict or duplicate existing logic
- documentation becomes unreliable quickly

With RCOS:

- AI reads only the files that matter
- every non-trivial change starts with an explicit plan
- scope stays controlled
- code and context stay in sync over time

RCOS turns AI coding from "guessing the repo" into a controlled collaboration system.

## What RCOS Is

RCOS is built around a simple idea: AI collaboration works better when the model reads less context, but the right context.

In RCOS, context is not only something the AI consumes. It is also something the AI can actively generate, maintain, and use to reorganize and refresh its own understanding of the codebase over time.

RCOS is not just a set of prompts, but a way to structure how humans and AI collaborate on code.

RCOS defines how context is structured, how attention is allocated, and how changes are introduced into a codebase with AI in the loop.

In practice, RCOS usually works by:

- loading minimal necessary context instead of defaulting to full-repo scans
- storing project facts, assumptions, and module authority in project-specific context files
- enforcing a plan-before-code workflow so scope, intent, and change plans are made explicit first
- keeping RCOS documentation updated alongside code so the context layer stays trustworthy

## Why RCOS Exists

Without a system like RCOS, AI-assisted development often runs into problems such as:

- the model scans too much irrelevant code and loses focus
- important project assumptions remain implicit and become inconsistent across conversations
- different AI sessions produce conflicting changes or duplicate logic
- scope expands silently during implementation
- documentation drifts away from the actual codebase and stops being trustworthy

RCOS addresses these issues by making context explicit, scoped, and continuously maintained alongside code.

Instead of relying on the model to "figure out the repo," RCOS defines how context is structured, selected, and updated.

## Quick Start

1. Copy `.rcos/` and `.cursor/` into your project.
2. Open the project in your coding environment.
3. Start a new AI conversation.
4. Paste the appropriate onboarding prompt from `.rcos/prompts/`.
5. Provide the current task plus the minimum relevant project files.
6. Follow the RCOS loop: plan -> confirm -> implement -> update context.

You now have a controlled AI collaboration loop with explicit context and approval gates.

## Example Workflow

User:
"Add caching to the news retrieval module."

AI (RCOS):
1. Scope Check
2. Context Summary
3. Change Intent
4. Change Plan

User:
"Approved."

AI:
- implements the minimal change set
- verifies the change
- updates relevant RCOS context files if needed

This loop keeps implementation controlled and aligned with project context.

RCOS turns AI from a code generator into a controlled collaborator.

## What RCOS Is Not

RCOS is not:

- a framework for building AI agents
- a code generation library
- a replacement for version control
- a guarantee that the model will always behave correctly

RCOS is:

- a system for structuring and controlling AI collaboration
- a way to make project context explicit and maintainable
- a discipline for keeping code and context aligned over time
- reusable prompt and workflow infrastructure for stable AI-assisted development

## Repository Purpose

This repository exists to package reusable RCOS collaboration assets so teams can adopt a more stable AI-assisted development workflow.

It helps with:

- initializing RCOS in new projects
- building project-specific RCOS context for existing repositories
- quickly onboarding a new AI conversation into an existing project
- maintaining plan-before-code, narrow scope, authority alignment, and documentation sync in daily collaboration

## Use Cases

These assets are mainly useful in three situations:

1. New project bootstrap
   For a brand-new repository where code and `.rcos/manifest/project/*` need to be initialized together.

2. Existing codebase RCOS adoption
   For a repository that already has code, docs, and historical complexity, and needs staged scanning plus project-specific RCOS files.

3. New conversation handoff
   For cases where context is limited and a new AI conversation needs to quickly learn the rules, project context, and collaboration style.

## Main Contents

A typical RCOS asset repository includes:

- `.rcos/manifest/templates/`
  The main source of truth for reusable RCOS templates and rules.

- `.rcos/prompts/`
  Practical prompts that can be copied directly into conversations.

- `.cursor/rules/`
  Local agent behavior constraints, such as approval gates.

- `rcos_bootstrap_pack_with_examples.zip`
  A bootstrap pack that can be extracted into a new project directory.

- `.rcos_examples/`
  A successful example project kept only as a reference seed, not as the active truth layer.

## Directory Structure

A typical layout looks like this:

```text
.rcos/
  manifest/
    templates/
    project/
  prompts/

.cursor/
  rules/

.rcos_examples/
  <seed-project>/

rcos_bootstrap_pack_with_examples.zip
```

Notes:

- `.rcos/manifest/templates/` is the reusable template layer.
- `.rcos/manifest/project/` is the active project-specific truth layer.
- `.rcos/prompts/` holds the most copy-friendly prompts.
- `.rcos_examples/` is for example seed projects only.

## Recommended Starting Points

The two best entry points are:

- `.rcos/prompts/BOOTSTRAP_PACK_USAGE_NOTE.md`
- `.rcos/prompts/PROMPT_CATALOG.md`
- [Project Startup Guide](./RCOS_Project_Startup_Guide.md)
- [Environment Setup Helper](./RCOS_Environment_Setup_Helper.md) (optional)

The first explains how to unpack and use the bootstrap pack. The second helps you choose the right prompt for each situation. The startup guide explains a fuller human workflow for pairing a conversational model with a coding agent when starting a brand-new RCOS project. The environment setup helper is optional and is meant for users who want extra step-by-step setup guidance before beginning the RCOS flow.

## Bootstrapping a New Project

For a brand-new repository, the recommended flow is:

1. Prepare the project goal, technical direction, and initial scope.
2. Review:
   - `.rcos/prompts/NEW_PROJECT_BOOTSTRAP_MATERIALS_CHECKLIST.md`
3. Start a new AI conversation with:
   - `.rcos/prompts/NEW_PROJECT_RCOS_BOOTSTRAP_PROMPT.md`
4. For more complex setups, use:
   - `.rcos/prompts/NEW_PROJECT_RCOS_BOOTSTRAP_PROMPT_VERBOSE.md`

The goal is usually to:

- initialize the code structure
- bring in reusable RCOS templates
- generate a complete `.rcos/manifest/project/*` layer for the new project

## Adding RCOS to an Existing Codebase

For an existing repository with code and docs already in place, the recommended flow is:

1. Prepare the README, directory tree, entry files, and engineer-provided background.
2. Review:
   - `.rcos/prompts/EXISTING_CODEBASE_RCOS_BOOTSTRAP_MATERIALS_CHECKLIST.md`
3. Use a dedicated new conversation with:
   - `.rcos/prompts/EXISTING_CODEBASE_RCOS_BOOTSTRAP_PROMPT.md`

The focus in this kind of session is not immediate feature work, but:

- scanning the codebase in stages
- separating confirmed facts, working assumptions, and open questions
- checking key points with engineers while scanning
- eventually generating or refining project-specific RCOS files

## Onboarding a New Conversation

If a project already has a complete `.rcos/manifest/project/*` layer and you only need a new conversation to take over, start with:

- `.rcos/prompts/NEW_CONVERSATION_ONBOARDING_PROMPT.md`

For continued day-to-day work, pair it with:

- `.rcos/prompts/DAILY_ROUTINE_PROMPT.md`

## Bootstrap Pack and Example Seed

`rcos_bootstrap_pack_with_examples.zip` is designed to:

- let you extract a ready-to-use RCOS foundation into a new repository
- include a successful example seed project to show structure and writing style

Key principle:

- the active `.rcos/manifest/project/*` must belong to the current project
- `.rcos_examples/<seed-project>/` is only an example seed
- the example seed may teach the AI about:
  - directory organization
  - prompt writing style
  - the typical granularity of RCOS project files
  - how collaboration constraints are recorded

The AI should not directly inherit from the example seed:

- project name
- product goals
- assumptions
- codebase map
- module authority
- project status

Example seeds may also demonstrate:

- roadmap planning and tracking as a first-class project-specific RCOS artifact
- how a contributor project can surface reusable RCOS improvements for possible upstream sync

But example seeds are still delayed-promotion samples, not the high-frequency DNA layer.

## Prompt Navigation

If you are not sure which prompt to use, start with:

- `.rcos/prompts/PROMPT_CATALOG.md`

Typical choices are:

- New project bootstrap:
  `NEW_PROJECT_RCOS_BOOTSTRAP_PROMPT.md`

- More complex new project bootstrap:
  `NEW_PROJECT_RCOS_BOOTSTRAP_PROMPT_VERBOSE.md`

- Existing codebase RCOS bootstrap:
  `EXISTING_CODEBASE_RCOS_BOOTSTRAP_PROMPT.md`

- New conversation onboarding:
  `NEW_CONVERSATION_ONBOARDING_PROMPT.md`

- Daily task collaboration:
  `DAILY_ROUTINE_PROMPT.md`

- RCOS audit / guard-failure repair:
  `SELF_HEAL_PROMPT.md`

## Maintenance Notes

If you maintain this repository over time, it helps to keep these habits:

- update `PROMPT_CATALOG.md` whenever new prompts are added
- update `BOOTSTRAP_PACK_USAGE_NOTE.md` whenever the pack structure changes
- when adding a new bootstrap scenario, try to add:
  - one prompt
  - one checklist
  - one usage note
- when a durable RCOS improvement is discovered in a contributor project:
  - first generalize it beyond the source project
  - tag the contributor project explicitly
  - if syncing an example seed, prefer the seed path that matches the contributor project
  - do not write contributor-project evolution into an unrelated example seed
  - sync templates, prompts, and example seed together when appropriate
  - do not upstream-sync it silently without human confirmation
- do not rebuild the bootstrap zip for every DNA change
- treat the bootstrap zip as a release artifact
- only make a same-step seed + artifact update when a human-approved exception release explicitly calls for it
- when a new project-specific file becomes durably useful, update:
  - templates
  - prompts
  - example seed
  - documentation references
- always keep the distinction clear between:
  - reusable templates
  - the active project truth layer
  - example seeds

That separation keeps the RCOS asset repository reusable instead of gradually turning into project-specific clutter.

## License

This repository is released under the MIT License. You are free to use, modify, distribute, and integrate these templates, prompts, rules, and bootstrap assets under the terms of that license.

See [LICENSE](./LICENSE) for the full text.
