# Prompt Catalog

这份文档用于汇总当前仓库中可用的 prompt / prompt-like 文件，方便快速选择合适的提示词。

说明：
- `.rcos/prompts/` 下的文件通常更适合直接手动复制到新 conversation 中使用。
- `.rcos/manifest/project/` 下的 prompt 文件通常是当前项目的权威协作入口。
- `.rcos/manifest/templates/` 下的 prompt 文件通常是 RCOS 通用模板或元规则，不一定适合直接原样粘贴，但很适合作为上层真相源。

---

## 一、最常用 Prompt

### 1. 新 conversation 接管当前项目
- 路径：`.rcos/prompts/NEW_CONVERSATION_ONBOARDING_PROMPT.md`
- 用途：在一个新的 conversation 中快速让 AI 接管当前 repo，并按 RCOS 方式完成 onboarding。
- 适用场景：
  - 新开 Codex conversation
  - 新开其他 AI 对话，但希望它先读当前 repo 的 RCOS 文件
- 使用方式：
  - 直接复制文件中的正文到对话框
  - 或手动输入一句，要求 AI 先读取这个文件
- 特点：
  - 短
  - 适合直接粘贴
  - 依赖 AI 继续读取 `PROJECT_ONBOARDING_PROMPT.md`

### 2. 当前项目完整 onboarding 真相源
- 路径：`.rcos/manifest/project/PROJECT_ONBOARDING_PROMPT.md`
- 用途：作为当前 `news_agent_mvp` 项目的完整 onboarding 指南。
- 适用场景：
  - 新 conversation 初始化
  - 需要向 AI 明确当前项目事实、近期重要行为和协作规则
- 使用方式：
  - 不一定直接全文粘贴
  - 更常见的做法是让 AI “先读取并遵守这个文件”
- 特点：
  - 权威
  - 信息完整
  - 已包含 approval gate、近期日志系统与 `/log` archive 浏览等关键事实

### 3. 当前项目日常协作 prompt
- 路径：`.rcos/manifest/project/PROJECT_COLLABORATION_PROMPT.md`
- 用途：约束 AI 在当前项目中的日常协作行为。
- 适用场景：
  - 已完成 onboarding 后的日常开发
  - 需要强调 authority、plan-before-code、RCOS update awareness
- 使用方式：
  - 通常作为 AI 需要读取的项目协作规范文件
  - 不一定作为“手动贴入 prompt”的第一选择
- 特点：
  - 偏当前项目协作 contract
  - 对 authority 和输出顺序要求更细

### 4. 日常任务短 prompt
- 路径：`.rcos/prompts/DAILY_ROUTINE_PROMPT.md`
- 用途：在当前项目中快速发起一个普通任务。
- 适用场景：
  - 已知 AI 已接管当前项目
  - 你只想给出一个任务，并提醒它遵守 plan-before-code
- 使用方式：
  - 把文件内容复制后，在最后补上当前任务
- 特点：
  - 简短
  - 适合日常重复使用

---

## 二、新项目初始化 Prompt

### 5. 新项目 bootstrap 短版 prompt
- 路径：`.rcos/prompts/NEW_PROJECT_RCOS_BOOTSTRAP_PROMPT.md`
- 用途：让 AI 在一个全新 repo 中同时完成：
  - initial code / scaffold
  - RCOS project-specific context bootstrap
- 适用场景：
  - 你刚新建一个 repo
  - 想在新 conversation 中初始化代码和 `.rcos/manifest/project/*`
- 使用方式：
  - 直接复制到新 conversation
  - 再补充你的项目目标、技术栈、功能范围
- 特点：
  - 简洁
  - approval-first
  - 明确要求 RCOS 文档和代码一起生成

### 6. 新项目 bootstrap 详细版 prompt
- 路径：`.rcos/prompts/NEW_PROJECT_RCOS_BOOTSTRAP_PROMPT_VERBOSE.md`
- 用途：和短版相同，但给出更完整的上下文和执行规则。
- 适用场景：
  - 项目重要
  - 项目复杂
  - 你担心对方 agent 不够稳
- 使用方式：
  - 直接复制到新 conversation
- 特点：
  - 更稳
  - 解释更完整
  - 更适合高风险初始化任务

### 7. 新项目 bootstrap 材料清单
- 路径：`.rcos/prompts/NEW_PROJECT_BOOTSTRAP_MATERIALS_CHECKLIST.md`
- 用途：帮助你在新项目启动前准备最小但足够的输入材料。
- 适用场景：
  - 你还没开始和 AI 对话
  - 你不确定该先准备哪些材料
- 使用方式：
  - 先照着清单准备材料
  - 然后再搭配 `NEW_PROJECT_RCOS_BOOTSTRAP_PROMPT.md` 或 verbose 版使用
- 特点：
  - 不是主 prompt
  - 是 prompt 的配套输入准备指南

### 8. Bootstrap pack 使用说明
- 路径：`.rcos/prompts/BOOTSTRAP_PACK_USAGE_NOTE.md`
- 用途：说明如何使用 `rcos_bootstrap_pack_with_examples.zip`，以及如何正确对待 example seed。
- 适用场景：
  - 你把整个 bootstrap pack 解压进一个全新项目目录之后
  - 你希望 AI 能参考旧项目范例，但不污染新项目事实来源
- 使用方式：
  - 可直接阅读
  - 也可以在新 conversation 中让 AI 一并读取
- 特点：
  - 明确区分活跃路径和 example 路径
  - 自带一段可直接复制的启动文本

### 9. 既有代码库接入 RCOS prompt
- 路径：`.rcos/prompts/EXISTING_CODEBASE_RCOS_BOOTSTRAP_PROMPT.md`
- 用途：在一个已经有代码和文档的仓库中，专门开新 conversation 分阶段扫描并建立 project-specific RCOS context。
- 适用场景：
  - 老仓库补建 RCOS
  - 已有代码库需要建立 `./rcos/manifest/project/*`
  - 需要 AI 在扫描过程中持续和人类工程师确认事实与 assumptions
- 使用方式：
  - 直接复制到新 conversation
  - 再补上 README、目录树、入口文件、已有文档等初始材料
- 特点：
  - 强调 phased scanning
  - 强调 confirmed facts / working assumptions / open questions
  - 不把这类会话误当作普通功能开发

### 10. 既有代码库接入 RCOS 材料清单
- 路径：`.rcos/prompts/EXISTING_CODEBASE_RCOS_BOOTSTRAP_MATERIALS_CHECKLIST.md`
- 用途：帮助你在一个已有代码和文档的仓库中补建 RCOS 前，先准备最小但足够的输入材料。
- 适用场景：
  - 老仓库补建 RCOS
  - 想先整理 README、目录树、入口文件、已有文档、工程师口头知识
- 使用方式：
  - 先照着清单准备输入
  - 再搭配 `EXISTING_CODEBASE_RCOS_BOOTSTRAP_PROMPT.md` 使用
- 特点：
  - 是 existing-codebase bootstrap 的配套 checklist
  - 重点帮助 AI 分阶段扫描并持续向工程师确认事实

---

## 三、修复 / 审计类 Prompt

### 11. Self-heal prompt
- 路径：`.rcos/prompts/SELF_HEAL_PROMPT.md`
- 用途：当 RCOS audit / patch guard / 一致性检查失败时，引导 AI 做最小修复。
- 适用场景：
  - 触发 guard failure
  - 出现越权修改、scope 失控、RCOS 文档未同步等问题
- 使用方式：
  - 把 guard / audit 输出粘贴到这个 prompt 里
- 特点：
  - 强调最小修复
  - 强调不要扩大 scope
  - 优先恢复 RCOS 一致性

---

## 四、模板 / 元 Prompt

### 12. Change plan 模板
- 路径：`.rcos/manifest/templates/CHANGE_PLAN_PROMPT.md`
- 用途：定义非 trivial 任务在实现前必须先输出的计划结构。
- 适用场景：
  - 设计 RCOS 工作流
  - 检查 AI 是否遵守 plan-before-code
- 使用方式：
  - 更适合作为 AI 要先读取的规则文件
  - 也可以在必要时手动贴给 AI 强化约束
- 核心结构：
  - Scope Check
  - Context Summary
  - Change Intent
  - Change Plan

### 13. Project-specific RCOS bootstrap 模板
- 路径：`.rcos/manifest/templates/PROJECT_SPECIFIC_RCOS_PROMPT_UNIT.md`
- 用途：定义如何为项目生成完整 project-specific RCOS 文件。
- 适用场景：
  - 现有 repo 接入 RCOS
  - brand-new repo 初始化并同时生成 project-specific RCOS 文件
- 使用方式：
  - 更适合作为上层模板真相源
  - 可供你或 AI 派生更具体的 bootstrap prompt
- 特点：
  - 覆盖项目 bootstrap、日常协作、new-thread onboarding 三类场景

---

## 五、如何选择

### 场景 A：我只是要在当前 repo 开一个新 conversation
优先使用：
1. `.rcos/prompts/NEW_CONVERSATION_ONBOARDING_PROMPT.md`
2. `.rcos/manifest/project/PROJECT_ONBOARDING_PROMPT.md`

### 场景 B：我已经完成 onboarding，只想发一个普通开发任务
优先使用：
1. `.rcos/prompts/DAILY_ROUTINE_PROMPT.md`
2. `.rcos/manifest/project/PROJECT_COLLABORATION_PROMPT.md`

### 场景 C：我要初始化一个全新 repo，并同时生成 RCOS project-specific 文件
优先使用：
1. `.rcos/prompts/NEW_PROJECT_BOOTSTRAP_MATERIALS_CHECKLIST.md`
2. `.rcos/prompts/NEW_PROJECT_RCOS_BOOTSTRAP_PROMPT.md`
3. `.rcos/prompts/BOOTSTRAP_PACK_USAGE_NOTE.md`

如果项目更复杂，改用：
1. `.rcos/prompts/NEW_PROJECT_BOOTSTRAP_MATERIALS_CHECKLIST.md`
2. `.rcos/prompts/NEW_PROJECT_RCOS_BOOTSTRAP_PROMPT_VERBOSE.md`
3. `.rcos/prompts/BOOTSTRAP_PACK_USAGE_NOTE.md`

### 场景 D：AI 已经把 RCOS 流程搞坏了，需要最小修复
优先使用：
1. `.rcos/prompts/SELF_HEAL_PROMPT.md`

### 场景 E：我有一个已有代码仓库，想补建 RCOS
优先使用：
1. `.rcos/prompts/EXISTING_CODEBASE_RCOS_BOOTSTRAP_MATERIALS_CHECKLIST.md`
2. `.rcos/prompts/EXISTING_CODEBASE_RCOS_BOOTSTRAP_PROMPT.md`
3. `.rcos/prompts/BOOTSTRAP_PACK_USAGE_NOTE.md`
4. `.rcos/manifest/templates/PROJECT_SPECIFIC_RCOS_PROMPT_UNIT.md`

---

## 六、推荐的最小手动操作

### 当前项目新 conversation
直接贴：
- `.rcos/prompts/NEW_CONVERSATION_ONBOARDING_PROMPT.md`

### 当前项目普通任务
直接贴：
- `.rcos/prompts/DAILY_ROUTINE_PROMPT.md`
然后补“当前任务”

### 新项目初始化
先看：
- `.rcos/prompts/NEW_PROJECT_BOOTSTRAP_MATERIALS_CHECKLIST.md`

再贴：
- `.rcos/prompts/NEW_PROJECT_RCOS_BOOTSTRAP_PROMPT.md`
- 如果你是从 bootstrap pack 解压出来的，再看：
  - `.rcos/prompts/BOOTSTRAP_PACK_USAGE_NOTE.md`

复杂项目则贴：
- `.rcos/prompts/NEW_PROJECT_RCOS_BOOTSTRAP_PROMPT_VERBOSE.md`

### 既有代码仓库补建 RCOS
先看：
- `.rcos/prompts/EXISTING_CODEBASE_RCOS_BOOTSTRAP_MATERIALS_CHECKLIST.md`

直接贴：
- `.rcos/prompts/EXISTING_CODEBASE_RCOS_BOOTSTRAP_PROMPT.md`
如果是从 bootstrap pack 解压出来的，再看：
- `.rcos/prompts/BOOTSTRAP_PACK_USAGE_NOTE.md`

---

## 七、维护原则

如果未来新增 prompt，建议在这里同步补充：
- 路径
- 作用
- 适用场景
- 是否适合直接复制粘贴
- 与哪些 prompt / template 配合使用

这样可以避免 prompt 越来越多后难以查找和误用。
