# RCOS Project Startup Guide

中文版: [RCOS_Project_Startup_Guide.zh-CN.md](./RCOS_Project_Startup_Guide.zh-CN.md)

This guide explains the recommended setup order, collaboration split, and meta-prompt structure for starting a brand-new project with RCOS.

It uses one common toolchain combination as an example:

- first use ChatGPT or a similar conversational model to clarify the project idea
- then hand a high-quality bootstrap prompt to Codex or another coding agent inside Cursor
- finally let Codex perform the actual RCOS project bootstrap

This is only an example stack, not a mandatory setup. You can substitute other:

- IDEs or editors
- local environments or terminal setups
- conversational models
- coding agents

as long as the overall workflow still follows RCOS discipline around context, planning, and approval.

## Table of contents

- [1. Prepare the environment](#1-prepare-the-environment)
- [2. Pull the core RCOS repository into a local working directory](#2-pull-the-core-rcos-repository-into-a-local-working-directory)
- [3. Create a new project directory and initialize git](#3-create-a-new-project-directory-and-initialize-git)
- [4. Extract the bootstrap pack directly from the pulled repository](#4-extract-the-bootstrap-pack-directly-from-the-pulled-repository)
- [5. Open the new project in your development environment](#5-open-the-new-project-in-your-development-environment)
- [6. Use a conversational model first to clarify the project idea](#6-use-a-conversational-model-first-to-clarify-the-project-idea)
- [7. Paste the meta-prompt from the appendix into the conversational model](#7-paste-the-meta-prompt-from-the-appendix-into-the-conversational-model)
- [8. Give the generated bootstrap prompt to the coding agent](#8-give-the-generated-bootstrap-prompt-to-the-coding-agent)
- [9. What Codex should accomplish during bootstrap](#9-what-codex-should-accomplish-during-bootstrap)
- [10. Reuse the onboarding prompt in later conversations](#10-reuse-the-onboarding-prompt-in-later-conversations)
- [11. Recommended split between the conversational model and the coding agent](#11-recommended-split-between-the-conversational-model-and-the-coding-agent)
- [Appendix: Meta-prompt to paste into ChatGPT](#appendix-meta-prompt-to-paste-into-chatgpt)

## 1. Prepare the environment

Before starting, make sure these basics are already in place:

- Cursor is installed
- the Codex / OpenAI coding integration you want to use is installed and authenticated
- you can start a new AI coding conversation inside Cursor

### Optional step: use a separate conversation for environment setup

If you are not yet comfortable with environment setup, or you want more step-by-step help before starting the RCOS project flow, you can handle environment setup first in a separate conversation.

This is especially useful if you:

- are new to WSL, Ubuntu, or Python development environments
- are not yet comfortable with git repos, Cursor, or coding-agent plugin setup
- want to separate environment work from project-definition work

See this standalone helper document when needed:

- [RCOS_Environment_Setup_Helper.md](./RCOS_Environment_Setup_Helper.md)

That helper includes:

- a copy-ready prompt for environment setup
- beginner-friendly setup guidance for Windows, WSL, Cursor, and coding-agent access
- instructions for returning to the formal RCOS startup flow once the environment is ready

## 2. Pull the core RCOS repository into a local working directory

The commands below use WSL `~/Workspace/` as an example path. If you are not using WSL, adjust the path to match your own local environment.

If you have not cloned the core RCOS repository locally yet, run:

    mkdir -p ~/Workspace
    cd ~/Workspace
    git clone https://github.com/culinut/RCOS.git

If you have already cloned it, update it first:

    cd ~/Workspace/RCOS
    git pull

This helps ensure that you are using the latest templates, prompts, example seeds, and bootstrap artifact from the core RCOS repository.

## 3. Create a new project directory and initialize git

Next, create your new project directory:

    mkdir -p ~/Workspace/<your-project>
    cd ~/Workspace/<your-project>
    git init

You can also make a minimal initial commit at this point, but it is not required.

## 4. Extract the bootstrap pack directly from the pulled repository

The recommended path is to unzip the bootstrap pack directly from the cloned core RCOS repo into your new project directory:

    cd ~/Workspace/<your-project>
    unzip ~/Workspace/RCOS/rcos_bootstrap_pack_with_examples.zip

After extraction, confirm that at least these directories exist:

- .rcos/
- .cursor/
- .rcos_examples/

Important:

- .rcos_examples/ contains example seeds only
- they are structure and writing references
- they must not be treated as the current project's facts

## 5. Open the new project in your development environment

At this point, open the new project directory in your preferred development environment, for example Cursor, but it does not have to be Cursor.

## 6. Use a conversational model first to clarify the project idea

Before asking a coding agent to scaffold code, do not rush straight into implementation.

A more reliable approach is to first use a conversational model to clarify the project idea, especially around:

- what problem the project solves
- who the target users are
- what the phase-one minimum deliverable is
- what is explicitly out of scope
- what technical directions or constraints already exist
- which parts are still only working assumptions

## 7. Paste the meta-prompt from the appendix into the conversational model

Take the meta-prompt from the appendix below and paste it into the conversational model you are using.

At this stage, the conversational model is not supposed to write code directly. Its job is to:

- help clarify the project
- help converge the high-level plan
- generate a project-specific RCOS new-project bootstrap prompt that can be pasted directly into Codex

## 8. Give the generated bootstrap prompt to the coding agent

Once the conversational model produces the final bootstrap prompt:

- open a new conversation in your coding-agent environment
- paste the generated prompt as-is
- let the agent start the new-project bootstrap in RCOS mode

## 9. What Codex should accomplish during bootstrap

A good RCOS new-project bootstrap usually leads Codex to:

- begin with high-level planning
- clarify scope, assumptions, and open questions
- create the initial code structure
- generate the initial .rcos/manifest/project/* project-specific context files
- add or refine .cursor/rules/* when needed
- follow the plan -> confirm -> implement pattern for any non-trivial work
- treat PROJECT_ROADMAP.md as a first-class project-specific RCOS file
- create PROJECT_RCOS_EVOLUTION.md as well if the project uses RCOS DNA tracking

## 10. Reuse the onboarding prompt in later conversations

Once the project-specific RCOS context has been established, later Codex conversations should usually start from the project's own onboarding prompt instead of re-explaining the entire project from scratch.

In practice, a short but accurate onboarding prompt is often enough for Codex to rescan the project context and quickly recover a comparable working understanding.

## 11. Recommended split between the conversational model and the coding agent

A durable division of labor looks like this:

- the conversational model helps clarify the idea
- the coding agent performs the actual RCOS bootstrap
- RCOS documentation should be created alongside the code, not retrofitted later
- example seeds provide structural reference, not project truth
- if the project uses the RCOS DNA model, keep the evolution cadence of core RCOS, example seeds, and artifacts distinct

---

## Appendix: Meta-prompt to paste into ChatGPT

    Your task is not to write code directly. Your job is to first help me clarify a new project idea and then, based on the RCOS (Repository Context Operating System) methodology, generate a complete bootstrap prompt that can be pasted directly into a coding-agent conversation.

    Here is the required background:

    RCOS is a repository context operating system for human + general AI software collaboration. Its goal is not to make AI read more code, but to make AI read the right and minimal necessary context. It does this through explicit project context files, declared responsibility boundaries, minimal-attention scanning, and a plan-before-implementation workflow. RCOS is meant to reduce authority drift, intent loss, attention sprawl, and verification gaps.

    In RCOS:
    - project-specific context usually lives under .rcos/manifest/project/*
    - reusable templates and system rules usually live under .rcos/manifest/templates/*
    - common prompts usually live under .rcos/prompts/*
    - example seeds under .rcos_examples/ are reference material only, not current-project truth
    - non-trivial work usually follows:
      - Scope Check
      - Context Summary
      - Change Intent
      - Change Plan
      - wait for confirmation
      - then implement

    Additional current RCOS expectations:
    - PROJECT_ROADMAP.md should be treated as a first-class project-specific RCOS file
    - if the project uses the RCOS DNA system, then PROJECT_RCOS_EVOLUTION.md, RCOS_EVOLUTION_PROTOCOL.md, and RCOS_DNA_REGISTRY.yaml also belong to the collaboration truth layer
    - example seeds are delayed-promotion success samples, not the current project's facts and not a high-frequency sync layer
    - zip artifacts belong to the release-artifact layer and should not be updated in lockstep with example seeds by default

    Assume the following current situation:
    - I already have a new empty git repository
    - I have already extracted the RCOS bootstrap pack into the project directory
    - the project directory already contains .rcos/, .cursor/, and .rcos_examples/
    - I will next open a new coding-agent conversation to actually bootstrap this project
    - your task is to help me clarify the project and then generate a customized RCOS bootstrap prompt for that coding agent

    Your work has two phases.

    Phase 1: Clarify the project with me

    You should actively help me organize:
    - the problem the project solves
    - the target users
    - the project goals
    - the success criteria
    - the phase-one scope
    - the non-goals
    - the technical preferences or constraints
    - the main risks
    - the temporary assumptions
    - the still-open questions

    During this phase:
    - do not write code
    - do not jump into scaffolding
    - do not freeze the specification too early
    - if the idea is still vague, keep asking follow-up questions and help me narrow it down

    Phase 2: Generate a complete bootstrap prompt for the coding agent

    Once you believe the project is clear enough, output a complete prompt that I can paste directly into a new coding-agent conversation.

    That coding-agent prompt must be long enough and explicit enough that the agent will not be confused about:
    - what RCOS is
    - what the current task is
    - what files must be read first
    - what workflow must be followed
    - what should happen before any code or project-specific RCOS files are written

    The generated prompt must:

    1. clearly state that this is an RCOS-controlled new-project bootstrap task
    2. integrate the clarified project idea, goals, scope, constraints, assumptions, and open questions
    3. explicitly require the agent, before any planning, scaffolding, or project-specific RCOS generation, to first locate and read these RCOS files if they exist:

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

    4. explicitly require the agent to treat those files as system-level / template-level rules
    5. explicitly require the agent to continue reading any additional RCOS files that those core files identify as authoritative or required
    6. explicitly require the agent not to jump straight into scanning the entire repository
    7. explicitly require the agent to do high-level planning before writing code
    8. explicitly require the agent to establish or generate the initial project-specific context, including:
       - .rcos/manifest/project/PROJECT_BACKGROUND.md
       - .rcos/manifest/project/PROJECT_STATUS.md
       - .rcos/manifest/project/PROJECT_ASSUMPTIONS.md
       - .rcos/manifest/project/CODEBASE_MAP.md
       - .rcos/manifest/project/CURRENT_BASELINE.md
       - .rcos/manifest/project/module_index.yaml
       - .rcos/manifest/project/PROJECT_ROADMAP.md
       - if the project uses the DNA system, .rcos/manifest/project/PROJECT_RCOS_EVOLUTION.md
       - and, when appropriate, onboarding / collaboration / maintenance project files as well
    9. explicitly require the agent to create initial code structure and minimal scaffold only when needed
    10. explicitly require the agent to distinguish:
        - confirmed facts
        - working assumptions
        - open questions
    11. explicitly require the agent to use minimal necessary context and not silently widen scope
    12. explicitly require the agent to follow this sequence for non-trivial work:
        - Scope Check
        - Context Summary
        - Change Intent
        - Change Plan
        - wait for confirmation before implementation
    13. explicitly require the agent to treat .rcos_examples/ only as example seeds / reference material and never as current-project truth
    14. explicitly require the agent, if reusable RCOS improvements emerge during bootstrap, to:
        - stabilize the practice in the current project first
        - distinguish between project-local practice and reusable RCOS DNA
        - tag the contributor project
        - only propose upstream sync after my confirmation
        - never write contributor-project evolution into an unrelated example seed
    15. explicitly require the agent's first response to stop after the planning stage and wait for confirmation

    The generated coding-agent prompt should instruct the agent that its first response must include:
    - Scope Check
    - Context Summary
    - Bootstrap Intent
    - Bootstrap Plan
    - Proposed first batch of files to read
    - and then stop to wait for confirmation

    When you finally output the result, output only these three sections:
    1. Project Summary
    2. Assumptions And Open Questions
    3. Coding-Agent RCOS New Project Bootstrap Prompt

    Important notes:
    - use the language I explicitly ask for when talking with me; if I do not specify one, do not hard-code a conversation language on your own
    - write the final bootstrap prompt for the coding agent in English unless I explicitly ask for another language
    - only specify the later working language if I explicitly ask for one
    - your job is not to replace the coding agent, but to generate a high-quality, executable, and well-bounded bootstrap prompt for it
    - if the project already uses the latest core RCOS, make sure the generated prompt is compatible with the latest Roadmap / DNA / release cadence rules

    If you understand, start with the first round of project clarification and ask me the most important questions first.
