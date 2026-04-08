# Project RCOS Maintenance

本文件定义 `news_agent_mvp` 中项目级 RCOS 文件的更新条件。目标是避免代码已经变了，但项目上下文仍停留在旧状态。

## 覆盖文件
- PROJECT_BACKGROUND.md
- PROJECT_STATUS.md
- PROJECT_ASSUMPTIONS.md
- CODEBASE_MAP.md
- PROJECT_ONBOARDING_PROMPT.md
- PROJECT_COLLABORATION_PROMPT.md
- PROJECT_RCOS_MAINTENANCE.md
- module_index.yaml

## 总原则
任何代码变更完成后，都必须显式检查 RCOS Update Impact；不能默认“不需要更新”。

---

## 1. 何时更新 PROJECT_BACKGROUND.md
当以下任一情况发生时更新：
- 项目用途发生变化：例如从“技术 / AI 热榜摘要”转向更广泛的信息平台；
- 目标用户发生变化：例如从内部试验工具扩展到明确面向外部用户；
- 范围边界发生实质变化：例如正式引入长期记忆、多 agent、可信度引擎、正文级深度分析主流程；
- 价值主张发生变化：例如从“快速过滤热点”切到“深度研究辅助”。

---

## 2. 何时更新 PROJECT_STATUS.md
当以下任一情况发生时更新：
- 主要功能落地；
- 主要限制被解除；
- 新的重要已知问题出现；
- 当前迭代优先级改变。

### 典型触发改动
- 把 `fetch_url` 正式接入主 pipeline；
- 让 `planner.py` 成为主流程唯一 planner authority；
- 让 `max_steps` 真的参与步骤控制；
- 支持新的模型供应商；
- 修复配置不一致问题（如 `.env.example` 与代码对齐）；
- 更换主要数据源或新增多个稳定 source。

---

## 3. 何时更新 PROJECT_ASSUMPTIONS.md
当以下任一假设改变时更新：
- 运行时环境假设；
- 模型供应商或模型接入方式；
- 数据源假设；
- 工作流假设；
- 参数语义假设（如 `max_steps` 从占位参数变为真实控制参数）。

### 典型触发改动
- `llm.py` 不再只支持 OpenAI；
- 从 subprocess 调工具改成原生 MCP / function calling；
- 新增长期记忆或 RAG；
- 引入正式 reflection / evaluation loop；
- 改变默认部署路径或不再依赖固定用户目录。

---

## 4. 何时更新 CODEBASE_MAP.md
当以下任一结构事实变化时更新：
- 入口点改变；
- 目录结构改变；
- pipeline 顺序改变；
- authority 模块边界改变；
- 运行脚本和服务关系改变；
- 新增重要目录或删除重要目录。

### 典型触发改动
- 增加新的 API entry 或 CLI entry；
- 把 planner 完整收敛到 `planner.py`；
- 增加 `memory.py`、`reflection.py`、`credibility.py` 等新服务模块；
- 改变 UI 组织方式；
- 把工具服务从脚本调用改成独立网络服务。

---

## 5. 何时更新 PROJECT_ONBOARDING_PROMPT.md
当新线程接管项目时最先需要知道的规则发生变化时更新：
- 事实优先级来源改变；
- 新的关键误判风险出现；
- 代码结构变化导致旧 onboarding 路径失效；
- 计划前置规则、最小 scope 规则或 authority 规则有新的项目级约束。

### 典型触发改动
- verifier 产物开始稳定存在并成为高优先级事实来源；
- `module_index.yaml` 结构或角色改变；
- planner authority 从 `agent.py` 转移到 `planner.py`；
- 项目从单体 MVP 变成多服务系统。

---

## 6. 何时更新 PROJECT_COLLABORATION_PROMPT.md
当日常协作流程、输出顺序或 authority 约束变化时更新：
- 计划流程变化；
- 代码输出默认形式变化；
- 新增必须遵循的项目级协作规则；
- authority 模块发生重大重新划分。

### 典型触发改动
- 开始强制使用 patch-only 工作流；
- 开始要求 verifier 输出为变更前置条件；
- planner authority 明确迁移到 `planner.py`；
- 新增 memory / reflection 模块后，需要新增避免重复逻辑的限制。

---

## 7. 何时更新 PROJECT_RCOS_MAINTENANCE.md
当 RCOS 文件本身的维护规则需要被修正时更新。

### 典型触发改动
- 新增必须纳入维护范围的项目级 RCOS 文件；
- 增加新的 authority 文件；
- 维护触发条件不再适用当前项目。

---

## 8. 代码变更类型 → 必须检查哪些 RCOS 文件

### A. 只改 prompt / 输出文案 / UI 样式
至少检查：
- PROJECT_STATUS.md
- CODEBASE_MAP.md（若 UI 路由或页面结构变化）

### B. 改 planner / scoring / enrichment / summarizer 逻辑
至少检查：
- PROJECT_STATUS.md
- PROJECT_ASSUMPTIONS.md
- CODEBASE_MAP.md
- module_index.yaml（若 authority 改变）

### C. 改模型供应商 / LLM 接入方式
至少检查：
- PROJECT_STATUS.md
- PROJECT_ASSUMPTIONS.md
- CODEBASE_MAP.md
- PROJECT_ONBOARDING_PROMPT.md（若接管注意点改变）
- module_index.yaml（若 authority 改变）

### D. 改工具服务、数据源或抓取方式
至少检查：
- PROJECT_STATUS.md
- PROJECT_ASSUMPTIONS.md
- CODEBASE_MAP.md

### E. 改入口、部署脚本、运行方式
至少检查：
- PROJECT_STATUS.md
- PROJECT_ASSUMPTIONS.md
- CODEBASE_MAP.md
- PROJECT_ONBOARDING_PROMPT.md

### F. 引入 memory / reflection / loop / multi-agent
必须检查：
- PROJECT_BACKGROUND.md（若项目定位升级）
- PROJECT_STATUS.md
- PROJECT_ASSUMPTIONS.md
- CODEBASE_MAP.md
- PROJECT_ONBOARDING_PROMPT.md
- PROJECT_COLLABORATION_PROMPT.md
- module_index.yaml

---

## 9. Required AI Behavior
每次批准后的代码变更，AI 必须显式输出：

## RCOS Update Impact
- 受影响的 RCOS 文件有哪些；
- 为什么受影响；
- 是否需要提供完整更新内容。

如果判断“不需要更新”，也必须说明理由，而不是跳过。
