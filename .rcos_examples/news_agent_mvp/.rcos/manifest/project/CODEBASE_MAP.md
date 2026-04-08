# Codebase Map

## 仓库概览
该仓库是一个以 Python 为主的新闻摘要 MVP。当前代码大致分为四层：
- 启动与 API 层；
- 配置与日志层；
- Agent / 检索 / 服务层；
- 工具服务与前端展示层。

## 入口点

### 1. `agent_api.py`
当前主启动入口。
职责：
- 导入 `app.main:app`；
- 读取 `HOST` / `PORT`；
- 启动 uvicorn。

### 2. `app/main.py`
FastAPI 应用装配入口。
职责：
- 初始化日志；
- 创建 `FastAPI(title=PROJECT_TITLE)`；
- 注册 API router。

### 3. `mcp_news_server.py`
工具服务入口。
职责：
- 读取 `hotlists.yaml`；
- 提供 `list_sources`、`get_hotlist`、`search_news`、`fetch_url`；
- 可作为 CLI 工具执行，也可作为 `FastMCP` 服务运行。

## 主要目录

### `app/api/`
负责 HTTP 路由与请求 schema。

#### `routes.py`
对外 HTTP 接口集中地。
主要端点：
- `GET /health`
- `GET /chat`
- `POST /query`
- `POST /query-async`
- `GET /query-status/{task_id}`
- `POST /fact-check`
- `POST /fact-check-async`
- `POST /follow-up`
- `POST /follow-up-async`
- `GET /refresh`
- `GET /log`
- `GET /log/raw`

说明：
- `/query` 调用 `run_agent(req.question, req.max_steps)`；
- `/query-async` 创建后台 query task，用于 `/chat` 的等待进度反馈；
- `/query-status/{task_id}` 返回 query task 当前状态、步骤进度与最终结果；
- `/fact-check` 调用独立事实核查子流程；
- `/fact-check-async` 创建后台 fact-check task；
- `/follow-up` 调用独立一次性追问子流程；
- `/follow-up-async` 创建后台 follow-up task；
- `/refresh` 通过 `subprocess.Popen()` 执行 `scripts/restart.sh`；
- `/log` 支持 latest / archive 两种视图，并通过查询参数选择 archive 的年、月、日、小时；
- `/log` 在 archive 浏览中还会合并当天未归档 hourly rotated logs；
- `/log/raw` 仍只读取活跃 `server.log`。

#### `schemas.py`
定义请求体模型。
当前核心模型：
- `QueryRequest(question, max_steps=DEFAULT_MAX_STEPS)`
- `FactCheckRequest(title, url, summary, source, published)`
- `FollowUpRequest(mode, follow_up_question, bound_news, optional_search_enabled)`

### `app/config/`
负责运行配置读取。

#### `settings.py`
当前配置事实来源。
持有：
- `BASE_DIR`, `LOG_DIR`, `LOG_ARCHIVE_DIR`, `LOG_PATH`
- `HOST`, `PORT`
- `MODEL_PROVIDER`, `MODEL_NAME`, `OPENAI_API_KEY`
- `PROJECT_TITLE`
- `DEFAULT_SOURCE_ID`, `DEFAULT_MAX_STEPS`, `DEFAULT_HOTLIST_LIMIT`
- `MCP_SERVER_SCRIPT`, `RESTART_SCRIPT`

说明：
- `DEFAULT_HOTLIST_LIMIT` 当前在主流程中未实际使用；
- `.env.example` 与这里的变量名目前不一致。

### `app/core/`
负责横切基础设施。

#### `logging.py`
日志初始化与日志路径访问。
职责：
- 建立活跃 `server.log` + stream handler；
- 在每小时第一条日志时执行 hourly rollover；
- 将 rollover 后的文件命名为 `server.log.YYYY-MM-DD-HH`；
- 在跨天后的第一批日志上归档当天之前的 hourly logs 到 `logs/archive/yyyy/mm/dd/hh/`；
- 返回统一 logger；
- 提供 `get_log_path()`。

说明：
- 当天的 rotated hourly logs 在归档前仍留在 `logs/` 根目录下，`log_page.py` 需要自行把它们纳入浏览索引。

### `app/services/`
仓库最核心的业务层。

#### `agent.py`
当前主编排模块，也是事实上的 planner authority 所在地。
职责：
- 接收用户问题；
- 内联构造 planner prompt 并调用 LLM；
- 在普通查询链路中上报步骤级 progress callback；
- 调 retrieval pipeline；
- 调 relevance scoring；
- 调 enrichment；
- 调 summarizer；
- 为 `/fact-check` 提供轻量委托入口；
- 为 `/follow-up` 提供轻量委托入口；
- 组装最终响应与 `trace`。

注意：
- `max_steps` 目前只被接收和记录日志，没有真正控制流程；
- 当前 planner 逻辑没有复用 `planner.py`。

#### `query_tasks.py`
负责普通查询、事实核查和追问的轻量异步任务管理。
权威职责：
- 创建 query / fact-check / follow-up task；
- 在后台线程执行 `run_agent()`、`run_fact_check()`、`run_follow_up()`；
- 保存任务状态、当前步骤、进度百分比与最终结果；
- 为 `/query-status/{task_id}` 提供状态读取。

#### `query_generation.py`
负责 query generation。
权威职责：
- 根据用户问题生成 2-5 个结构化检索查询；
- 为 search source 生成 search-friendly query 文本；
- 覆盖 broad / specific 两种粒度；
- 在 LLM 输出失败时提供最小 fallback 查询集。

#### `retrieval_models.py`
负责检索层统一数据结构。
权威职责：
- 定义 `SearchQuery`
- 定义 `RetrievedItem`

说明：
- `SearchQuery` 当前同时承载用户可读 query 与 search-friendly query 元数据。

#### `retrieval_normalize.py`
负责不同来源结果的标准化。
权威职责：
- RSS item 归一化；
- search item 归一化；
- URL canonicalization。

#### `retrieval_dedup.py`
负责检索结果去重。
权威职责：
- 基于 `title + url` 做 exact / near-duplicate 去重；
- 合并重复 item 的 `matched_queries` 与补充字段。

#### `retrieval_rerank.py`
负责 retrieval 层第一阶段排序。
权威职责：
- 计算 query keyword match；
- 消费 `freshness.py` 的时效性结果；
- 组合为 retrieval score 并输出 reranked items。

说明：
- 这里不应复制 freshness 分段逻辑，recency 只消费 `freshness.py`。

#### `retrieval_pipeline.py`
负责 query-driven retrieval 主链路。
权威职责：
- 调 query generation；
- 调 RSS retrieval 与 lightweight search retrieval；
- 在 lightweight search 0 结果时尝试 fallback query；
- 调 normalization、dedup、rerank；
- 返回结构化 retrieval 结果给 `agent.py`。

#### `fact_check_queries.py`
负责 fact check query generation。
权威职责：
- 围绕单条新闻生成 2-5 个二次求证 query；
- 覆盖原始事件、关键主体、官方回应、证伪方向；
- 在 LLM 失败时提供最小 fallback。

#### `fact_check_analyzer.py`
负责 fact check 结果分析。
权威职责：
- 生成可信度分与可信度标签；
- 生成中文概述与依据说明；
- 输出 authority_sources；
- 输出 consistency_assessment。

#### `fact_check_pipeline.py`
负责独立事实核查子流程。
权威职责：
- 调 fact check query generation；
- 复用 retrieval pipeline 做二次检索；
- 聚合候选项并去重；
- 上报 fact-check-specific progress steps；
- 调 analyzer 输出专用 fact-check 结构。

#### `follow_up_classifier.py`
负责 follow-up 问题理解。
权威职责：
- 判断追问属于 explanation / background / comparison / verification / impact_analysis / other 哪一类。

#### `follow_up_answerer.py`
负责 follow-up 问答生成。
权威职责：
- 围绕绑定新闻生成问答式中文回复；
- 输出 supporting_points 与 used_context；
- 避免退化为普通新闻播报。

#### `follow_up_pipeline.py`
负责一次性追问子流程。
权威职责：
- 接收 follow-up question 与 bound_news；
- 调 classifier；
- 视情况复用 retrieval pipeline；
- 按需调用 fetch_url；
- 上报 follow-up-specific progress steps；
- 输出专用 follow-up 结构。

#### `planner.py`
已存在的 planner 辅助模块。
当前提供：
- `build_planner_messages()`
- `parse_planner_output()`
- `run_planner()`

现状：
- 模块存在，但未被 `run_agent()` 正式接入；
- 因此它不是当前主流程实际 authority。

#### `mcp_client.py`
负责从主应用侧调用 `mcp_news_server.py`。
当前方式：
- 通过 `subprocess.run()` 调命令行工具；
- 成功时解析 stdout JSON；
- 失败时返回统一错误字典。

#### `freshness.py`
负责时间相关计算。
权威职责：
- `compute_freshness()`：统一产出 `freshness_score` 与 `freshness_label`；
- `compute_freshness_score()`：对外兼容包装；
- `compute_freshness_label()`：对外兼容包装。

#### `scoring.py`
负责 relevance 结果解析与候选条目组装。
权威职责：
- 解析相关性评分结果；
- 从 RSS summary HTML 中抽取评论区链接；
- 消费 `freshness.py` 的统一时效性结果；
- 计算 relevance / total score；
- 生成并排序 `scored_items`。

当前综合分公式：
- `total_score = relevance_score * 0.7 + freshness_score * 0.3`

#### `enrichment.py`
负责中文本地化与展示字段增强。
权威职责：
- 生成 `title_zh`
- 生成 `summary_zh`
- 生成 `relevance_label`

#### `summarizer.py`
负责最终摘要生成。
权威职责：
- 基于问题、focus、summary_instruction 与已评分条目生成：
  - `final_summary`
  - `top_items`
  - `followup_suggestions`

#### `llm.py`
负责 LLM 统一调用。
当前事实：
- 只支持 OpenAI；
- `build_openai_client()` 延迟初始化客户端；
- `call_llm()` 是服务层统一入口。

### `app/web/`
负责浏览器端页面模板。

#### `chat_page.py`
内嵌聊天页面 HTML / JS。
职责：
- 调 `/query`；
- 调 `/query-async` 与 `/query-status/{task_id}`；
- 调 `/fact-check`；
- 调 `/fact-check-async`；
- 调 `/follow-up`；
- 调 `/follow-up-async`；
- 以 Markdown + 新闻卡片展示结果；
- 在精选新闻卡片上渲染“事实核查”按钮；
- 在精选新闻卡片上渲染“追问”按钮；
- 维护一次性 follow-up mode 状态；
- 在普通查询提交后渲染 spinner、步骤文案和进度条；
- 在事实核查提交后渲染 spinner、步骤文案和进度条；
- 在追问提交后渲染 spinner、步骤文案和进度条；
- 轮询异步 task 状态，并在完成后替换等待卡；
- 渲染专用 fact-check 回复块；
- 渲染专用 follow-up 回复块；
- 显示分数、标签、本地时间、原始链接与评论区链接。

#### `log_page.py`
负责日志页面 HTML 渲染与日志浏览交互。
职责：
- 渲染 latest `server.log` 视图；
- 扫描 `logs/archive/yyyy/mm/dd/hh/` 结构；
- 合并当天尚未归档的 hourly rotated logs；
- 提供年 / 月 / 日 / 小时选择；
- latest 模式提供自动刷新 toggle；
- 提供行级复制交互：
  - 从某一行复制到结尾
  - 设起点后复制区间

说明：
- 前端当前固定发送 `max_steps: 3`；
- 页面是完整内嵌模板，不依赖独立前端构建流程。

#### `log_page.py`
日志页面 HTML 渲染。
职责：
- 渲染 latest `server.log` 视图；
- 扫描 `logs/archive/yyyy/mm/dd/hh/` 结构；
- 仅展示实际存在日志的年、月、日、小时；
- 读取并展示所选 hourly log file；
- 在 latest 模式自动刷新，在 archive 模式关闭自动刷新。

## 核心流水线
当前主流程如下：

1. 用户通过 `/query` 提交 `question`；
2. `app/api/routes.py` 调用 `run_agent()`；
3. `agent.py` 内联 planner prompt，判断：
   - 是否需要执行新闻检索；
   - 摘要应围绕什么 focus；
4. 如需要新闻，则通过 `retrieval_pipeline.py` 进行：
   - query generation；
   - RSS retrieval；
   - lightweight search retrieval；
   - search fallback attempts；
   - dedup / rerank；
5. 获取 `raw_items` 后，进行：
   - relevance scoring；
   - enrichment；
   - freshness / total score 计算与排序；
6. 排序后的条目交给 `summarizer.py`；
7. 组装返回 JSON；
8. `/chat` 页面渲染结果。

## Fact Check 子流程

1. 用户点击某条精选新闻卡片上的“事实核查”按钮；
2. 前端向 `POST /fact-check` 发送单条新闻字段；
3. `agent.py` 调 `fact_check_pipeline.py`；
4. `fact_check_pipeline.py` 生成 fact-check queries；
5. 复用 retrieval pipeline 做二次搜索；
6. `fact_check_analyzer.py` 输出可信度与权威信源结构；
7. 前端用 fact-check 专用卡片展示结果。

## Follow-up 子流程

1. 用户点击某条精选新闻卡片上的“追问”按钮；
2. 前端进入一次性 follow-up mode，但不立即发送正式消息；
3. 用户下一条消息被发送到 `POST /follow-up`；
4. `agent.py` 调 `follow_up_pipeline.py`；
5. `follow_up_pipeline.py` 先做问题分类；
6. 必要时复用 retrieval pipeline 和 fetch_url；
7. `follow_up_answerer.py` 输出问答式中文回复；
8. 前端展示 follow-up 专用回复，并自动退出模式。

## Log Browser 子流程

1. 用户访问 `/log`；
2. latest 模式默认显示活跃 `server.log`；
3. archive 模式会合并：
   - `logs/archive/yyyy/mm/dd/hh/` 中已归档 hourly logs；
   - 当天尚未归档、仍位于 `logs/` 根目录的 hourly rotated logs；
4. 用户可切换自动刷新；
5. 用户可通过行首选择按钮复制从某一行到结尾，或复制选中区间。

## 数据流

### 输入数据
- 用户 query；
- `.env` 配置；
- `hotlists.yaml` 的 source 列表；
- RSS feed 内容；
- lightweight search source 返回结果。

### 中间数据
- `planner_raw` / `planner`
- `retrieval_result`
- `generated_queries`
- `search_diagnostics`
- `raw_items`
- `scorer_raw`
- `relevance_map`
- `enrichment_result`
- `scored_items`
- `summary_data`
- `fact_check_queries`
- `fact_check_retrieval`
- `authority_sources`
- `consistency_assessment`
- `follow_up_question`
- `question_type`
- `supporting_points`
- `used_context`
- `trace`

### 输出数据
- `/query` 返回 JSON；
- `/chat` 页面展示；
- `logs/server.log`；
- `logs/server.log.YYYY-MM-DD-HH`；
- `logs/archive/yyyy/mm/dd/hh/server.log.YYYY-MM-DD-HH`；
- `/log` latest / archive 日志查看；
- `/log/raw` 活跃日志原文查看。

## Runtime / 脚本

### `scripts/restart.sh`
当前重启脚本。
职责：
- 进入固定目录；
- 激活虚拟环境；
- `pkill -f "python agent_api.py"` 掉旧进程；
- 后台重启 `agent_api.py`。

说明：
- 路径是硬编码的，明显绑定个人机器环境。

### `hotlists.yaml`
当前数据源配置事实来源。
默认 sources：
- `hn_frontpage`
- `hn_newest`
- `reddit_openai`

## 当前 authority 映射（基于当前源码事实）
- 主流程编排：`app/services/agent.py`
- Planner 实际 authority：`app/services/agent.py`（不是 `planner.py`）
- Planner 辅助模块：`app/services/planner.py`
- Query generation：`app/services/query_generation.py`
- Retrieval normalization / dedup / rerank / pipeline：`app/services/retrieval_*.py`
- LLM 调用：`app/services/llm.py`
- 工具服务：`mcp_news_server.py`
- 工具调用桥：`app/services/mcp_client.py`
- 时间 / 时效性：`app/services/freshness.py`
- 评分组装：`app/services/scoring.py`
- 中文本地化：`app/services/enrichment.py`
- 最终摘要：`app/services/summarizer.py`
- 配置：`app/config/settings.py`
- Web 页面：`app/web/chat_page.py`, `app/web/log_page.py`
