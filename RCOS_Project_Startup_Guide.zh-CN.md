# RCOS 项目启动指南

English version: [RCOS_Project_Startup_Guide.md](./RCOS_Project_Startup_Guide.md)

这份指南说明：如果你想用 RCOS 启动一个全新的项目，推荐的准备顺序、协作分工和启动提示词应该怎么组织。

它以一组常见工具组合作为示例：

- 你先用 ChatGPT 或类似对话模型把项目想法聊清楚
- 再把高质量 bootstrap prompt 交给 Codex 或 Cursor 中的 coding agent
- 最后让 Codex 按 RCOS 流程完成新项目 bootstrap

这只是示例组合，不是强制要求。你完全可以替换为其他：

- IDE / 编辑器
- 操作系统或终端环境
- 对话模型
- coding agent

只要整体流程仍然符合 RCOS 的上下文、规划和审批纪律即可。

## 1. 先准备环境

建议先确认这些基础条件已经就绪：

- 已安装 Cursor
- 已安装并登录你要使用的 Codex / OpenAI 编码插件或集成能力
- 你可以在 Cursor 中正常发起新的 AI coding conversation

### 可选步骤：先单独完成环境配置

如果你对环境配置还不熟，或者希望在进入 RCOS 项目启动流程之前先把基础环境一步步准备好，可以先单独完成环境配置。

适合这种情况的读者：

- 刚开始接触 WSL、Ubuntu 或 Python 开发环境
- 不熟悉 git repo、Cursor、或 coding agent 插件配置
- 希望先把环境问题拆开，不和项目设计讨论混在一起

请按需查看这份单独文档：

- [RCOS_Environment_Setup_Helper.zh-CN.md](./RCOS_Environment_Setup_Helper.zh-CN.md)

那份文档里包含：

- 一个可直接复制给对话模型的环境配置 prompt
- Windows / WSL / Cursor / coding agent 的前置准备建议
- 如何在完成环境准备后回到正式的 RCOS 项目启动流程

## 2. 先把本体 RCOS 拉到本地工作目录

下面使用 WSL 的 `~/Workspace/` 作为示例路径。如果你使用的不是 WSL，而是其他本地环境，请按你的实际目录调整。

如果你还没有把本体 RCOS 仓库 clone 到本地，建议先执行：

    mkdir -p ~/Workspace
    cd ~/Workspace
    git clone https://github.com/culinut/RCOS.git

如果你已经 clone 过，则先更新到最新版本：

    cd ~/Workspace/RCOS
    git pull

这样可以确保你拿到的是本体 RCOS 的最新模板、prompt、example seed 和 bootstrap artifact。

## 3. 创建新的项目目录并初始化 git

接着创建你的新项目目录：

    mkdir -p ~/Workspace/<your-project>
    cd ~/Workspace/<your-project>
    git init

你也可以顺手做一个最小初始提交，但不是必须。

## 4. 从 pulled repo 直接解压 bootstrap pack

推荐直接从本体 RCOS 仓库里把 bootstrap pack 解压到新项目目录：

    cd ~/Workspace/<your-project>
    unzip ~/Workspace/RCOS/rcos_bootstrap_pack_with_examples.zip

解压后，至少应确认这些目录已经存在：

- .rcos/
- .cursor/
- .rcos_examples/

注意：

- .rcos_examples/ 里的内容只是 example seed
- 它们只能提供结构和写法参考
- 不能被当成当前项目事实来源

## 5. 在你的开发环境中打开新项目

现在可以在你使用的开发环境中打开这个新项目目录了，例如 Cursor，但并不局限于 Cursor。

## 6. 先用对话模型把项目想法聊清楚

在真正让 coding agent 写代码之前，不要急着直接让它开始 scaffold。

更稳的做法是先在对话模型里把项目 idea 尽量聊清楚，尤其是这些问题：

- 这个项目要解决什么问题
- 目标用户是谁
- 第一阶段最小可交付范围是什么
- 明确不做什么
- 有哪些技术方向或约束
- 哪些内容目前还只是工作假设

## 7. 把附录中的元提示词贴给对话模型

把本文后面的元提示词直接贴给你使用的对话模型，让它继续和你把项目想法聊开。

这一步里，对话模型的职责不是直接写代码，而是：

- 帮你澄清项目
- 帮你收敛高层规划
- 最后生成一份结合你的项目想法、可直接贴给 Codex 的 RCOS new project bootstrap prompt

## 8. 把生成的 bootstrap prompt 交给 coding agent

当对话模型产出最终 prompt 后：

- 在你的 coding agent 环境里新开一个新 conversation
- 把生成的那份 prompt 原样贴进去
- 让 agent 按 RCOS 方式开始新项目 bootstrap

## 9. Codex 在 bootstrap 中的目标

一个好的 RCOS new-project bootstrap，通常应让 Codex：

- 先做 high-level planning
- 明确 scope、assumptions 和 open questions
- 建立初始代码结构
- 生成 .rcos/manifest/project/* 的初始 project-specific context files
- 必要时补充 .cursor/rules/*
- 在 non-trivial 工作中遵守先 plan、等确认、再实施
- 把 PROJECT_ROADMAP.md 视为正式 project-specific RCOS 文件
- 如果项目使用 RCOS DNA 机制，则同时建立 PROJECT_RCOS_EVOLUTION.md

## 10. 后续 conversation 优先复用 onboarding prompt

当项目已经建立起 RCOS project context 后，后续再开新的 Codex conversation 时，优先使用项目内已有的 onboarding prompt，而不是每次重新从头解释项目。

在实践中，一个简短但准确的 onboarding prompt，通常就足以让 Codex 重新扫描项目 context，并快速恢复到接近相同的上下文掌握水平。

## 11. 对话模型与 coding agent 的推荐分工

一个很稳的分工方式是：

- 对话模型负责把想法聊清楚
- coding agent 负责按 RCOS 流程落地 bootstrap
- RCOS 文档与代码应一起建立，而不是事后补写
- example seed 只提供结构参考，不提供当前项目事实
- 如果项目启用了 RCOS DNA 机制，要区分 core RCOS、example seed 和 artifact 的不同演化节奏

---

## 附录：可直接复制给对话模型的元提示词

    你现在的任务不是直接写代码，而是先帮我把一个新项目想法聊清楚，然后基于 RCOS（Repository Context Operating System）方法，为 Codex 生成一份可以直接执行的新项目 bootstrap prompt。

    先给你必要背景：

    RCOS 是一套面向人类与通用 AI 协作开发的仓库上下文操作系统。它的目标不是让 AI 读取更多代码，而是让 AI 读取正确且最小必要的上下文，并通过显式的项目上下文文件、职责边界、先规划后实施的流程，降低职责漂移、意图丢失、注意力扩散和验证缺口。

    RCOS 的一些关键特征：
    - 上下文不是只给 AI 读取的，很多上下文也可以由 AI 主动生成和持续维护
    - 项目上下文会沉淀在 .rcos/manifest/project/*
    - 通用模板和规则通常在 .rcos/manifest/templates/*
    - 常用 prompt 在 .rcos/prompts/*
    - 非 trivial 工作通常遵守：
      - Scope Check
      - Context Summary
      - Change Intent
      - Change Plan
      - 等人确认
      - 再实施
    - PROJECT_ROADMAP.md 应被视为正式 project-specific RCOS 文件
    - 如果项目启用了 RCOS DNA 机制，则 PROJECT_RCOS_EVOLUTION.md、RCOS_EVOLUTION_PROTOCOL.md、RCOS_DNA_REGISTRY.yaml 也属于协作真相层的一部分
    - example seed 是延迟 promotion 的成功样本，不是当前项目事实，也不是高频同步层
    - zip artifact 属于 release artifact 层，不应与 example seed 进行默认同步更新

    当前情况假设如下：
    - 我已经有一个新的空 git repo
    - 我已经把 RCOS bootstrap pack 解压进项目目录
    - 项目目录里已经有 .rcos/、.cursor/ 和 .rcos_examples/
    - 我接下来会在 Cursor / Codex 中开启一个新的 conversation 来真正 bootstrap 这个项目
    - 你的任务是先和我把项目 idea 聊清楚，然后为 Codex 生成一份定制的 bootstrap prompt

    你的工作分两阶段：

    第一阶段：和我一起澄清项目
    你需要主动帮助我整理这些内容：
    - 项目要解决的问题
    - 目标用户
    - 项目目标
    - 成功标准
    - 第一阶段范围
    - 非目标
    - 技术偏好或约束
    - 风险点
    - 暂时假设
    - 仍然开放的问题

    这阶段你不要直接写代码，也不要过早替我定规格。
    如果信息不够清楚，你要继续追问并帮助我收敛。

    第二阶段：生成一份给 Codex 的完整 bootstrap prompt
    当你认为项目已经足够清楚时，请输出一份可直接复制到 Codex 新 conversation 里的完整 prompt。

    这份给 Codex 的 prompt 必须：
    1. 明确这是一个 RCOS-controlled new project bootstrap task
    2. 把我们刚才聊清楚的项目 idea、目标、范围、约束、假设整合进去
    3. 明确要求 Codex 在开始任何 high-level planning、代码 scaffold 或 project-specific context generation 之前，先读取并理解以下 RCOS 文件（如果存在）：

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

    4. 明确要求 Codex 把这些文件当作 system-level / template-level rules 来理解，并以它们作为后续 bootstrap 的起点，而不是直接跳去读整个 repo
    5. 要求 Codex 继续读取这些核心文件中明确引用为 authoritative 或 required 的其他 RCOS 文件
    6. 要求 Codex 先做 high-level planning，而不是立即写代码
    7. 要求 Codex 建立初始 project-specific context，包括：
       - .rcos/manifest/project/PROJECT_BACKGROUND.md
       - .rcos/manifest/project/PROJECT_STATUS.md
       - .rcos/manifest/project/PROJECT_ASSUMPTIONS.md
       - .rcos/manifest/project/CODEBASE_MAP.md
       - .rcos/manifest/project/CURRENT_BASELINE.md
       - .rcos/manifest/project/module_index.yaml
       - .rcos/manifest/project/PROJECT_ROADMAP.md
       - 如项目使用 DNA 机制，则包括 .rcos/manifest/project/PROJECT_RCOS_EVOLUTION.md
       - 如合适，也包括 onboarding / collaboration / maintenance 相关 project files

    8. 要求 Codex 在需要时建立初始代码结构和最小 scaffold
    9. 要求 Codex 区分：
       - confirmed facts
       - working assumptions
       - open questions
    10. 要求 Codex 使用最小必要上下文，不静默扩 scope
    11. 要求 Codex 在 non-trivial 工作中遵守：
       - Scope Check
       - Context Summary
       - Change Intent
       - Change Plan
       - 等待确认后再实施
    12. 要求 Codex 在 bootstrap 过程中把 .rcos_examples/ 仅视为 example seed / reference，不能把其中的 project-specific 内容当成当前项目事实
    13. 如果 bootstrap 过程中形成了可复用的 RCOS 改进，要要求 Codex：
       - 先在当前项目内稳定该实践
       - 区分项目内实践与通用 RCOS DNA
       - 标记 contributor project
       - 只在我确认后才提议回流本体 RCOS
       - 不要把 contributor project 的演化误写进无关 example seed
    14. 最终输出必须是完整成品，可直接复制给 Codex 使用

    当你最终输出时，请只输出三部分：
    1. Project Summary
    2. Assumptions And Open Questions
    3. Codex RCOS New Project Bootstrap Prompt

    请注意：
    - 和我交流时请使用我明确指定的语言；如果我没有指定，不要擅自绑定一种固定语言
    - 最终生成给 Codex 的 bootstrap prompt 请用英文写；后续 conversation 的工作语言只在我明确指定时才写入 prompt
    - 你的目标不是替代 Codex，而是为 Codex 生成一份高质量、边界清晰、可直接执行的 bootstrap prompt
    - 如果我的 idea 还很模糊，请先帮助我把它收敛清楚
    - 如果项目已经使用了最新本体 RCOS，请让生成给 Codex 的 prompt 优先兼容最新的 Roadmap / DNA / release cadence 规则

    如果你理解了，请先开始第一轮项目澄清，并先问我最关键的几个问题。
