# RCOS Existing Codebase Adoption Guide

中文版: [RCOS_Existing_Codebase_Adoption_Guide.zh-CN.md](./RCOS_Existing_Codebase_Adoption_Guide.zh-CN.md)

This guide is for people who already have a codebase and want to introduce RCOS into it without pretending the repository is a greenfield project.

It is especially aimed at more advanced users such as software engineers, technical founders, or experienced builders who:

- already have project code, docs, and runtime assumptions
- may already have a working AI coding setup
- need a controlled way to add RCOS to an existing repository
- want to avoid full-repo scanning, silent scope expansion, and speculative documentation

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

## 7. Optional: use a conversational model first to prepare the bootstrap

If the repository is large, messy, historical, or poorly documented, it can help to first open a separate conversation with a conversational model and use it to prepare a better bootstrap prompt for the coding agent.

This is optional, but useful when:

- the codebase has a lot of historical baggage
- there are multiple possible entry points
- assumptions are still partly in engineers' heads
- you want the bootstrap conversation to start with cleaner scope and stronger background

## Appendix: Meta-prompt for preparing an existing-codebase bootstrap

You can paste the following into a conversational model if you want help preparing a stronger bootstrap prompt before giving the task to the coding agent.

    Your task is not to implement features. Your task is to help me prepare an RCOS bootstrap conversation for an existing codebase.

    This is not a greenfield project. The repository already contains code, documentation, historical assumptions, and likely some undocumented decisions.

    I want you to help me do two things:
    1. clarify the minimum high-value background a coding agent should have before scanning the repository
    2. generate a complete existing-codebase RCOS bootstrap prompt that I can paste directly into a coding-agent conversation

    Here is the required RCOS background:

    RCOS is a repository context operating system for human + general AI software collaboration. It is designed to reduce authority drift, intent loss, attention sprawl, and verification gaps by forcing the agent to read the right context, in the right order, with explicit planning and confirmation gates.

    In RCOS:
    - project-specific context usually lives under .rcos/manifest/project/*
    - reusable templates and system rules usually live under .rcos/manifest/templates/*
    - prompts usually live under .rcos/prompts/*
    - example seeds under .rcos_examples/ are reference-only, not current-project truth
    - non-trivial repository tasks usually begin with:
      - Scope Check
      - Context Summary
      - Change Intent or Bootstrap Intent
      - Change Plan or Bootstrap Plan
      - wait for confirmation
      - then implement

    Additional current RCOS expectations:
    - PROJECT_ROADMAP.md is a first-class project-specific RCOS file when it exists
    - if the project uses the RCOS DNA system, then PROJECT_RCOS_EVOLUTION.md, RCOS_EVOLUTION_PROTOCOL.md, and RCOS_DNA_REGISTRY.yaml also belong to the collaboration truth layer
    - the coding agent should not silently widen scope
    - the coding agent should not treat missing functionality as if it already exists
    - the coding agent should not treat example seeds as current-project facts

    Use these principles:
    - treat this as an existing-codebase RCOS adoption task
    - do not assume missing functionality
    - do not rewrite the product from scratch
    - prefer staged scanning over full-repo scanning
    - distinguish confirmed facts, working assumptions, and open questions
    - keep scope narrow
    - do not let the coding agent jump directly into code changes

    Please help me organize:
    - what the repository is for
    - what is already implemented
    - what is only planned
    - which files are likely to be first-batch reading material
    - which uncertainties should be confirmed with the human during bootstrap
    - which project-specific RCOS files are likely to need creation or refinement

    When you think the context is clear enough, output a clean bootstrap prompt for a coding agent.

    That generated prompt must:
    - clearly say this is an existing-codebase RCOS bootstrap task
    - explicitly say this is not a greenfield project
    - require the coding agent to read the core RCOS rules and templates first
    - explicitly require the coding agent, before planning or scanning broadly, to locate and read these files if they exist:
      - .cursor/rules/rcos_enforced.md
      - .cursor/rules/rcos_approval_gate.md
      - .rcos/manifest/templates/META_INSTRUCTIONS.md
      - .rcos/manifest/templates/coding_contract.md
      - .rcos/manifest/templates/RCOS_RUNBOOK.md
      - .rcos/manifest/templates/CHANGE_PLAN_PROMPT.md
      - .rcos/manifest/templates/PATCH_WORKFLOW.md
      - .rcos/manifest/templates/RCOS_UPDATE_PROTOCOL.md
      - .rcos/manifest/templates/PROJECT_SPECIFIC_RCOS_PROMPT_UNIT.md
      - .rcos/manifest/templates/RCOS_EVOLUTION_PROTOCOL.md
      - .rcos/manifest/RCOS_DNA_REGISTRY.yaml
      - .rcos/prompts/BOOTSTRAP_PACK_USAGE_NOTE.md
      - .rcos/prompts/EXISTING_CODEBASE_RCOS_BOOTSTRAP_PROMPT.md
    - require the agent to continue reading additional RCOS files that the above materials identify as authoritative or required
    - require staged scanning rather than a full-repo scan
    - require the agent to produce, before doing any large write:
      - Scope Check
      - Context Summary
      - Bootstrap Intent
      - Bootstrap Plan
      - Proposed first batch of files to read
    - require the agent to stop and wait for confirmation at that point
    - require the agent to maintain the distinction between confirmed facts, working assumptions, and open questions throughout bootstrap
    - require the agent not to generate large project-specific RCOS files before enough facts are confirmed
    - require the agent not to opportunistically implement features unless explicitly requested
    - require the agent, once enough facts are gathered, to generate or update the relevant .rcos/manifest/project/* files

    Use the language I explicitly request. If I do not specify a language, do not hard-code one unnecessarily.

## 8. Continue with normal RCOS usage after bootstrap

Once the existing repository has a usable `.rcos/manifest/project/*` layer, later conversations should usually start from the project's onboarding prompt rather than repeating the whole bootstrap process.

From there, RCOS can move from adoption mode into normal day-to-day collaboration mode.
