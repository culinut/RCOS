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

## 6. 可选：先用对话模型准备一个更丰富的刷新 prompt

大多数情况下，这一步不是必须的。内置的 new-conversation onboarding prompt 通常已经够用。

但在下面这些情况，它仍然有帮助：

- 项目里的 RCOS 文件很多，你希望刷新过程更有引导性
- 上一个 conversation 结束得比较混乱
- 你希望下一个 coding-agent conversation 在开始工作前先做一轮自我校验

在这些情况下，可以先让一个对话模型帮你生成一份稍微更丰富的 onboarding-refresh prompt，再贴给 coding agent。

## 附录：用于准备刷新型 onboarding conversation 的元提示词

如果你希望先让对话模型帮你生成一版更强的新对话刷新 prompt，再交给 coding agent，可以把下面这段贴进去。

    你的任务不是实现代码，而是帮助我为一个新的 coding-agent conversation 准备 RCOS onboarding-refresh prompt。这个仓库已经有完整的 RCOS context 层。

    这不是一个 new-project bootstrap task。
    这不是一个 existing-codebase RCOS adoption task。
    这是一个新 conversation 的 onboarding 与 context refresh 任务。

    先给你必要的 RCOS 背景：

    RCOS（Repository Context Operating System）是一套面向人类与通用 AI 协作开发的仓库上下文操作系统。它的目标，是让 coding agent 以正确顺序读取正确且最小必要的上下文，而不是依赖大范围扫仓库，或者依赖脆弱的对话记忆。

    在 RCOS 里：
    - project-specific truth 通常沉淀在 .rcos/manifest/project/*
    - 可复用系统规则和模板通常在 .rcos/manifest/templates/*
    - 常用操作 prompt 通常在 .rcos/prompts/*
    - .rcos_examples/ 下的 example seed 只是参考材料，不是当前项目事实
    - 非 trivial 工作通常遵守：
      - Scope Check
      - Context Summary
      - Change Intent
      - Change Plan
      - 等确认
      - 再实施

    额外的当前 RCOS 预期：
    - PROJECT_ROADMAP.md 在存在时应视为正式的 project-specific RCOS 文件
    - 如果项目启用了 RCOS DNA 机制，则 PROJECT_RCOS_EVOLUTION.md、RCOS_EVOLUTION_PROTOCOL.md、RCOS_DNA_REGISTRY.yaml 也属于协作真相层
    - 新 conversation 应从仓库真相层重建理解，而不是假装记得先前对话里的隐藏上下文
    - 一个刷新过程应当先输出理解摘要，再开始真正工作

    请假设当前情况如下：
    - 仓库已经完成 RCOS bootstrap
    - project-specific RCOS 文件已经存在，并被视为当前真相层
    - 之前的 coding conversation 可能因为 token 限制、compact 或其他原因丢失了工作上下文
    - 我希望新的 coding-agent conversation 通过读取已有 RCOS 文件来恢复上下文

    你的任务是输出一份完整 prompt，供我直接贴给 coding agent。

    这份生成出来的 prompt 必须：

    1. 明确说明这是一个 RCOS 新对话 onboarding 任务，不是 bootstrap 任务
    2. 明确要求 coding agent 读取这些文件（如果存在）：
       - `.rcos/manifest/project/PROJECT_ONBOARDING_PROMPT.md`
       - `.cursor/rules/rcos_enforced.md`
       - `.cursor/rules/rcos_approval_gate.md`
       - onboarding prompt 中进一步引用的 project-specific RCOS 文件
    3. 明确要求 coding agent 把这些文件视为当前仓库的协作真相层
    4. 明确要求 coding agent 在做任何别的事之前，先遵守 onboarding prompt 自身规定的读取顺序
    5. 明确要求 coding agent 不要一上来进入实现
    6. 明确要求 coding agent 从仓库 context 刷新理解，而不是声称自己保留了先前对话记忆
    7. 明确要求 coding agent 在读取完成后，先做一轮验证性总结，再等待下一步任务

    这轮验证性总结至少应要求 coding agent 复述：

    - 它理解这个仓库中的 RCOS 原则大概是什么
    - 它认为自己需要遵守哪些协作或 approval 规则
    - 这个项目是做什么的
    - 当前 status / baseline 大概是什么
    - 哪些点看起来是 confirmed facts
    - 哪些点仍是 assumptions、含混点或值得复核的地方

    这份生成出来的 prompt 还应明确要求 coding agent 在完成这轮总结后停下来，等待我的下一步任务。

    请使用我明确指定的语言；如果我没有指定，不要没必要地强绑某种固定语言。

