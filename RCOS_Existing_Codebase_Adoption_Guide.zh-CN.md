# RCOS 既有代码库引入指南

English version: [RCOS_Existing_Codebase_Adoption_Guide.md](./RCOS_Existing_Codebase_Adoption_Guide.md)

这份指南面向这样一种情况：你已经有一个代码库，现在希望把 RCOS 引入进去，但又不想把它假装成一个从零开始的新项目。

它尤其适合较高级的用户，例如软件工程师、技术型创业者，或者已经有一定工程经验的构建者。这类用户通常：

- 已经拥有项目代码、文档和运行假设
- 可能已经有可用的 AI coding 环境
- 需要一种受控方式把 RCOS 接到已有仓库上
- 想避免一上来全仓扫描、静默扩 scope、或把猜测写进文档

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

## 7. 可选：先用对话模型整理 bootstrap 输入

如果这个仓库很大、很乱、历史负担很重，或者文档状态不好，先单独开一个对话模型 conversation 来整理 bootstrap 输入，通常会更稳。

这是可选步骤，但在下面这些情况尤其有帮助：

- 代码库历史包袱较多
- 入口点很多
- 大量假设还只存在于工程师脑中
- 你希望 coding agent 的 bootstrap conversation 一开始就有更清晰的 scope 和背景

## 附录：用于准备 existing-codebase bootstrap 的元提示词

如果你想先让对话模型帮你整理一版更干净的 bootstrap prompt，再交给 coding agent，可以把下面这段贴进去。

    你的任务不是实现功能，而是帮助我为一个已有代码库准备 RCOS bootstrap conversation。

    这不是一个 greenfield project。这个仓库已经包含代码、文档、历史假设，以及很可能尚未文档化的设计决策。

    我希望你帮助我做两件事：
    1. 澄清一个 coding agent 在扫描仓库前最需要掌握的最小但高价值背景
    2. 生成一份完整的 existing-codebase RCOS bootstrap prompt，供我直接贴给 coding agent

    先给你必要的 RCOS 背景：

    RCOS 是一套面向人类与通用 AI 协作开发的仓库上下文操作系统。它的目的，是通过正确的文件读取顺序、显式规划、确认门禁和 project-specific context，降低 authority drift、intent loss、attention sprawl 和 verification gaps。

    在 RCOS 里：
    - project-specific context 通常在 .rcos/manifest/project/*
    - 可复用模板和系统规则通常在 .rcos/manifest/templates/*
    - prompts 通常在 .rcos/prompts/*
    - .rcos_examples/ 下的 example seed 只是参考材料，不是当前项目事实
    - 非 trivial 的仓库任务通常要先输出：
      - Scope Check
      - Context Summary
      - Change Intent 或 Bootstrap Intent
      - Change Plan 或 Bootstrap Plan
      - 等确认
      - 再实施

    额外的当前 RCOS 预期：
    - PROJECT_ROADMAP.md 在存在时应被视为正式的 project-specific RCOS 文件
    - 如果项目启用了 RCOS DNA 机制，则 PROJECT_RCOS_EVOLUTION.md、RCOS_EVOLUTION_PROTOCOL.md、RCOS_DNA_REGISTRY.yaml 也属于协作真相层
    - coding agent 不能静默扩大 scope
    - coding agent 不能把缺失功能当成已存在
    - coding agent 不能把 example seed 当成当前项目事实

    请遵守这些原则：
    - 把这次工作当成一个 existing-codebase RCOS adoption task
    - 不要假设缺失功能
    - 不要把产品重新从零设计一遍
    - 优先分阶段扫描，不要一上来全仓扫描
    - 区分 confirmed facts、working assumptions 和 open questions
    - 保持 scope 收敛
    - 不要让 coding agent 直接跳进代码修改

    请帮助我整理：
    - 这个仓库是做什么的
    - 哪些内容已经实现
    - 哪些还只是计划
    - 哪些文件适合作为第一批阅读材料
    - 哪些不确定点应该在 bootstrap 过程中和人类确认
    - 哪些 project-specific RCOS 文件大概率需要新建或修正

    当你认为上下文已经足够清楚时，请输出一份给 coding agent 的干净 bootstrap prompt。

    这份生成出来的 prompt 必须：
    - 明确说明这是一个 existing-codebase RCOS bootstrap task
    - 明确说明这不是一个 greenfield project
    - 要求 coding agent 先读取 RCOS 核心规则与模板
    - 明确要求 coding agent 在 planning 或大范围扫描之前，先定位并读取以下文件（如果存在）：
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
    - 要求 coding agent 继续读取这些材料中被标为 authoritative 或 required 的其他 RCOS 文件
    - 要求 coding agent 分阶段扫描，而不是整仓扫描
    - 要求 coding agent 在任何大写入之前先输出：
      - Scope Check
      - Context Summary
      - Bootstrap Intent
      - Bootstrap Plan
      - Proposed first batch of files to read
    - 要求 coding agent 在那个阶段停下来等待确认
    - 要求 coding agent 在整个 bootstrap 过程中持续区分 confirmed facts、working assumptions 和 open questions
    - 要求 coding agent 在事实不足前不要大面积生成 project-specific RCOS 文件
    - 要求 coding agent 不要顺手进入功能开发，除非被明确要求
    - 要求 coding agent 在事实足够后，再生成或更新相关的 .rcos/manifest/project/* 文件

    请使用我明确指定的语言；如果我没有指定，不要没必要地强绑某种固定语言。

## 8. bootstrap 完成后回到正常 RCOS 使用方式

当已有仓库已经形成可用的 `.rcos/manifest/project/*` 之后，后续新 conversation 一般就不需要重复整个 bootstrap，而是应优先从项目自己的 onboarding prompt 开始。

也就是说，RCOS 会从“引入模式”进入“日常协作模式”。
