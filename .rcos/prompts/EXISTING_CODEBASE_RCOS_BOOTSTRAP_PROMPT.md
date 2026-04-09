# Existing Codebase RCOS Bootstrap Prompt

```text
你现在的任务不是开发功能，而是把一个“已有代码的仓库”初始化进 RCOS，并建立完整的 project-specific RCOS context。

请把这当成一个专门的 onboarding / bootstrap conversation，而不是普通 coding task。

请先读取并严格遵守：
- `.rcos/manifest/templates/PROJECT_SPECIFIC_RCOS_PROMPT_UNIT.md`
- `.rcos/manifest/templates/META_INSTRUCTIONS.md`
- `.rcos/manifest/templates/coding_contract.md`
- `.rcos/manifest/templates/RCOS_RUNBOOK.md`
- `.rcos/manifest/templates/CHANGE_PLAN_PROMPT.md`

目标：
1. 有条理地扫描已有代码和已有文档
2. 在扫描过程中持续和人类工程师确认关键事实
3. 生成并迭代完整的 `.rcos/manifest/project/*`
4. 不要把推测写成事实

工作方式要求：

Phase 1
- 先读取已有 README、设计文档、目录树、入口文件
- 基于最小上下文输出：
  1. Scope Check
  2. Context Summary
  3. Bootstrap Intent
  4. Bootstrap Plan
- 然后停止，等待我的确认

Phase 2
- 在我确认后，按批次扫描代码
- 每一批只读取少量最关键文件
- 每批扫描后都输出：
  - Confirmed facts
  - Working assumptions
  - Open questions
  - Proposed next scan batch
- 如果功能意图、模块职责、历史遗留设计不清楚，必须主动向我提问确认

Phase 3
- 当事实足够后，生成或更新：
  - `.rcos/manifest/project/PROJECT_BACKGROUND.md`
  - `.rcos/manifest/project/PROJECT_STATUS.md`
  - `.rcos/manifest/project/PROJECT_ASSUMPTIONS.md`
  - `.rcos/manifest/project/CODEBASE_MAP.md`
  - `.rcos/manifest/project/PROJECT_ONBOARDING_PROMPT.md`
  - `.rcos/manifest/project/PROJECT_COLLABORATION_PROMPT.md`
  - `.rcos/manifest/project/PROJECT_RCOS_MAINTENANCE.md`
  - `.rcos/manifest/project/PROJECT_ROADMAP.md`
  - `.rcos/manifest/project/PROJECT_RCOS_EVOLUTION.md`
  - `.rcos/manifest/project/CURRENT_BASELINE.md`
  - `.rcos/manifest/project/module_index.yaml`

规则：
- 绝对不要把推测写成事实
- 不要一上来扫描整个 repo
- 未确认前不要大面积生成 project-specific RCOS 文件
- 不要顺手做业务代码改造，除非我明确要求
- 如果 bootstrap 过程中出现了可复用的 RCOS 改进：
  - 先把它写清楚是项目内实践还是通用经验
  - 标记 contributor project
  - 提议是否回流主 RCOS 仓库
  - 在得到我的确认前不要直接改上游 RCOS 仓库
- 如果 scope 必须扩大，必须说明：
  - 为什么
  - 要读哪些文件
  - 风险是什么

如果你理解了，请先：
1. 总结你将如何执行这次 existing codebase 的 RCOS bootstrap
2. 告诉我第一批你建议读取哪些文件
3. 停止并等待我的确认

上述 instruction 为了便于理解使用英文思维组织，但后续交流和生成请保持以中文为基础。
```
