# RCOS New Conversation Onboarding Guide

中文版: [RCOS_New_Conversation_Onboarding_Guide.zh-CN.md](./RCOS_New_Conversation_Onboarding_Guide.zh-CN.md)

This guide is for the situation where a project has already completed RCOS bootstrap, the project-specific RCOS context is already present and aligned, and you want a new coding-agent conversation to recover working context quickly from the existing RCOS files.

Typical use cases:

- the old conversation is hitting token or context limits
- the current conversation was compacted and you want to refresh full project awareness
- you want a clean new conversation without relying on memory from earlier turns
- you want the coding agent to re-ground itself from the repository truth layer before continuing work

This is not a bootstrap guide. It assumes the project already has a usable RCOS collaboration layer.

## 1. Confirm that the project already has usable RCOS context

This guide is only appropriate if the repository already contains a stable RCOS context layer, especially:

- `.rcos/manifest/project/PROJECT_BACKGROUND.md`
- `.rcos/manifest/project/PROJECT_STATUS.md`
- `.rcos/manifest/project/PROJECT_ASSUMPTIONS.md`
- `.rcos/manifest/project/CODEBASE_MAP.md`
- `.rcos/manifest/project/CURRENT_BASELINE.md`
- `.rcos/manifest/project/module_index.yaml`
- `.rcos/manifest/project/PROJECT_ONBOARDING_PROMPT.md`

If the project also uses the newer RCOS layers, it may additionally have:

- `.rcos/manifest/project/PROJECT_ROADMAP.md`
- `.rcos/manifest/project/PROJECT_RCOS_EVOLUTION.md`

If these files do not exist yet, or are obviously stale, go back to the appropriate bootstrap or maintenance flow first.

## 2. Start from the dedicated new-conversation onboarding prompt

For most cases, the main entry point is:

- `.rcos/prompts/NEW_CONVERSATION_ONBOARDING_PROMPT.md`

This prompt is designed for exactly this handoff scenario: a new conversation should read the project's existing onboarding materials, rebuild working context, summarize what it learned, and stop before jumping into implementation.

For normal follow-up work after the refresh, you may also pair it with:

- `.rcos/prompts/DAILY_ROUTINE_PROMPT.md`

## 3. What a good refresh should do

A good RCOS new-conversation refresh should let the coding agent:

- read the project's onboarding and core rule files first
- recover the collaboration workflow it is expected to follow
- summarize the project purpose, current status, and likely next working area
- distinguish confirmed facts from assumptions or still-unverified points
- avoid pretending it remembers prior conversation details that are not present in the repository truth layer
- stop after rebuilding context and wait for the next task

The point is not to recover every past chat detail. The point is to recover the project truth layer and the collaboration discipline.

## 4. Suggested user workflow

When starting a new coding-agent conversation:

1. open a clean new conversation
2. paste `.rcos/prompts/NEW_CONVERSATION_ONBOARDING_PROMPT.md`
3. if needed, add one short sentence explaining why you are refreshing context, for example:
   - the previous conversation hit token limits
   - the previous conversation was compacted
   - you want a clean context rebuild from RCOS files
4. let the agent complete the onboarding pass
5. review its summary before giving the next implementation task

## 5. What you should expect back before giving the next task

Before you continue into implementation, a good onboarding refresh should usually produce a compact but meaningful summary that includes:

- what RCOS is doing in this repository
- which workflow or approval rules the agent will follow
- what the project appears to be for
- what the current baseline or status is
- which facts seem confirmed from files
- which items still look like assumptions or open questions

If the summary is vague, overconfident, or clearly skipped key files, it is worth correcting the refresh before continuing.

## 6. Optional: use a conversational model first to prepare a richer refresh prompt

In most cases, this is not necessary. The built-in new-conversation onboarding prompt should already be enough.

However, it can still help when:

- the project has many RCOS files and you want a more guided refresh
- the previous conversation ended in a confusing state
- you want the next coding-agent conversation to self-verify its understanding before it starts work

In those cases, you can first use a conversational model to generate a slightly richer onboarding-refresh prompt for the coding agent.

## Appendix: Meta-prompt for preparing a refreshed onboarding conversation

You can paste the following into a conversational model if you want help generating a stronger new-conversation refresh prompt for a coding agent.

    Your task is not to implement code. Your task is to help me prepare a clean RCOS onboarding-refresh prompt for a new coding-agent conversation in a repository that already has a complete RCOS context layer.

    This is not a new-project bootstrap task.
    This is not an existing-codebase RCOS adoption task.
    This is a new-conversation onboarding and context-refresh task.

    Here is the required RCOS background:

    RCOS (Repository Context Operating System) is a repository context operating system for human + general AI software collaboration. Its purpose is to make the coding agent read the right and minimal necessary context, in the right order, instead of relying on broad repository scans or fragile conversational memory.

    In RCOS:
    - project-specific truth usually lives under .rcos/manifest/project/*
    - reusable system rules and templates usually live under .rcos/manifest/templates/*
    - common operational prompts usually live under .rcos/prompts/*
    - example seeds under .rcos_examples/ are reference-only, not current-project truth
    - non-trivial work usually follows:
      - Scope Check
      - Context Summary
      - Change Intent
      - Change Plan
      - wait for confirmation
      - then implement

    Additional current RCOS expectations:
    - PROJECT_ROADMAP.md is a first-class project-specific RCOS file when it exists
    - if the project uses the RCOS DNA system, then PROJECT_RCOS_EVOLUTION.md, RCOS_EVOLUTION_PROTOCOL.md, and RCOS_DNA_REGISTRY.yaml also belong to the collaboration truth layer
    - a new conversation should rebuild understanding from repository truth, not pretend to remember prior hidden context
    - a refresh pass should summarize understanding before starting work

    Assume the following situation:
    - the repository already completed RCOS bootstrap
    - the project-specific RCOS files already exist and are considered the active truth layer
    - the previous coding conversation may have hit token limits, been compacted, or otherwise lost working context
    - I want a new coding-agent conversation to recover context by reading the existing RCOS files

    Your job is to produce a complete prompt that I can paste directly into a coding-agent conversation.

    The generated prompt must:

    1. clearly state that this is an RCOS new-conversation onboarding task, not a bootstrap task
    2. explicitly require the coding agent to read, if they exist:
       - `.rcos/manifest/project/PROJECT_ONBOARDING_PROMPT.md`
       - `.cursor/rules/rcos_enforced.md`
       - `.cursor/rules/rcos_approval_gate.md`
       - relevant project-specific RCOS files referenced by the onboarding prompt
    3. explicitly require the coding agent to treat those files as the repository's current collaboration truth layer
    4. explicitly require the coding agent to follow the onboarding prompt's own reading instructions before doing anything else
    5. explicitly require the coding agent not to jump straight into implementation
    6. explicitly require the coding agent to refresh understanding from repository context rather than claiming memory from prior conversations
    7. explicitly require the coding agent, after reading, to perform a verification pass before asking for the next task

    That verification pass should ask the coding agent to summarize:

    - what RCOS appears to mean in this repository
    - which collaboration or approval rules it believes it must follow
    - what the project is for
    - what the current status or baseline appears to be
    - which points seem confirmed facts
    - which points are still assumptions, unclear, or worth rechecking

    The generated prompt should also require the coding agent to stop after that summary and wait for the next user task.

    Use the language I explicitly request. If I do not specify a language, do not hard-code one unnecessarily.

