# RCOS Existing Codebase Adoption Guide

中文版: [RCOS_Existing_Codebase_Adoption_Guide.zh-CN.md](./RCOS_Existing_Codebase_Adoption_Guide.zh-CN.md)

This guide is for people who already have a codebase and want to introduce RCOS into it without pretending the repository is a greenfield project.

It is especially aimed at more advanced users such as software engineers, technical founders, or experienced builders who:

- already have project code, docs, and runtime assumptions
- may already have a working AI coding setup
- need a controlled way to add RCOS to an existing repository
- want to avoid full-repo scanning, silent scope expansion, and speculative documentation

## Table of contents

- [1. Decide whether you need environment help first](#1-decide-whether-you-need-environment-help-first)
- [2. Pull the core RCOS repository locally](#2-pull-the-core-rcos-repository-locally)
- [3. Add RCOS into the existing repository](#3-add-rcos-into-the-existing-repository)
- [4. Prepare the minimum materials before opening the bootstrap conversation](#4-prepare-the-minimum-materials-before-opening-the-bootstrap-conversation)
- [5. Start with the existing-codebase bootstrap prompt](#5-start-with-the-existing-codebase-bootstrap-prompt)
- [6. What the RCOS bootstrap conversation should accomplish](#6-what-the-rcos-bootstrap-conversation-should-accomplish)
- [7. Copy-ready prompt for the coding agent](#copy-ready-coding-agent-prompt)
- [8. Continue with normal RCOS usage after bootstrap](#8-continue-with-normal-rcos-usage-after-bootstrap)

## 1. Decide whether you need environment help first

If your development environment and coding-agent setup are already working, you can skip this entirely.

If you still need help with Windows / WSL / Cursor / coding-agent setup, use the optional helper first:

- [Environment Setup Helper](./RCOS_Environment_Setup_Helper.md)

Then come back here once your environment is ready.

## 2. Pull the core RCOS repository locally

If you have not cloned the core RCOS repository locally yet:

    mkdir -p ~/Workspace
    cd ~/Workspace
    git clone https://github.com/culinut/RCOS.git

If you already have it:

    cd ~/Workspace/RCOS
    git pull

## 3. Add RCOS into the existing repository

At this point, your goal is not to redesign the product. Your goal is to attach an RCOS collaboration layer to an already-existing codebase.

If the target repository does not yet contain RCOS assets, copy or extract the needed RCOS files into it first.

The important mindset is:

- this is an existing-codebase bootstrap task
- not a new-project scaffold
- not a feature implementation task

## 4. Prepare the minimum materials before opening the bootstrap conversation

Before starting a dedicated RCOS bootstrap conversation, gather the smallest useful material set:

- the repository README
- a rough directory tree
- the main entry files
- any high-level design notes or architecture docs
- any known runtime or deployment assumptions
- any engineer-provided background that would help distinguish facts from guesses

If available, also prepare:

- current module boundaries
- known problem areas
- open architectural questions

## 5. Start with the existing-codebase bootstrap prompt

For most advanced users, this is the main entry point:

- `.rcos/prompts/EXISTING_CODEBASE_RCOS_BOOTSTRAP_PROMPT.md`

Also review:

- `.rcos/prompts/EXISTING_CODEBASE_RCOS_BOOTSTRAP_MATERIALS_CHECKLIST.md`

This is usually enough if you already understand the repository and just need the coding agent to bootstrap RCOS in a disciplined way.

## 6. What the RCOS bootstrap conversation should accomplish

A good existing-codebase RCOS bootstrap should:

- scan the repository in stages rather than all at once
- separate confirmed facts, working assumptions, and open questions
- confirm key uncertainties with the human while scanning
- generate or refine `.rcos/manifest/project/*`
- avoid rewriting the product direction from scratch
- avoid opportunistic feature work unless explicitly requested

<a id="copy-ready-coding-agent-prompt"></a>

## 7. Copy-ready prompt for the coding agent

If you want a direct prompt instead of composing one yourself, paste the following into a new coding-agent conversation.

    This repository is managed under the RCOS (Repository Context Operating System) methodology.

    This is an existing-codebase RCOS bootstrap task, not a greenfield project and not a feature-implementation task.

    Your job is to bootstrap or refine the RCOS collaboration layer for an already-existing repository.

    Before doing any broad scanning, planning, or code changes, first locate and read these files if they exist:

    - `.cursor/rules/rcos_enforced.md`
    - `.cursor/rules/rcos_approval_gate.md`
    - `.rcos/manifest/templates/META_INSTRUCTIONS.md`
    - `.rcos/manifest/templates/coding_contract.md`
    - `.rcos/manifest/templates/RCOS_RUNBOOK.md`
    - `.rcos/manifest/templates/CHANGE_PLAN_PROMPT.md`
    - `.rcos/manifest/templates/PATCH_WORKFLOW.md`
    - `.rcos/manifest/templates/RCOS_UPDATE_PROTOCOL.md`
    - `.rcos/manifest/templates/PROJECT_SPECIFIC_RCOS_PROMPT_UNIT.md`
    - `.rcos/manifest/templates/RCOS_EVOLUTION_PROTOCOL.md`
    - `.rcos/manifest/RCOS_DNA_REGISTRY.yaml`
    - `.rcos/prompts/BOOTSTRAP_PACK_USAGE_NOTE.md`
    - `.rcos/prompts/EXISTING_CODEBASE_RCOS_BOOTSTRAP_PROMPT.md`

    Treat these as system-level or template-level rules.

    If any of the above files identify additional RCOS files as authoritative or required, continue reading those too before proceeding.

    This repository already has code, documents, historical assumptions, and likely some undocumented decisions.
    Do not treat it as a blank project.
    Do not assume missing functionality.
    Do not rewrite the product from scratch.
    Do not opportunistically implement features unless I explicitly ask for that.

    During bootstrap, you must:

    - scan the repository in stages rather than all at once
    - distinguish confirmed facts, working assumptions, and open questions
    - confirm key uncertainties with me as needed
    - avoid silently widening scope
    - avoid writing large project-specific RCOS files before enough facts are confirmed

    Before any large write, your first response must include:

    1. Scope Check
    2. Context Summary
    3. Bootstrap Intent
    4. Bootstrap Plan
    5. Proposed first batch of files to read

    Then stop and wait for my confirmation.

    Throughout the bootstrap, maintain the distinction between:

    - confirmed facts
    - working assumptions
    - open questions

    Once enough facts are gathered, generate or refine the relevant `.rcos/manifest/project/*` files.

    Use the language I explicitly request. If I do not specify a language, do not hard-code one unnecessarily.

## 8. Continue with normal RCOS usage after bootstrap

Once the existing repository has a usable `.rcos/manifest/project/*` layer, later conversations should usually start from the project's onboarding prompt rather than repeating the whole bootstrap process.

For that handoff stage, use the direct prompt in:

- [RCOS_New_Conversation_Onboarding_Guide.md](./RCOS_New_Conversation_Onboarding_Guide.md#copy-ready-coding-agent-prompt)

From there, RCOS can move from adoption mode into normal day-to-day collaboration mode.
