# RCOS 新对话 Onboarding 指南

English version: [RCOS_New_Conversation_Onboarding_Guide.md](./RCOS_New_Conversation_Onboarding_Guide.md)

这份指南适用于这样一种情况：项目已经完整完成 RCOS bootstrap，项目级 RCOS context 已经生成并对齐，现在你希望在一个新的 coding agent conversation 中，仅通过读取已有的 RCOS 文件，就快速恢复工作上下文。

常见使用场景：

- 旧 conversation 快到 token 或上下文上限了
- 当前 conversation 被 compact 过，希望刷新完整项目记忆
- 想开一个干净的新 conversation，而不依赖旧对话里的残留记忆
- 希望 coding agent 先重新锚定仓库真相层，再继续后续工作

这不是 bootstrap 指南。它默认项目已经有可用的 RCOS 协作层。

## 1. 先确认项目已经有可用的 RCOS context

只有当仓库里已经存在稳定的 RCOS context 层时，才适合使用这份指南，尤其是：

- `.rcos/manifest/project/PROJECT_BACKGROUND.md`
- `.rcos/manifest/project/PROJECT_STATUS.md`
- `.rcos/manifest/project/PROJECT_ASSUMPTIONS.md`
- `.rcos/manifest/project/CODEBASE_MAP.md`
- `.rcos/manifest/project/CURRENT_BASELINE.md`
- `.rcos/manifest/project/module_index.yaml`
- `.rcos/manifest/project/PROJECT_ONBOARDING_PROMPT.md`

如果项目还启用了较新的 RCOS 层，还可能包括：

- `.rcos/manifest/project/PROJECT_ROADMAP.md`
- `.rcos/manifest/project/PROJECT_RCOS_EVOLUTION.md`

如果这些文件还不存在，或者明显陈旧，应先回到 bootstrap 或 maintenance 流程，而不是直接做新对话刷新。

## 2. 优先从专门的新对话 onboarding prompt 开始

多数情况下，主入口就是：

- `.rcos/prompts/NEW_CONVERSATION_ONBOARDING_PROMPT.md`

这个 prompt 正是为这种 handoff 场景设计的：让新 conversation 先读取项目内已有的 onboarding 材料与规则文件，重建工作上下文，输出总结，然后停下来等待下一步任务。

如果刷新完成后还要继续日常开发，可以再配合：

- `.rcos/prompts/DAILY_ROUTINE_PROMPT.md`

## 3. 一个好的刷新过程应该做到什么

一个好的 RCOS 新对话刷新，应当让 coding agent：

- 先读取项目 onboarding 文件和核心规则文件
- 恢复它应该遵守的协作 workflow
- 总结项目用途、当前状态和可能的下一工作区
- 区分 confirmed facts 和 assumptions / 未验证点
- 不要假装自己记得仓库真相层以外的旧对话细节
- 在完成 context rebuild 后停下来等待下一步任务

这里的目标不是恢复每一条历史聊天细节，而是恢复项目真相层和协作纪律。

## 4. 推荐的用户操作方式

当你要开启一个新的 coding-agent conversation 时：

1. 新开一个干净的 conversation
2. 粘贴 `.rcos/prompts/NEW_CONVERSATION_ONBOARDING_PROMPT.md`
3. 如果有需要，再补一句很短的说明，例如：
   - 上一个 conversation 到了 token 上限
   - 上一个 conversation 被 compact 了
   - 我想让你先从 RCOS 文件重新刷新完整上下文
4. 让 agent 先完成 onboarding refresh
5. 在它总结完之前，不要急着直接下实现任务

## 5. 在进入下一任务前，你应当期待看到什么

在你继续进入实现工作之前，一个好的 onboarding refresh 通常应当返回一段简洁但有信息量的总结，至少包括：

- 这个仓库里 RCOS 大概是怎么工作的
- 它理解自己需要遵守哪些 workflow 或 approval 规则
- 这个项目是做什么的
- 当前 baseline / status 大概是什么
- 哪些内容看起来是从文件里确认过的事实
- 哪些仍像 assumptions 或 open questions

如果这段总结过于空泛、过度自信，或者明显跳过了关键文件，最好先修正刷新结果，再进入下一步。

## 6. 可直接复制给 coding agent 的 prompt

如果你不想再经过单独的准备步骤，可以直接把下面这段贴进一个新的 coding-agent conversation。

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
