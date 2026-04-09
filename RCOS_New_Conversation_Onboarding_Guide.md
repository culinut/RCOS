# RCOS New Conversation Onboarding Guide

中文版: [RCOS_New_Conversation_Onboarding_Guide.zh-CN.md](./RCOS_New_Conversation_Onboarding_Guide.zh-CN.md)

This guide is for the situation where a project has already completed RCOS bootstrap, the project-specific RCOS context is already present and aligned, and you want a new coding-agent conversation to recover working context quickly from the existing RCOS files.

Typical use cases:

- the old conversation is hitting token or context limits
- the current conversation was compacted and you want to refresh full project awareness
- you want a clean new conversation without relying on memory from earlier turns
- you want the coding agent to re-ground itself from the repository truth layer before continuing work

This is not a bootstrap guide. It assumes the project already has a usable RCOS collaboration layer.

## Table of contents

- [1. Confirm that the project already has usable RCOS context](#1-confirm-that-the-project-already-has-usable-rcos-context)
- [2. Start from the dedicated new-conversation onboarding prompt](#2-start-from-the-dedicated-new-conversation-onboarding-prompt)
- [3. What a good refresh should do](#3-what-a-good-refresh-should-do)
- [4. Suggested user workflow](#4-suggested-user-workflow)
- [5. What you should expect back before giving the next task](#5-what-you-should-expect-back-before-giving-the-next-task)
- [6. Copy-ready prompt for the coding agent](#copy-ready-coding-agent-prompt)

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

<a id="copy-ready-coding-agent-prompt"></a>

## 6. Copy-ready prompt for the coding agent

If you want a direct prompt instead of relying on a separate preparation step, paste the following into a new coding-agent conversation.

    This repository is managed under the RCOS (Repository Context Operating System) methodology.

    This is a new-conversation onboarding and context-refresh task.
    It is not a new-project bootstrap task.
    It is not an existing-codebase RCOS adoption task.

    The repository already has a usable RCOS context layer.
    Your job is to rebuild working context from the existing RCOS files before any new implementation work begins.

    First locate and read these files if they exist:

    - `.rcos/manifest/project/PROJECT_ONBOARDING_PROMPT.md`
    - `.cursor/rules/rcos_enforced.md`
    - `.cursor/rules/rcos_approval_gate.md`

    Then follow the onboarding prompt's own reading instructions and read any project-specific RCOS files it identifies as required.

    Treat those files as the repository's current collaboration truth layer.

    Do not jump straight into implementation.
    Do not pretend to remember hidden context from previous conversations.
    Rebuild your understanding from the repository truth layer instead.

    After reading, perform a verification pass before asking for the next task.

    Your verification summary must include:

    - what RCOS appears to mean in this repository
    - which collaboration or approval rules you believe you must follow
    - what the project is for
    - what the current status or baseline appears to be
    - which points seem to be confirmed facts
    - which points are still assumptions, unclear, or worth rechecking

    Then stop and wait for my next task.

    Use the language I explicitly request. If I do not specify a language, do not hard-code one unnecessarily.
