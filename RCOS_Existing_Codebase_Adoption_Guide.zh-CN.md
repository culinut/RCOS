# RCOS 既有代码库引入指南

英文版：[RCOS_Existing_Codebase_Adoption_Guide.md](./RCOS_Existing_Codebase_Adoption_Guide.md)

这份指南面向这样一种情况：你已经有一个代码库，现在希望把 RCOS 引入进去，但又不想把它假装成一个从零开始的新项目。

它尤其适合较高级的用户，例如软件工程师、技术型创业者，或者已经有一定工程经验的构建者。这类用户通常：

- 已经拥有项目代码、文档和运行假设
- 可能已经有可用的 AI 编码环境
- 需要一种受控方式把 RCOS 接到已有仓库上
- 想避免一上来全仓扫描、悄悄扩大范围、或把猜测写进文档

## 目录

- [1. 先判断是否需要环境配置帮助](#1-先判断是否需要环境配置帮助)
- [2. 先把本体 RCOS 拉到本地](#2-先把本体-rcos-拉到本地)
- [3. 把 RCOS 接到已有仓库里](#3-把-rcos-接到已有仓库里)
- [4. 在开启 RCOS 引入对话之前，先准备最小材料集](#4-在开启-rcos-引入对话之前先准备最小材料集)
- [5. 直接从既有代码库引入提示词开始](#5-直接从既有代码库引入提示词开始)
- [6. 一个好的 RCOS 引入对话应该完成什么](#6-一个好的-rcos-引入对话应该完成什么)
- [7. 可直接复制给编程agent的提示词](#copy-ready-coding-agent-prompt)
- [8. 引入完成后回到正常 RCOS 使用方式](#8-引入完成后回到正常-rcos-使用方式)

## 1. 先判断是否需要环境配置帮助

如果你的开发环境和编程agent配置已经可用，这一步可以直接跳过。

如果你还需要 Windows / WSL / Cursor / 编程agent方面的帮助，可以先看这份可选辅助文档：

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

- 这是一个既有代码库的 RCOS 引入任务
- 不是新项目搭骨架任务
- 也不是功能开发任务

## 4. 在开启 RCOS 引入对话之前，先准备最小材料集

在开始专门的 RCOS 引入对话之前，先准备最小但有用的一组材料：

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

## 5. 直接从既有代码库引入提示词开始

对多数高级用户来说，这就是主入口：

- `.rcos/prompts/EXISTING_CODEBASE_RCOS_BOOTSTRAP_PROMPT.md`

同时建议配合参考：

- `.rcos/prompts/EXISTING_CODEBASE_RCOS_BOOTSTRAP_MATERIALS_CHECKLIST.md`

如果你已经大致理解这个仓库的情况，通常这就足够了。

## 6. 一个好的 RCOS 引入对话应该完成什么

一个好的既有代码库 RCOS 引入流程，通常应做到：

- 分阶段扫描仓库，而不是一次读完整个代码库
- 区分已确认事实、工作假设和待确认问题
- 在扫描过程中持续和人类确认关键不确定点
- 生成或修正 `.rcos/manifest/project/*`
- 不要把产品方向重新发明一遍
- 不要顺手进入功能开发，除非被明确要求

<a id="copy-ready-coding-agent-prompt"></a>

## 7. 可直接复制给编程agent的提示词

如果你不想自己再组织提示词，可以直接把下面这段贴进一个新的编程agent对话。

    这个仓库采用 RCOS（Repository Context Operating System）方法来管理。

    当前任务是一个“既有代码库的 RCOS 引入任务”，不是从零开始的新项目，也不是功能开发任务。

    你的工作，是为一个已经存在的仓库建立或完善 RCOS 协作层。

    在进行大范围扫描、规划或代码修改之前，请先定位并读取以下文件（如果存在）：

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

    请把这些文件视为 system-level 或 template-level rules。

    如果这些文件中还点名了其他 authoritative 或 required 的 RCOS 文件，请在继续之前一并读取。

    这个仓库已经有代码、文档、历史假设，以及很可能尚未写下来的设计决策。
    不要把它当成空白项目。
    不要假设缺失功能已经存在。
    不要把产品重新从零设计一遍。
    除非我明确要求，否则不要顺手实现功能。

    在引入过程中，你必须：

    - 分阶段扫描仓库，而不是一次全部扫完
    - 区分 confirmed facts、working assumptions 和 open questions
    - 在需要时和我确认关键不确定点
    - 避免悄悄扩大范围
    - 在事实不足前，不要大面积生成项目级 RCOS 文件

    在做任何大写入之前，你的第一轮回复必须包括：

    1. Scope Check
    2. Context Summary
    3. Bootstrap Intent
    4. Bootstrap Plan
    5. Proposed first batch of files to read

    然后停下来，等待我的确认。

    在整个引入过程中，请始终保持以下区分：

    - confirmed facts
    - working assumptions
    - open questions

    当事实足够后，再生成或修订相关的 `.rcos/manifest/project/*` 文件。

    请使用我明确指定的语言；如果我没有指定，就不要没必要地强行绑定某一种语言。

## 8. 引入完成后回到正常 RCOS 使用方式

当已有仓库已经形成可用的 `.rcos/manifest/project/*` 后，后续新对话一般就不需要重复整个引入流程，而是应优先从项目自己的接管提示词开始。

在这个交接阶段，可以直接使用这份指南中的可复制提示词：

- [RCOS_New_Conversation_Onboarding_Guide.zh-CN.md](./RCOS_New_Conversation_Onboarding_Guide.zh-CN.md#copy-ready-coding-agent-prompt)

也就是说，RCOS 会从“引入模式”进入“日常协作模式”。
