# RCOS Bootstrap Pack

一个用于在新项目或既有代码仓库中快速引入 RCOS（Repository Context Operating System）的可复用资产仓库。

这个仓库的目标不是承载某个具体业务系统，而是提供一套可复制、可解压、可扩展的 RCOS 基础设施，包括：

- RCOS 通用模板
- project-specific RCOS bootstrap 提示词
- 新 conversation onboarding 提示词
- 日常协作 prompt
- 既有代码库补建 RCOS 的 prompt 与 checklist
- 一个可直接解压到新项目目录中的 bootstrap pack
- 一个成功项目的 example seed，供 AI 参考结构与写法

## Table Of Contents

- [仓库用途](#仓库用途)
- [适用场景](#适用场景)
- [主要内容](#主要内容)
- [目录结构](#目录结构)
- [推荐使用方式](#推荐使用方式)
- [新项目初始化](#新项目初始化)
- [既有代码库补建 RCOS](#既有代码库补建-rcos)
- [新 Conversation Onboarding](#新-conversation-onboarding)
- [Bootstrap Pack 与 Example Seed](#bootstrap-pack-与-example-seed)
- [Prompt 导航](#prompt-导航)
- [维护建议](#维护建议)

## 仓库用途

这个仓库用于沉淀一套通用 RCOS 协作资产，帮助团队在以下场景中更稳定地使用 AI：

- 为新项目建立最初的 RCOS 结构
- 为已有代码库补建 RCOS project-specific context
- 在新的 AI conversation 中快速完成 onboarding
- 在日常协作中维持 plan-before-code、最小 scope、authority 对齐和 RCOS 文档同步

## 适用场景

这套资产主要适用于三类工作：

1. 新项目 bootstrap
   适合一个全新的 repo，需要同时初始化代码和 `.rcos/manifest/project/*`

2. 既有代码库接入 RCOS
   适合一个已经有代码、文档和历史包袱的仓库，需要分阶段扫描并补建 project-specific RCOS 文件

3. 新 conversation 接管已有项目
   适合上下文有限、需要快速让 AI 读规则、读 project context、形成稳定协作方式

## 主要内容

本仓库一般会包含这些资产：

- `.rcos/manifest/templates/`
  RCOS 通用模板与规则真相源

- `.rcos/prompts/`
  可直接复制到对话中的实用 prompt

- `.cursor/rules/`
  本地 agent 行为约束，例如 approval gate

- `rcos_bootstrap_pack_with_examples.zip`
  可直接解压进新项目目录的 bootstrap pack

- `.rcos_examples/`
  成功项目的 example seed，只作范例参考，不是当前项目的事实来源

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
- `.rcos/manifest/project/` 是当前项目的 project-specific truth layer
- `.rcos/prompts/` 是实际使用时最方便复制的 prompt 集合
- `.rcos_examples/` 是示例项目目录，只能作为 example seed

## 推荐使用方式

推荐优先从这两个文件开始：

- `.rcos/prompts/BOOTSTRAP_PACK_USAGE_NOTE.md`
- `.rcos/prompts/PROMPT_CATALOG.md`

前者告诉你 bootstrap pack 该怎么解压和使用，后者告诉你不同场景该选哪个 prompt。

## 新项目初始化

如果你面对的是一个全新的项目仓库，推荐流程是：

1. 准备项目目标、技术方向、初始功能范围
2. 参考：
   - `.rcos/prompts/NEW_PROJECT_BOOTSTRAP_MATERIALS_CHECKLIST.md`
3. 在新 conversation 中使用：
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
3. 在一个专门的新 conversation 中使用：
   - `.rcos/prompts/EXISTING_CODEBASE_RCOS_BOOTSTRAP_PROMPT.md`

这类会话的重点不是立即开发功能，而是：

- 分阶段扫描代码
- 区分 confirmed facts / working assumptions / open questions
- 在扫描过程中持续向工程师确认关键事实
- 最终生成或更新 project-specific RCOS 文件

## 新 Conversation Onboarding

如果项目已经有完整的 `.rcos/manifest/project/*`，而你只是要在新 conversation 中快速接管它，优先使用：

- `.rcos/prompts/NEW_CONVERSATION_ONBOARDING_PROMPT.md`

如果还要继续日常开发，则可以配合：

- `.rcos/prompts/DAILY_ROUTINE_PROMPT.md`

## Bootstrap Pack 与 Example Seed

`rcos_bootstrap_pack_with_examples.zip` 的设计目标是：

- 让你把一套可用的 RCOS 基础设施直接解压进新项目目录
- 同时附带一个成功项目的 example seed，帮助 AI 参考结构和写法

关键原则：

- 活跃的 `.rcos/manifest/project/*` 必须属于当前项目
- `.rcos_examples/<seed-project>/` 只能作为 example seed
- example seed 只能帮助 AI 学习：
  - 目录组织方式
  - prompt 写法
  - RCOS project files 的粒度与风格
  - 协作约束如何落盘

AI 不应直接继承 example seed 中的：

- 项目名称
- 产品目标
- assumptions
- codebase map
- module authority
- 项目状态

## Prompt 导航

如果不确定该用哪个 prompt，优先看：

- `.rcos/prompts/PROMPT_CATALOG.md`

通常可以这样选：

- 新项目初始化：
  `NEW_PROJECT_RCOS_BOOTSTRAP_PROMPT.md`

- 新项目复杂初始化：
  `NEW_PROJECT_RCOS_BOOTSTRAP_PROMPT_VERBOSE.md`

- 已有码库补建 RCOS：
  `EXISTING_CODEBASE_RCOS_BOOTSTRAP_PROMPT.md`

- 新 conversation onboarding：
  `NEW_CONVERSATION_ONBOARDING_PROMPT.md`

- 日常任务协作：
  `DAILY_ROUTINE_PROMPT.md`

- RCOS 审计 / guard 失败修复：
  `SELF_HEAL_PROMPT.md`

## 维护建议

如果你把这个仓库作为长期维护的 RCOS 资产仓库，建议保持以下习惯：

- 新增 prompt 时同步更新 `PROMPT_CATALOG.md`
- 调整 bootstrap pack 结构时同步更新 `BOOTSTRAP_PACK_USAGE_NOTE.md`
- 如果新增了新的 bootstrap 场景，同时补：
  - 一个 prompt
  - 一个 checklist
  - 一段 usage note
- 始终区分：
  - 通用模板
  - 当前项目 truth layer
  - example seed

这样可以避免 RCOS 资产逐渐堆积后变得难以使用。

