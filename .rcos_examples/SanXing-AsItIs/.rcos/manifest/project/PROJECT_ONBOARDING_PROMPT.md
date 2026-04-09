# PROJECT_ONBOARDING_PROMPT

你正在接手一个 RCOS 管理下的现有项目：`SanXing-AsItIs`。

请先理解以下事实，再决定任何修改：

## 项目本质

这是一个将纸质《三省书》数字化的低摩擦自我反思系统。

当前重点不是功能扩展，而是：

- 维护真实的项目上下文
- 逐步沉淀评分语义
- 在最小运行骨架上继续推进

## 你必须先读的文件

- `.cursor/rules/rcos_enforced.md`
- `.cursor/rules/rcos_approval_gate.md`
- `.rcos/manifest/templates/META_INSTRUCTIONS.md`
- `.rcos/manifest/project/PROJECT_BACKGROUND.md`
- `.rcos/manifest/project/PROJECT_STATUS.md`
- `.rcos/manifest/project/PROJECT_ASSUMPTIONS.md`
- `.rcos/manifest/project/CODEBASE_MAP.md`
- `.rcos/manifest/project/CURRENT_BASELINE.md`
- `.rcos/manifest/project/PROJECT_ROADMAP.md`
- `.rcos/manifest/project/module_index.yaml`

如果任务与评分语义相关，还必须读：

- `.rcos/manifest/project/scoring_model_seed.json`
- `.rcos/manifest/project/三省书_monthly.pdf`

## 当前真实基线

- 应用代码目前只有最小 FastAPI 运行骨架
- 已确认有 systemd socket activation 运行链路
- `data/SanXing.db` 当前为空文件
- `pdf/export/` 与 `pdf/template/` 当前为空目录
- `scoring_model_seed.json` 是当前评分语义工作基线

## 关于评分语义的关键约束

- seed 已可作为继续建模的工作基线
- 已确认其结构完整：
  - 三次时间切片
  - 六度预读
  - 八正道预读
  - 12 个评分维度
- 但参考 PDF 是扫描件
- 当前本机环境缺少 OCR / PDF 文本提取工具
- 所以不能把 seed 中每一条措辞都当作“已逐字核对原文”

## 工作规则

你必须先输出：

1. Scope Check
2. Context Summary
3. Change Intent
4. Change Plan

未经批准，不要：

- 改代码
- 改 RCOS 文件
- 扩大扫描范围

## 特别提醒

- 不要把 `module_index.yaml` 中的规划模块误当成全部已实现模块
- 不要把 seed 中的工作语义未经标注地升级为已核对事实
- 不要绕过 RCOS 审批门

## 关于 RCOS 自演化与上游同步

如果在项目协作过程中发现了可复用、可泛化的 RCOS 改进，例如：

- 新的项目级文件形态
- 更稳的 planning / tracking 方式
- 更明确的 onboarding / maintenance 约束

则应：

1. 先在当前项目内把该改进沉淀为本地已确认实践；
2. 将 contributor project 标记为 `SanXing-AsItIs`；
3. 明确说明它是否值得同步回主 RCOS 仓库；
4. 在得到人类明确确认前，不要直接修改上游 RCOS 仓库。
