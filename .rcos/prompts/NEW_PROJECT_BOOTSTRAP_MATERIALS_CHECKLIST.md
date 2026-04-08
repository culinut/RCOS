# New Project Bootstrap Materials Checklist

## 目的

这份清单用于在一个全新的 project repo 中启动 RCOS bootstrap 之前，帮助你准备最小但足够的输入材料。

适用场景：
- 新建 repo
- 在新 conversation 中让 AI 同时完成 initial code + RCOS project-specific context bootstrap

推荐配合以下 prompt 使用：
- `.rcos/prompts/NEW_PROJECT_RCOS_BOOTSTRAP_PROMPT.md`
- `.rcos/prompts/NEW_PROJECT_RCOS_BOOTSTRAP_PROMPT_VERBOSE.md`

---

## 最小必备材料

下面这些内容通常足够让 AI 先做初始化计划：

### 1. 项目目标
- 这个项目要解决什么问题
- 目标用户是谁
- 你希望它现在处于什么阶段
  - 例如：MVP、内部工具、实验原型、正式产品雏形

### 2. 技术方向
- 计划使用的语言 / 框架
- 明确想用或不想用的技术
- 是否已有部署环境偏好
  - 例如：本地脚本、Docker、云服务、serverless

### 3. 初始功能范围
- 第一版必须完成的 3-7 个能力
- 明确哪些能力不在当前范围
- 是否已有 API / UI / CLI 偏好

### 4. 目录或仓库初始状态
- 当前 repo 是否为空
- 是否已经有 README、requirements、package.json、pyproject.toml、Dockerfile 等
- 如果已有，请把关键文件给 AI

### 5. 协作规则
- 是否使用 RCOS approval-first workflow
- 是否要求 plan before code
- 是否要求代码改动必须同步更新 RCOS 文档
- 是否有额外本地规则目录
  - 例如 `.cursor/rules/`

### 6. 可选的成功项目范例 seed
- 你是否有一个成功项目，想把它作为 RCOS / 协作 / 目录结构范例提供给 AI
- 如果有，推荐放到：
  - `.rcos_examples/<seed-project>/`
  - 或 `.rcos/examples/<seed-project>/`
- 不要把旧项目的 `.rcos/manifest/project/*` 直接放在新项目的活跃权威路径下继续使用

---

## 强烈建议提供的材料

这些内容不是绝对必需，但会显著提升 bootstrap 质量：

### 1. 产品描述
- 一段电梯描述
- 一段“为什么做这个项目”的说明
- 成功标准或验收标准

### 2. 输入 / 输出样例
- 用户会输入什么
- 系统应该输出什么
- 最好给 1-3 个具体例子

### 3. 参考系统或竞品
- 你想参考的产品、页面、交互方式或架构风格
- 你明确不想模仿的对象

### 4. 非功能要求
- 是否优先快速试验还是优先长期可维护
- 是否关注性能、成本、安全、可观测性
- 是否需要日志、测试、CI、部署脚本

### 5. 已知约束
- 时间限制
- API key / 外部服务限制
- 必须兼容的环境
- 必须复用的现有代码或模板

---

## 如果你已经有这些文件，优先直接给 AI

可任选其一或多个：

- README 草稿
- PRD / spec / notes
- 草图或页面描述
- 数据结构草稿
- API 草案
- 初始目录树
- 伪代码
- 参考截图

---

## 推荐的新 conversation 启动步骤

### 方案 A：最简启动
1. 先准备本清单中的“最小必备材料”
2. 在新 conversation 中粘贴：
   - `.rcos/prompts/NEW_PROJECT_RCOS_BOOTSTRAP_PROMPT.md`
3. 再补上你的项目目标和约束

### 方案 B：更稳妥启动
1. 准备“最小必备材料” + “强烈建议提供的材料”
2. 在新 conversation 中粘贴：
   - `.rcos/prompts/NEW_PROJECT_RCOS_BOOTSTRAP_PROMPT_VERBOSE.md`
3. 再补上现有 repo 状态和你希望 AI 先读的文件

### 方案 C：带成功项目范例 seed 的启动
1. 准备最小必备材料
2. 把旧项目范例放到非权威路径：
   - `.rcos_examples/<seed-project>/`
   - 或 `.rcos/examples/<seed-project>/`
3. 在新 conversation 中粘贴：
   - `.rcos/prompts/NEW_PROJECT_RCOS_BOOTSTRAP_PROMPT_VERBOSE.md`
4. 明确告诉 AI：
   - 这些 example seed 只能作为范例
   - 新项目自己的 `.rcos/manifest/project/*` 必须重新生成

---

## 推荐你手动粘贴给 AI 的最小信息模板

```text
项目名称：

项目目标：

目标用户：

当前阶段目标（MVP / 原型 / 内部工具 / 其他）：

计划技术栈：

明确不使用的技术：

第一版必须完成的功能：
1.
2.
3.

明确不在当前范围的功能：
1.
2.
3.

当前 repo 状态：

我会提供给你的关键文件：
1.
2.
3.

协作要求：
- 使用 RCOS
- approval-first
- plan before code
- 同步维护 `.rcos/manifest/project/*`

可选 example seed：
- 是否提供成功项目范例：
- 范例所在路径：
- 说明：只能作为结构/写法/协作范例，不能作为新项目事实来源
```

---

## 判断材料是否足够的简单标准

如果你已经能回答下面这些问题，就通常足够让 AI 开始 bootstrap plan：

- 这个项目做什么？
- 给谁用？
- 第一版必须交付什么？
- 用什么技术做？
- 哪些内容明确先不做？
- 当前 repo 里已经有什么？

如果这些问题还答不清，就先不要让 AI 直接开始写代码，先让它帮你收敛需求更稳。
