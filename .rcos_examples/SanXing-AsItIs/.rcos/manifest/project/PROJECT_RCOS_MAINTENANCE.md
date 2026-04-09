# PROJECT_RCOS_MAINTENANCE

本文定义 `SanXing-AsItIs` 的项目级 RCOS 文件在什么情况下必须更新。

## 总原则

项目级 RCOS 文件不是装饰性文档，而是当前项目协作系统的一部分。

当代码、运行方式、语义基线或产品边界发生变化时，必须同步检查这些文件是否需要更新。

---

## 文件职责

### `PROJECT_BACKGROUND.md`

在以下情况下更新：

- 项目目标变化
- 核心价值定位变化
- 核心非目标变化
- 评分语义来源发生重大变化

### `PROJECT_STATUS.md`

在以下情况下更新：

- 当前阶段变化
- 当前优先级变化
- 已完成 / 未完成列表明显变化
- 关键风险变化

### `PROJECT_ASSUMPTIONS.md`

在以下情况下更新：

- 用户使用方式假设变化
- 产品边界假设变化
- 技术假设变化
- 评分语义证据状态变化

### `CODEBASE_MAP.md`

在以下情况下更新：

- 新增入口点
- 新增目录或模块
- 运行链路变化
- 数据流变化
- 占位目录变为真实实现

### `CURRENT_BASELINE.md`

在以下情况下更新：

- 当前已实现能力变化
- 当前阻塞项变化
- 数据库 / PDF / 模板等资源状态变化
- 评分 seed 的验证状态变化

### `PROJECT_ROADMAP.md`

在以下情况下更新：

- 当前推荐实现顺序变化
- 里程碑定义变化
- 当前阶段判断变化
- 关键未决策项得到结论
- 新阻塞点改变推进路径

### `PROJECT_RCOS_EVOLUTION.md`

在以下情况下更新：

- tenant_protocol_version 变化
- tenant_core_dna_base_release 变化
- 新的 local candidate DNA 出现
- 某个 candidate 被上行 promotion
- 某个本体 DNA 被下行 intake 或暂缓 intake
- seed / artifact 节奏规则发生变化

### `module_index.yaml`

在以下情况下更新：

- 模块职责变化
- 模块实现状态变化
- 新增或删除模块
- authority 归属得到澄清

### `PROJECT_ONBOARDING_PROMPT.md`

在以下情况下更新：

- 新线程接手时必须先读的材料变化
- 当前关键协作约束变化
- 评分语义核对边界变化

### `PROJECT_COLLABORATION_PROMPT.md`

在以下情况下更新：

- 日常协作流程变化
- 审批门或事实分层规则变化
- RCOS 输出顺序变化

---

## 本项目的特别维护要求

### 评分语义相关

若发生以下任一情况，必须同步检查：

- `scoring_model_seed.json` 有实质更新
- 对《三省书》PDF 完成了更高精度的 OCR 或人工校勘
- 维度数量、时间切片、预读内容发生变化
- “高分语义”的统一规则发生变化

受影响文件通常包括：

- `PROJECT_BACKGROUND.md`
- `PROJECT_STATUS.md`
- `PROJECT_ASSUMPTIONS.md`
- `CURRENT_BASELINE.md`
- `CODEBASE_MAP.md`
- `module_index.yaml`

### RCOS 自演化与上游同步相关

若当前项目在实践中沉淀出可复用的 RCOS 改进，例如：

- 新的项目级文件类型
- 更成熟的 roadmap planning / tracking 机制
- 更成熟的 onboarding / collaboration / maintenance 规则

则必须同步检查：

- 当前项目的相关 RCOS 文件是否已经先落盘
- 该改进是否已被表述为项目内已确认实践
- 是否值得提议同步回主 RCOS 仓库

执行约束：

- 该类候选改进应标记 contributor project：`SanXing-AsItIs`
- 若同步到主 RCOS 的 example seed，应优先更新与 contributor project 对应的 seed 路径
- 不要把当前项目的 RCOS 进化误落到其他项目的 example seed
- 默认优先同步到本体主 `.rcos`
- 不要默认同时更新 example seed 与 zip artifact
- 在得到人类明确确认前，不要直接修改上游 RCOS 仓库
- 一旦确认同步，应同时检查：
  - 本项目 RCOS 文件
  - 主 RCOS 模板 / prompt
  - 主 RCOS example seed

### 运行链路相关

若发生以下任一情况，必须同步检查：

- FastAPI 入口变化
- systemd / socket activation 变化
- `.venv`、端口、启动命令变化

受影响文件通常包括：

- `CODEBASE_MAP.md`
- `CURRENT_BASELINE.md`
- `PROJECT_STATUS.md`

### 代码落地相关

若以下模块从规划变为真实实现：

- `checkin`
- `storage`
- `ui`
- `eightfold_display`
- `export_pdf`

则必须同步更新：

- `CODEBASE_MAP.md`
- `CURRENT_BASELINE.md`
- `PROJECT_STATUS.md`
- `module_index.yaml`

---

## 每次任务结束时的最小检查

完成任何已批准改动后，至少检查一次：

1. 当前修改是否改变了项目事实
2. 当前修改是否使某个 RCOS 文件过时
3. 当前修改是否把“规划”推进成了“现实”
4. 当前修改是否改变了评分语义证据状态

如果答案是“是”，就要同步更新 RCOS 文件或明确说明为何暂不更新。
