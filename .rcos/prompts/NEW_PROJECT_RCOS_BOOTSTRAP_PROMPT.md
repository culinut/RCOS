# New Project RCOS Bootstrap Prompt

```text
你现在要初始化一个全新的项目仓库，并把它纳入 RCOS 协作体系。

请先读取并严格遵守：
- `.rcos/manifest/templates/PROJECT_SPECIFIC_RCOS_PROMPT_UNIT.md`
- `.rcos/manifest/templates/META_INSTRUCTIONS.md`
- `.rcos/manifest/templates/coding_contract.md`
- `.rcos/manifest/templates/RCOS_RUNBOOK.md`
- `.rcos/manifest/templates/CHANGE_PLAN_PROMPT.md`

你的任务有两个，而且必须一起完成：
1. 创建或脚手架化这个新项目的初始代码与目录结构
2. 同时 bootstrap 完整的 project-specific RCOS 文件到：
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

要求：
- 先输出：
  1. Scope Check
  2. Context Summary
  3. Change Intent
  4. Change Plan
- 然后停止，等待我的确认
- 在我确认前不要写代码，不要创建文件
- 缺信息时只问最小必要问题，不要猜
- 不要把 RCOS 文档当作附属说明，它们必须与代码一起生成并保持一致
- 如果 repo 中已经存在从别的成功项目复制来的 `.rcos` / `.cursor` / 其他示例材料：
  - 只能把它们当作 example seed
  - 不能把它们当作新项目事实来源
  - 推荐先移动到 `.rcos_examples/<seed-project>/` 或 `.rcos/examples/<seed-project>/`
  - 新项目自己的权威文件必须重新生成到活跃路径
- 不得直接继承旧项目的项目名、目标、module authority、项目状态或 assumptions
- 实施完成后必须输出：
  - Verification
  - RCOS Update Impact

如果你理解了，请先根据我提供的新项目目标，给出初始化计划并等待确认。

上述 instruction 为了便于理解使用英文来书写，后续的交流和生成请保持以中文为基础。
```
