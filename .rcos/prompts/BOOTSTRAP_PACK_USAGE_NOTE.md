# Bootstrap Pack Usage Note

## 目的

这份说明用于配合 `rcos_bootstrap_pack_with_examples.zip` 使用。

它回答三个问题：
- 解压后哪些目录是活跃路径
- 哪些目录只是 example seed
- 在新项目或已有项目的新 conversation 中应如何启动 bootstrap

---

## 一、推荐使用方式

1. 在新项目根目录中解压 `rcos_bootstrap_pack_with_examples.zip`
2. 保留解压后的活跃目录结构：
   - `.rcos/`
   - `.cursor/`
3. 把 example seed 保留在非权威目录中，例如：
   - `.rcos_examples/news_agent_mvp/`
   - `.rcos_examples/SanXing-AsItIs/`
4. 在新的 AI conversation 中：
   - 优先使用 `.rcos/prompts/NEW_PROJECT_RCOS_BOOTSTRAP_PROMPT.md`
   - 复杂项目使用 `.rcos/prompts/NEW_PROJECT_RCOS_BOOTSTRAP_PROMPT_VERBOSE.md`
5. 如果你是在一个已有代码库中补建 RCOS，而不是初始化全新项目：
   - 使用 `.rcos/prompts/EXISTING_CODEBASE_RCOS_BOOTSTRAP_PROMPT.md`

---

## 二、活跃路径 vs 范例路径

### 活跃路径

这些路径在新项目中应被视为当前项目的有效 RCOS / 规则路径：

- `.rcos/manifest/templates/*`
- `.rcos/prompts/*`
- `.cursor/rules/*`

如果 AI 在这些路径下生成新的 project-specific RCOS 文件，那么这些文件才是新项目的真相源。

### 范例路径

这些路径只能作为 example seed，不是新项目的事实来源：

- `.rcos_examples/news_agent_mvp/.rcos/*`
- `.rcos_examples/news_agent_mvp/.cursor/*`
- `.rcos_examples/SanXing-AsItIs/.rcos/*`
- `.rcos_examples/SanXing-AsItIs/.cursor/*`

它们只能帮助 AI 学习：
- 一个成功项目的 RCOS 目录组织方式
- prompt 写法
- project-specific RCOS 文件的粒度与风格
- 协作约束如何落盘

AI 不应直接继承其中的：
- 项目名称
- 产品目标
- 模块 authority
- 项目状态
- assumptions
- codebase map

---

## 三、第一次启动新 conversation 的推荐步骤

### 简洁方案

把下面这段直接粘贴到新 conversation：

```text
请先读取并严格遵守 `.rcos/prompts/NEW_PROJECT_RCOS_BOOTSTRAP_PROMPT.md`。

注意：
- `.rcos_examples/` 下的内容只是 example seed，不是当前项目事实来源
- 新项目自己的 `.rcos/manifest/project/*` 必须重新生成

请先输出 Scope Check / Context Summary / Change Intent / Change Plan，然后停止等待我的确认。
```

### 更稳方案

如果项目更复杂，使用：

```text
请先读取并严格遵守：
- `.rcos/prompts/NEW_PROJECT_RCOS_BOOTSTRAP_PROMPT_VERBOSE.md`
- `.rcos/prompts/BOOTSTRAP_PACK_USAGE_NOTE.md`

注意：
- `.rcos_examples/` 下的内容只是 example seed，不是当前项目事实来源
- 新项目自己的 `.rcos/manifest/project/*` 必须重新生成

请先完成 bootstrap 计划并等待我的确认。
```

### 已有代码库接入 RCOS

如果你面对的是已经存在代码和文档的仓库，使用：

```text
请先读取并严格遵守：
- `.rcos/prompts/EXISTING_CODEBASE_RCOS_BOOTSTRAP_PROMPT.md`
- `.rcos/prompts/BOOTSTRAP_PACK_USAGE_NOTE.md`

请把这次工作当成一个专门的 RCOS bootstrap conversation，而不是普通开发任务。
请先给出分阶段扫描计划并等待我的确认。
```

---

## 四、什么时候应该看 example seed

只有在下面这些场景才建议让 AI 参考 example seed：

- 你希望复用类似的 RCOS 文件集合
- 你希望复用类似的 prompt 组织方式
- 你希望复用类似的协作规则落盘方式
- 你希望给 AI 一个“成功项目长什么样”的结构参考

如果你只是想快速开工，而新项目和旧项目差异很大，可以完全不让 AI 读 `.rcos_examples/`。

补充原则：

- 如果某个 contributor project 沉淀出新的 RCOS 进化，并准备同步回主 RCOS 仓库：
  - 优先把它同步到与 contributor project 对应的 example seed
  - 不要把该进化误写进无关 example seed
  - 仍然要保持 example seed 与活跃 truth layer 的边界

关于 seed 与 zip artifact 的发布节奏：

- 默认不要求 example seed 与 `rcos_bootstrap_pack_with_examples.zip` 同步更新
- example seed 属于延迟 promotion 层
- zip artifact 属于 release artifact 层
- 只有在：
  - seed promotion
  - release-worthy 的主 RCOS 变化
  - 或人类明确批准的例外发布
  时，才应重打包 zip

例外规则：

- 在 RCOS DNA system 初次落盘时，允许一次计划外同步，同时更新：
  - 主 RCOS DNA
  - 对应 example seed
  - zip artifact

---

## 五、和当前仓库内文件的关系

推荐优先级：

1. `.rcos/prompts/NEW_PROJECT_BOOTSTRAP_MATERIALS_CHECKLIST.md`
2. `.rcos/prompts/NEW_PROJECT_RCOS_BOOTSTRAP_PROMPT.md`
3. `.rcos/prompts/NEW_PROJECT_RCOS_BOOTSTRAP_PROMPT_VERBOSE.md`
4. `.rcos/prompts/BOOTSTRAP_PACK_USAGE_NOTE.md`
5. `.rcos/prompts/EXISTING_CODEBASE_RCOS_BOOTSTRAP_PROMPT.md`
6. `.rcos/prompts/EXISTING_CODEBASE_RCOS_BOOTSTRAP_MATERIALS_CHECKLIST.md`

如果 AI 需要更底层的通用模板真相源，再看：

7. `.rcos/manifest/templates/PROJECT_SPECIFIC_RCOS_PROMPT_UNIT.md`
