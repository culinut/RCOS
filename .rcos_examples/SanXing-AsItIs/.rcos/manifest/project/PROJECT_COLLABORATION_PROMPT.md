# PROJECT_COLLABORATION_PROMPT

你正在 `SanXing-AsItIs` 项目中协作。

请严格遵守以下协作协议：

## 输出顺序

对任何非平凡任务，先输出：

1. Scope Check
2. Context Summary
3. Change Intent
4. Change Plan

经人类确认后，再进入实现。

## 上下文原则

- 优先读取 `.rcos/manifest/project/*`
- 只读取当前任务所需最少文件
- 不要默认扫描整个仓库
- 如需扩展范围，必须说明：
  - 为什么需要
  - 要读哪些文件
  - 会带来什么风险

## 事实分层

请始终明确区分三类内容：

1. 代码已确认事实
2. RCOS seed / 项目文档中的工作基线
3. 仍待进一步核对的问题

特别是评分语义相关内容：

- `scoring_model_seed.json` 是当前工作基线
- 但由于《三省书》PDF 是扫描件，且本机缺少 OCR / PDF 文本提取工具
- seed 中的具体措辞不能默认视为全部已由原文逐字复核

如果存在 `PROJECT_RCOS_EVOLUTION.md`，还应额外区分：

4. 当前 tenant 已吸收的本体 DNA
5. 当前 tenant 尚未 promotion / 尚未 intake 的 DNA

## 范围约束

默认目标是：

- 最小改动
- 不做隐藏式重构
- 不做未请求的功能扩展
- 不把规划模块写成已实现模块

## 权威与职责

- 当前 `module_index.yaml` 是模块职责的工作声明
- 若发现其与实际代码不一致，应优先修正文档或提出澄清
- 不要在未经确认的情况下新增第二套职责定义

## 每次变更后的收尾

每次批准后的修改完成后，必须报告：

- 改了什么
- 如何验证
- 是否需要更新以下 RCOS 文件：
  - `PROJECT_STATUS.md`
  - `CODEBASE_MAP.md`
  - `PROJECT_ASSUMPTIONS.md`
  - `module_index.yaml`

## RCOS 自演化与上游同步

如果在当前项目中形成了稳定、可复用的 RCOS 协作经验，例如：

- 新的 roadmap planning / tracking 写法
- 新的 RCOS maintenance 规则
- 更成熟的 onboarding / collaboration 约束

则应显式执行：

1. 在当前项目内先落盘并验证；
2. 将该经验总结为候选 RCOS 进化项；
3. 为该候选项标记 contributor project：`SanXing-AsItIs`；
4. 若要同步到主 RCOS 的 example seed，优先同步到与 contributor project 对应的 seed 路径；
5. 不要把来自当前项目的 RCOS 进化误写进无关 example seed；
6. 默认优先同步到本体主 `.rcos`，而不是立即同步 seed 或 zip artifact；
7. 提议是否同步回主 RCOS 仓库；
8. 在人类明确确认前，不要直接修改上游 RCOS 仓库。

## DNA 节奏约束

若存在 `PROJECT_RCOS_EVOLUTION.md`，则默认遵守：

- 主 DNA 层可先演化
- example seed 是延迟 promotion 层
- zip artifact 是发布层
- 除非明确进入例外发布，不要同时更新 seed 与 zip artifact
