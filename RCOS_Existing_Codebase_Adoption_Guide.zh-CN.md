# RCOS 既有代码库引入指南

English version: [RCOS_Existing_Codebase_Adoption_Guide.md](./RCOS_Existing_Codebase_Adoption_Guide.md)

这份指南面向这样一种情况：你已经有一个代码库，现在希望把 RCOS 引入进去，但又不想把它假装成一个从零开始的新项目。

它尤其适合较高级的用户，例如软件工程师、技术型创业者，或者已经有一定工程经验的构建者。这类用户通常：

- 已经拥有项目代码、文档和运行假设
- 可能已经有可用的 AI coding 环境
- 需要一种受控方式把 RCOS 接到已有仓库上
- 想避免一上来全仓扫描、静默扩 scope、或把猜测写进文档

## 目录

- [1. 先判断是否需要环境配置帮助](#1-先判断是否需要环境配置帮助)
- [2. 先把本体 RCOS 拉到本地](#2-先把本体-rcos-拉到本地)
- [3. 把 RCOS 接到已有仓库里](#3-把-rcos-接到已有仓库里)
- [4. 在开启 bootstrap conversation 之前，先准备最小材料集](#4-在开启-bootstrap-conversation-之前先准备最小材料集)
- [5. 直接从 existing-codebase bootstrap prompt 开始](#5-直接从-existing-codebase-bootstrap-prompt-开始)
- [6. 一个好的 bootstrap conversation 应该完成什么](#6-一个好的-bootstrap-conversation-应该完成什么)
- [7. 可直接复制给 coding agent 的 prompt](#copy-ready-coding-agent-prompt)
- [8. bootstrap 完成后回到正常 RCOS 使用方式](#8-bootstrap-完成后回到正常-rcos-使用方式)

## 1. 先判断是否需要环境配置帮助

如果你的开发环境和 coding agent 配置已经可用，这一步可以直接跳过。

如果你还需要 Windows / WSL / Cursor / coding agent 方面的帮助，可以先看这份可选辅助文档：

- [环境配置辅助指南](./RCOS_Environment_Setup_Helper.zh-CN.md)

环境准备好之后，再回到这里继续。

## 2. 先把本体 RCOS 拉到本地

如果你还没有把本体 RCOS 仓库 clone 到本地：

    mkdir -p ~/Workspace
    cd ~/Workspace
    git clone https://github.com/culinut/RCOS.git

如果你已经有本体 RCOS：

    cd ~/Workspace/RCOS
    git pull

## 3. 把 RCOS 接到已有仓库里

在这个阶段，你的目标不是重做产品设计，而是给一个已经存在的代码库接上一层 RCOS 协作基础设施。

如果目标仓库里还没有 RCOS 资产，先把所需的 RCOS 文件复制或解压进去。

这里最重要的心智是：

- 这是一个既有代码库的 RCOS bootstrap 任务
- 不是新项目 scaffold
- 也不是功能开发任务

## 4. 在开启 bootstrap conversation 之前，先准备最小材料集

在开始专门的 RCOS bootstrap conversation 之前，先准备最小但有用的一组材料：

- 仓库 README
- 粗略目录树
- 主要入口文件
- 任何高层设计说明或架构文档
- 已知的运行或部署假设
- 工程师提供的背景信息，尤其是能帮助区分事实与猜测的内容

如果有的话，也建议准备：

- 当前模块边界
- 已知问题区
- 还没解决的架构疑问

## 5. 直接从 existing-codebase bootstrap prompt 开始

对多数高级用户来说，这就是主入口：

- `.rcos/prompts/EXISTING_CODEBASE_RCOS_BOOTSTRAP_PROMPT.md`

同时建议配合参考：

- `.rcos/prompts/EXISTING_CODEBASE_RCOS_BOOTSTRAP_MATERIALS_CHECKLIST.md`

如果你已经理解这个仓库的大致情况，通常这就足够了。

## 6. 一个好的 bootstrap conversation 应该完成什么

一个好的 existing-codebase RCOS bootstrap，通常应做到：

- 分阶段扫描仓库，而不是一次读完整个 repo
- 区分 confirmed facts、working assumptions 和 open questions
- 在扫描过程中持续和人类确认关键不确定点
- 生成或修正 `.rcos/manifest/project/*`
- 不要把产品方向重新发明一遍
- 不要顺手进入功能开发，除非被明确要求

<a id="copy-ready-coding-agent-prompt"></a>

## 7. 可直接复制给 coding agent 的 prompt

如果你不想自己再组织 prompt，可以直接把下面这段贴进一个新的 coding-agent conversation。

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

## 8. bootstrap 完成后回到正常 RCOS 使用方式

当已有仓库已经形成可用的 `.rcos/manifest/project/*` 之后，后续新 conversation 一般就不需要重复整个 bootstrap，而是应优先从项目自己的 onboarding prompt 开始。

在这个 handoff 阶段，可以直接使用这份指南中的可复制 prompt：

- [RCOS_New_Conversation_Onboarding_Guide.zh-CN.md](./RCOS_New_Conversation_Onboarding_Guide.zh-CN.md#copy-ready-coding-agent-prompt)

也就是说，RCOS 会从“引入模式”进入“日常协作模式”。
