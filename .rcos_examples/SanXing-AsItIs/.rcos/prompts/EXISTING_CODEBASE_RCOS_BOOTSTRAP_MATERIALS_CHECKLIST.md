# Existing Codebase RCOS Bootstrap Materials Checklist

## 目的

这份清单用于在一个“已经存在代码和文档”的仓库中补建 RCOS 之前，帮助你准备最小但足够的输入材料。

适用场景：
- 老仓库补建 RCOS
- 需要让 AI 分阶段扫描现有代码并建立 `.rcos/manifest/project/*`
- 需要 AI 在扫描中持续向人类工程师确认事实、意图和 assumptions

推荐配合以下 prompt 使用：
- `.rcos/prompts/EXISTING_CODEBASE_RCOS_BOOTSTRAP_PROMPT.md`
- `.rcos/prompts/BOOTSTRAP_PACK_USAGE_NOTE.md`

---

## 最小必备材料

### 1. 仓库入口材料
- README（如果有）
- 目录树
- 1 到 3 个入口文件
- 任何现有设计文档 / ADR / 技术说明

### 2. 人类工程师口头说明
- 这个系统主要做什么
- 目前主要给谁用
- 现阶段最重要的能力是什么
- 你认为最容易被 AI 误解的地方是什么

### 3. 当前仓库状态
- 当前 repo 是否在活跃开发
- 是否已有未完成重构
- 是否已有明显历史遗留模块
- 是否已有文档与代码不一致的已知问题

### 4. 协作规则
- 是否使用 RCOS approval-first workflow
- 是否要求 plan before code
- 是否要求 AI 在扫描过程中持续向工程师提问确认
- 是否允许 AI 在 bootstrap conversation 中顺手改业务代码
  - 推荐答案通常应为“不允许，除非明确要求”

---

## 强烈建议提供的材料

### 1. 高层结构信息
- 主要目录各自大致做什么
- 哪个文件或模块是主入口
- 哪些模块最值得优先看

### 2. 已知 authority / ownership
- 如果团队已经知道某些逻辑的“事实 authority”
- 哪些模块不应被误当成主入口
- 哪些模块是历史遗留或备用实现

### 3. 已知痛点
- 文档缺失
- 配置混乱
- 历史命名不一致
- 已知技术债
- 可能误导 AI 的旧代码

### 4. 验证材料
- 如果已有测试、脚本、运行说明、部署方式
- 如果已有 repo facts / scan / inventory

---

## 推荐的新 conversation 启动步骤

### 方案 A：标准 existing-codebase bootstrap
1. 先准备本清单中的“最小必备材料”
2. 在新 conversation 中粘贴：
   - `.rcos/prompts/EXISTING_CODEBASE_RCOS_BOOTSTRAP_PROMPT.md`
3. 再补上 README、目录树、入口文件和你的人类说明

### 方案 B：从 bootstrap pack 解压后的 existing-codebase bootstrap
1. 先准备本清单中的“最小必备材料”
2. 在新 conversation 中粘贴：
   - `.rcos/prompts/EXISTING_CODEBASE_RCOS_BOOTSTRAP_PROMPT.md`
3. 再让 AI 读取：
   - `.rcos/prompts/BOOTSTRAP_PACK_USAGE_NOTE.md`

---

## 推荐你手动粘贴给 AI 的最小信息模板

```text
项目名称：

这个仓库主要做什么：

目标用户：

当前阶段：

我认为最关键的入口文件：
1.
2.
3.

我会提供给你的已有文档：
1.
2.
3.

我已知的几个重要事实：
1.
2.
3.

我不确定、需要你帮助梳理的点：
1.
2.
3.

协作要求：
- 使用 RCOS
- approval-first
- plan before code
- 分阶段扫描
- 扫描过程中持续向工程师确认关键事实
- 未经允许不要顺手改业务代码
```

---

## 判断材料是否足够的简单标准

如果你已经能回答这些问题，就通常足够让 AI 开始 bootstrap plan：

- 这个仓库主要做什么？
- 当前最关键的入口从哪里开始看？
- 哪些文档值得优先看？
- 哪些模块最容易误判？
- 有没有必须先向工程师确认的历史背景？

如果这些问题还完全答不出来，建议先不要让 AI 大规模扫描代码，而是先让工程师补一轮口头背景更稳。

