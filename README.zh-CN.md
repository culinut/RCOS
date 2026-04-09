# RCOS 启动套装

英文版：[README.md](./README.md)

引导AI去读什么，才能更好地控制它做什么。

## 面向 AI 协作软件开发的操作系统

RCOS（Repository Context Operating System）是一套面向人类与通用 AI 协作开发的“仓库上下文操作系统”。它并不是为了替代工程判断，而是希望通过最小必要上下文、清晰的职责边界，以及先规划后实施的协作流程，持续降低责任漂移、意图丢失、注意力扩散和验证缺口。

它还有一个重要价值：大量工作上下文可以由 AI 主动生成并持续维护。这既能降低人工编写和维护文档的成本，也能让 AI 在维护这些上下文的过程中不断整理、刷新并稳定自己对代码库的感知。

这个仓库收录了一组可复用资产，可帮助团队在新项目或既有代码仓库中快速引入 RCOS。

这个仓库的目标不是承载某个具体业务系统，而是提供一套可复制、可解压、可扩展的 RCOS 基础设施，包括：

- RCOS 通用模板
- 新项目引导提示词
- 新对话接管提示词
- 日常协作提示词
- 既有代码库补建 RCOS 的提示词与检查清单
- 一个可直接解压到新项目目录中的 RCOS 套装
- 一个成功项目的示例种子，供 AI 参考结构与写法

RCOS 现在还支持一套 DNA 化的演化模型：

- 租户项目可以产出可复用的 RCOS DNA
- 主 RCOS、示例种子和发布产物采用不同同步节奏
- 上行同步与下行吸收都应显式进行，而不是默认自动发生

## 目录

- [使用前后对比](#使用前后对比)
- [RCOS 简介](#rcos-简介)
- [RCOS 为什么存在](#rcos-为什么存在)
- [快速开始](#快速开始)
- [示例工作流](#示例工作流)
- [RCOS 不是什么](#rcos-不是什么)
- [仓库用途](#仓库用途)
- [适用场景](#适用场景)
- [主要内容](#主要内容)
- [目录结构](#目录结构)
- [推荐使用方式](#推荐使用方式)
- [新项目引入 RCOS](#新项目引入-rcos)
- [既有代码库补建 RCOS](#既有代码库补建-rcos)
- [新对话接管](#新对话接管)
- [启动套装与示例种子](#启动套装与示例种子)
- [提示词导航](#提示词导航)
- [维护建议](#维护建议)
- [许可证](#许可证)

## 使用前后对比

如果你曾经觉得 AI 写代码一开始很好用，但推进到某个阶段后突然开始失控，RCOS 就是为这种时刻设计的。

没有 RCOS 时：

- AI 会扫描仓库里大段不相关的代码，逐渐失去焦点
- 上下文会在不同对话之间漂移
- 修改容易冲突，或者重复实现已有逻辑
- 文档很快变得不再可靠

有了 RCOS 之后：

- AI 只读取真正相关的文件
- 每个非简单变更都从显式规划开始
- 范围会保持在受控范围内
- 代码和上下文能长期保持同步

RCOS 把 AI 写代码从“靠猜理解仓库”变成了一套受控的人机协作系统。

## RCOS 简介

RCOS 关注的不是“让 AI 多读代码”，而是“让 AI 在正确的边界内读取足够少、但足够关键的上下文”。

在 RCOS 里，上下文不只是给 AI 读取的材料，也是 AI 用来主动生成、维护并持续刷新自身代码库理解的一层协作基础设施。

RCOS 不只是一些提示词的集合，而是一种组织人类与 AI 协作处理代码的方式。

RCOS 进一步定义了上下文应该如何组织、注意力应该如何分配，以及在 AI 参与的前提下，代码改动应该如何被引入代码库。

它通常通过以下机制工作：

- 先读取最小必要上下文，而不是默认扫描整个仓库
- 用项目级上下文文件声明当前项目的事实、假设与模块职责归属
- 用先规划后实施的工作流，让 AI 先明确范围、意图和变更计划
- 在代码变更后同步维护 RCOS 文档，避免代码与上下文层逐渐失配

## RCOS 为什么存在

如果没有像 RCOS 这样的系统，AI 协作开发很容易出现这些问题：

- 模型扫描了过多无关代码，逐渐失去焦点
- 重要的项目假设只存在于隐性共识里，在不同会话中逐渐变得不一致
- 不同 AI 会话产出彼此冲突的修改，或重复实现已有逻辑
- 实施过程中范围悄悄扩张
- 文档和代码逐渐脱节，最后不再可信

RCOS 的做法，是把上下文变成一层显式的、窄范围的、并且与代码一同持续维护的协作基础设施。

它不依赖模型自行“猜懂仓库”，而是明确规定上下文应当如何被组织、选择和更新。

## 快速开始

1. 将 `.rcos/` 和 `.cursor/` 复制到你的项目中。
2. 在你的开发环境里打开项目。
3. 新开一个 AI 对话。
4. 从 `.rcos/prompts/` 中选择并粘贴合适的入门提示词。
5. 提供当前任务和最小必要的项目文件。
6. 按 RCOS 工作流推进：先规划 -> 再确认 -> 后实施 -> 最后更新上下文。

这样你就得到了一套带有显式上下文和审批门禁的 AI 协作闭环。

## 示例工作流

用户：
“给 news retrieval 模块加缓存。”

AI（RCOS）：
1. 范围检查
2. 上下文摘要
3. 变更意图
4. 变更计划

用户：
“批准。”

AI：
- 实施最小变更集
- 验证改动
- 如有需要，同步更新相关 RCOS 上下文文件

这个闭环会让实现过程始终处于受控状态，并与项目上下文保持一致。

RCOS 会把 AI 从单纯的代码生成器，变成一个受控的协作参与者。

## RCOS 不是什么

RCOS 不是：

- 一个用于构建 AI 智能体的框架
- 一个代码生成库
- 一个版本控制系统的替代品
- 一个能保证模型永远行为正确的机制

RCOS 是：

- 一套组织和约束 AI 协作的系统
- 一种让项目上下文显式化、可维护化的方法
- 一种长期保持代码与上下文对齐的协作纪律
- 一套可复用的 AI 协作提示词与流程基础设施

## 仓库用途

这个仓库用于沉淀一套通用 RCOS 协作资产，帮助团队在以下场景中更稳定地使用 AI：

- 为新项目建立最初的 RCOS 结构
- 为已有代码库补建 RCOS 项目级上下文
- 在新的 AI 对话中快速完成接管
- 在日常协作中维持先规划后写代码、最小范围、职责对齐和 RCOS 文档同步

## 适用场景

这套资产主要适用于三类工作：

1. 新项目引入 RCOS
   适合一个全新的代码仓库，需要同时建立代码骨架和 `.rcos/manifest/project/*`

2. 既有代码库接入 RCOS
   适合一个已经有代码、文档和历史包袱的仓库，需要分阶段扫描并补建项目级 RCOS 文件

3. 新对话接管已有项目
   适合上下文有限、需要快速让 AI 读规则、读项目上下文、形成稳定协作方式

## 主要内容

本仓库一般会包含这些资产：

- `.rcos/manifest/templates/`
  RCOS 通用模板与规则真相源

- `.rcos/prompts/`
  可直接复制到对话中的实用提示词

- `.cursor/rules/`
  本地 agent 行为约束，例如 approval gate

- `rcos_bootstrap_pack_with_examples.zip`
  可直接解压进新项目目录的 RCOS 套装

- `.rcos_examples/`
  成功项目的示例种子，只作范例参考，不是当前项目的事实来源

## 目录结构

一个典型的结构会类似于：

```text
.rcos/
  manifest/
    templates/
    project/
  prompts/

.cursor/
  rules/

.rcos_examples/
  <seed-project>/

rcos_bootstrap_pack_with_examples.zip
```

说明：

- `.rcos/manifest/templates/` 是通用模板层
- `.rcos/manifest/project/` 是当前项目的项目级真相层
- `.rcos/prompts/` 是实际使用时最方便复制的提示词集合
- `.rcos_examples/` 是示例项目目录，只能作为示例种子

## 推荐使用方式

推荐优先从这些入口开始：

- `.rcos/prompts/BOOTSTRAP_PACK_USAGE_NOTE.md`
- `.rcos/prompts/PROMPT_CATALOG.md`
- [新项目导引](./RCOS_Project_Startup_Guide.zh-CN.md)
- [既有代码库引入指南](./RCOS_Existing_Codebase_Adoption_Guide.zh-CN.md)
- [新对话接管指南](./RCOS_New_Conversation_Onboarding_Guide.zh-CN.md)
- [环境配置辅助指南](./RCOS_Environment_Setup_Helper.zh-CN.md)（可选）

前者告诉你这套 RCOS 文件该怎么解压和使用，后者告诉你不同场景该选哪个提示词。新项目导引面向全新的仓库，既有代码库引入指南面向已经有代码和历史上下文的仓库，新对话接管指南面向已经完成 RCOS 引入、但需要在新对话中快速刷新上下文的场景。环境配置辅助指南则是按需查看的可选材料，适合想在进入正式 RCOS 流程前先获得更多环境配置帮助的读者。

## 新项目引入 RCOS

如果你面对的是一个全新的项目仓库，推荐流程是：

1. 准备项目目标、技术方向、初始功能范围
2. 参考：
   - `.rcos/prompts/NEW_PROJECT_BOOTSTRAP_MATERIALS_CHECKLIST.md`
3. 在新对话中使用：
   - `.rcos/prompts/NEW_PROJECT_RCOS_BOOTSTRAP_PROMPT.md`
4. 如果项目更复杂，改用：
   - `.rcos/prompts/NEW_PROJECT_RCOS_BOOTSTRAP_PROMPT_VERBOSE.md`

目标通常是：

- 初始化代码结构
- 引入 RCOS 通用模板
- 同时生成完整的 `.rcos/manifest/project/*`

## 既有代码库补建 RCOS

如果你面对的是一个已经存在代码和文档的仓库，推荐流程是：

1. 准备 README、目录树、入口文件和工程师口头背景
2. 参考：
   - `.rcos/prompts/EXISTING_CODEBASE_RCOS_BOOTSTRAP_MATERIALS_CHECKLIST.md`
   - [RCOS_Existing_Codebase_Adoption_Guide.zh-CN.md](./RCOS_Existing_Codebase_Adoption_Guide.zh-CN.md)
3. 在一个专门的新对话中使用：
   - `.rcos/prompts/EXISTING_CODEBASE_RCOS_BOOTSTRAP_PROMPT.md`

这类会话的重点不是立即开发功能，而是：

- 分阶段扫描代码
- 区分已确认事实 / 工作假设 / 待确认问题
- 在扫描过程中持续向工程师确认关键事实
- 最终生成或更新项目级 RCOS 文件

## 新对话接管

如果项目已经有完整的 `.rcos/manifest/project/*`，而你只是要在新对话中快速接管它，优先使用：

- `.rcos/prompts/NEW_CONVERSATION_ONBOARDING_PROMPT.md`
- [新对话接管指南](./RCOS_New_Conversation_Onboarding_Guide.zh-CN.md)

如果还要继续日常开发，则可以配合：

- `.rcos/prompts/DAILY_ROUTINE_PROMPT.md`

这份指南尤其适合：上一个对话到了上下文上限、被压缩过，或者你希望让新的编程agent先从仓库真相层重新锚定上下文，再继续后续工作。

## 启动套装与示例种子

`rcos_bootstrap_pack_with_examples.zip` 的设计目标是：

- 让你把一套可用的 RCOS 基础设施直接解压进新项目目录
- 同时附带一个成功项目的示例种子，帮助 AI 参考结构和写法

关键原则：

- 活跃的 `.rcos/manifest/project/*` 必须属于当前项目
- `.rcos_examples/<种子项目>/` 只能作为示例种子
- 示例种子只能帮助 AI 学习：
  - 目录组织方式
  - 提示词写法
  - RCOS project files 的粒度与风格
  - 协作约束如何落盘

AI 不应直接继承示例种子中的：

- 项目名称
- 产品目标
- 假设
- codebase map
- module authority
- 项目状态

示例种子也可以示范：

- 把路线图规划 / 跟踪作为正式的项目级 RCOS 文件
- 贡献项目如何把可复用的 RCOS 改进提议同步回主 RCOS 仓库

但示例种子仍然只是延迟提升的成功样本，不是高频 DNA 层。

## 提示词导航

如果不确定该用哪个提示词，优先看：

- `.rcos/prompts/PROMPT_CATALOG.md`

通常可以这样选：

- 新项目初始化：
  `NEW_PROJECT_RCOS_BOOTSTRAP_PROMPT.md`

- 新项目复杂初始化：
  `NEW_PROJECT_RCOS_BOOTSTRAP_PROMPT_VERBOSE.md`

- 已有码库补建 RCOS：
  `EXISTING_CODEBASE_RCOS_BOOTSTRAP_PROMPT.md`

- 新对话接管：
  `NEW_CONVERSATION_ONBOARDING_PROMPT.md`

- 日常任务协作：
  `DAILY_ROUTINE_PROMPT.md`

- RCOS 审计 / guard 失败修复：
  `SELF_HEAL_PROMPT.md`

## 维护建议

如果你把这个仓库作为长期维护的 RCOS 资产仓库，建议保持以下习惯：

- 新增提示词时同步更新 `PROMPT_CATALOG.md`
- 调整启动套装结构时同步更新 `BOOTSTRAP_PACK_USAGE_NOTE.md`
- 如果新增了新的启动场景，同时补：
  - 一个提示词
  - 一个检查清单
  - 一段 usage note
- 如果某个贡献项目沉淀出了可复用的 RCOS 改进：
  - 先把它抽象成通用经验，而不是直接复制项目事实
  - 显式标记贡献项目
- 如果要同步示例种子，优先同步到与贡献项目对应的种子路径
- 不要把某个项目的 RCOS 进化误写进无关的示例种子
- 在合适时同步更新模板、提示词和示例种子
  - 未经人类确认，不要静默回流到主 RCOS 仓库
- 不要因为每一次 DNA 微调就重新打包启动压缩包
- 应把启动压缩包视为发布产物
- 只有在明确发布或经人类批准的例外发布时，才应在同一步更新种子与压缩包
- 如果某种新的项目级文件被证明长期有价值，要同时更新：
  - 模板
  - 提示词
  - 示例种子
  - 文档引用
- 始终区分：
  - 通用模板
  - 当前项目真相层
  - 示例种子

这样可以避免 RCOS 资产逐渐堆积后变得难以使用。

## 许可证

本仓库采用 MIT 许可证。你可以在遵守许可证条款的前提下自由使用、修改、分发和复用这些模板、提示词、规则与启动资产。

完整许可证文本见根目录 [LICENSE](./LICENSE)。
