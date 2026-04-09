# RCOS 新对话接管指南

英文版：[RCOS_New_Conversation_Onboarding_Guide.md](./RCOS_New_Conversation_Onboarding_Guide.md)

这份指南适用于这样一种情况：项目已经完整完成 RCOS 引入，项目级 RCOS 上下文已经生成并对齐，现在你希望在一个新的编程agent对话中，仅通过读取已有的 RCOS 文件，就快速恢复工作上下文。

常见使用场景：

- 旧对话快到上下文上限了
- 当前对话被压缩过，希望刷新完整项目记忆
- 想开一个干净的新对话，而不依赖旧对话里的残留记忆
- 希望编程agent先重新锚定仓库真相层，再继续后续工作

这不是引入指南。它默认项目已经有可用的 RCOS 协作层。

## 目录

- [1. 先确认项目已经有可用的 RCOS 上下文](#1-先确认项目已经有可用的-rcos-上下文)
- [2. 优先从专门的新对话接管提示词开始](#2-优先从专门的新对话接管提示词开始)
- [3. 一个好的刷新过程应该做到什么](#3-一个好的刷新过程应该做到什么)
- [4. 推荐的用户操作方式](#4-推荐的用户操作方式)
- [5. 在进入下一任务前，你应当期待看到什么](#5-在进入下一任务前你应当期待看到什么)
- [6. 可直接复制给编程agent的提示词](#copy-ready-coding-agent-prompt)

## 1. 先确认项目已经有可用的 RCOS 上下文

只有当仓库里已经存在稳定的 RCOS 上下文层时，才适合使用这份指南，尤其是：

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

如果这些文件还不存在，或者明显陈旧，应先回到引入或维护流程，而不是直接做新对话刷新。

## 2. 优先从专门的新对话接管提示词开始

多数情况下，主入口就是：

- `.rcos/prompts/NEW_CONVERSATION_ONBOARDING_PROMPT.md`

这个提示词正是为这种交接场景设计的：让新对话先读取项目内已有的接管材料与规则文件，重建工作上下文，输出总结，然后停下来等待下一步任务。

如果刷新完成后还要继续日常开发，可以再配合：

- `.rcos/prompts/DAILY_ROUTINE_PROMPT.md`

## 3. 一个好的刷新过程应该做到什么

一个好的 RCOS 新对话刷新，应当让编程agent：

- 先读取项目接管文件和核心规则文件
- 恢复它应该遵守的协作工作流程
- 总结项目用途、当前状态和可能的下一工作区域
- 区分已确认事实和假设 / 未验证点
- 不要假装自己记得仓库真相层以外的旧对话细节
- 在完成上下文重建后停下来等待下一步任务

这里的目标不是恢复每一条历史聊天细节，而是恢复项目真相层和协作纪律。

## 4. 推荐的用户操作方式

当你要开启一个新的编程agent对话时：

1. 新开一个干净的对话
2. 粘贴 `.rcos/prompts/NEW_CONVERSATION_ONBOARDING_PROMPT.md`
3. 如果有需要，再补一句很短的说明，例如：
   - 上一个对话到了上下文上限
   - 上一个对话被压缩了
   - 我想让你先从 RCOS 文件重新刷新完整上下文
4. 让agent先完成接管刷新
5. 在它总结完之前，不要急着直接下实现任务

## 5. 在进入下一任务前，你应当期待看到什么

在你继续进入实现工作之前，一个好的接管刷新通常应当返回一段简洁但有信息量的总结，至少包括：

- 这个仓库里 RCOS 大概是怎么工作的
- 它理解自己需要遵守哪些工作流程或确认规则
- 这个项目是做什么的
- 当前基础状态 / 项目状态大概是什么
- 哪些内容看起来是从文件里确认过的事实
- 哪些仍像假设或待确认问题

如果这段总结过于空泛、过度自信，或者明显跳过了关键文件，最好先修正刷新结果，再进入下一步。

<a id="copy-ready-coding-agent-prompt"></a>

## 6. 可直接复制给编程agent的提示词

如果你不想再经过单独的准备步骤，可以直接把下面这段贴进一个新的编程agent对话。

    这个仓库采用 RCOS（Repository Context Operating System）方法来管理。

    当前任务是一个“新对话接管与上下文刷新任务”。
    这不是新项目引入任务。
    这也不是既有代码库引入 RCOS 的任务。

    这个仓库已经有可用的 RCOS 上下文层。
    你的工作，是在任何新的实现开始之前，先通过现有 RCOS 文件重建工作上下文。

    请先定位并读取这些文件（如果存在）：

    - `.rcos/manifest/project/PROJECT_ONBOARDING_PROMPT.md`
    - `.cursor/rules/rcos_enforced.md`
    - `.cursor/rules/rcos_approval_gate.md`

    然后遵循 onboarding prompt 自身规定的读取顺序，把它点名要求的 project-specific RCOS files 继续读完。

    请把这些文件视为当前仓库的 collaboration truth layer。

    不要一上来就进入实现。
    不要假装自己记得先前对话里那些没有落盘的隐藏上下文。
    请从仓库里的真相层重新建立理解。

    读取完成后，在询问下一步任务之前，先做一轮验证性总结。

    这段总结必须包括：

    - 你理解这个仓库里的 RCOS 原则大概是什么
    - 你认为自己需要遵守哪些协作或确认规则
    - 这个项目是做什么的
    - 当前 project status 或 baseline 大概是什么
    - 哪些内容看起来是 confirmed facts
    - 哪些内容仍是 assumptions、含混点或值得复核的地方

    总结完之后，停下来等待我的下一步任务。

    请使用我明确指定的语言；如果我没有指定，就不要没必要地强行绑定某一种语言。
