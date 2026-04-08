# Project Assumptions

本文件只记录当前源码能够支持、且会影响协作判断的假设；不把愿景写成事实。

## 技术假设

### 1. 当前主实现语言与框架假设
- 主项目使用 Python；
- 对外服务由 FastAPI 承担；
- 前端页面以内嵌 HTML/JS 字符串形式放在 Python 文件中；
- 日志使用 Python logging + 自定义 `TimedRotatingFileHandler` 派生 handler；
- 活跃日志固定写入 `logs/server.log`；
- 每小时第一条日志会触发 hourly rollover，上一小时文件命名为 `server.log.YYYY-MM-DD-HH`；
- 跨天后的第一批日志会把当天之前的 hourly log 移动到 `logs/archive/yyyy/mm/dd/hh/`。

### 2. 当前模型接入假设
- 当前只稳定支持 OpenAI；
- `MODEL_PROVIDER` 存在，但 `llm.py` 对非 `openai` 会直接报错；
- 统一 LLM 调用入口是 `app/services/llm.py::call_llm()`；
- 当前没有 function calling、response schema enforcement 或多供应商适配层。

### 3. 当前工具调用假设
- 工具调用不是模型原生 function calling；
- 主应用通过 `subprocess.run()` 调 `mcp_news_server.py --tool ...`；
- 工具脚本既能命令行执行，也能以 `FastMCP` 方式运行；
- 当前主 pipeline 已正式调用 `list_sources`、`get_hotlist` 与 `search_news`；
- `fetch_url` 仍未接入主摘要链路。

### 4. 当前运行环境假设
- 项目默认依赖 `.env`；
- 默认通过 `agent_api.py` 启动 uvicorn；
- `scripts/restart.sh` 假设固定目录 `/home/culinut/Workspace/news_agent_mvp` 与 `.venv/bin/activate` 存在；
- `mcp_client.py` 假设当前运行环境里 `python` 命令可用，并能直接执行 `mcp_news_server.py`；
- `/log` 当前是服务端渲染的日志浏览页，可浏览 archive 中实际存在的年月日小时日志；
- `/log` 还会合并当天未归档的 hourly rotated logs 供浏览；
- `/log/raw` 仍只读取活跃 `server.log`，不提供 archive raw 浏览能力。
- `/chat` 当前对普通 `/query`、`/fact-check` 和 `/follow-up` 都使用轻量异步 task + 轮询模式来显示等待进度。

### 5. 当前数据源假设
- 当前主要输入是 RSS + 一个轻量 search source；
- `hotlists.yaml` 是 source 配置事实来源；
- 默认 source 很少，且明显偏技术 / AI 社区；
- 当前没有搜索索引、数据库缓存或正文抓取结果持久化。

## 产品假设

### 1. 当前第一优先级是“快速消费热点”
现有链路更强调：
- 先判断值不值得检索；
- 再生成可覆盖不同表达方式与粒度的查询；
- 再聚合多源候选项；
- 再给排序后的候选项；
- 再用中文摘要压缩信息。

这说明当前首要目标是节省浏览时间，而不是做全面检索。

### 2. 当前产品更像“热点过滤器 + 中文说明层”
系统不是简单翻译器，因为它已经引入：
- relevance score；
- freshness score；
- relevance label；
- final summary / top_items / followup_suggestions。

但它也还不是独立决策引擎，因为这些分数主要服务排序和展示。

### 3. 当前产品仍偏内部实验工具
源码里直接包含：
- `/refresh` 重启入口；
- `/log` 和 `/log/raw` 日志查看；
- 单文件内嵌式页面模板。

这说明当前交付重心仍是快速试验，而不是正式对外产品化。

### 4. 当前主要面向英文技术 / AI 新闻，不应默认泛化到“新闻平台”
虽然用户可以自由发问，但默认 sources 仍只覆盖少量英文技术社区源，因此不应把当前系统表述成广义新闻平台。

## AI Workflow 假设

### 1. 当前实际工作流
当前主流程是：
- `run_agent()` 内联 planner prompt；
- query generation；
- multi-source retrieval；
- dedup / rerank；
- relevance scoring；
- enrichment；
- summarizer。

另外，普通查询、事实核查和追问现在都会在前端通过异步 task 展示步骤级等待反馈，但各自主业务步骤本身仍分别由 `run_agent()`、`run_fact_check_pipeline()`、`run_follow_up_pipeline()` 单次执行。

### 2. 当前系统是单轮 workflow，而非完整 agent
可以确认：
- 有 LLM 判断；
- 有外部工具；
- 有多阶段处理；

不能确认：
- 有 loop；
- 有记忆；
- 有 reflection；
- 有多 agent；
- 有自动失败恢复。

### 3. 当前 `max_steps` 更像预留参数，而不是实际控制器
- API schema 暴露了 `max_steps`；
- `run_agent()` 接收并记录它；
- 前端 `/chat` 也固定发送 `max_steps: 3`；
- 但当前源码没有真正按 `max_steps` 控制步骤数。

### 4. 当前 freshness authority 假设
- 发布时间解析与时效性标签/分数换算应集中在 `app/services/freshness.py`；
- `app/services/scoring.py` 负责消费该结果并做总分组装，不应重复维护另一套发布时间分段规则。

### 5. 当前 trace 是调试材料，不是 memory 层
`trace` 记录 planner / scorer / summarizer 等原始输出，方便排查，但当前不会被后续请求复用。

### 6. 当前等待反馈假设
- `/query`、`/fact-check`、`/follow-up` 本身仍可同步调用；
- `/chat` 为了改善长等待体验，会对三类耗时操作改走异步 task + 状态轮询；
- 进度条当前基于真实步骤位置映射，不是基于精确耗时估算；
- 普通查询可见步骤至少包括 `planner / retrieval / relevance_scoring / enrichment / summarizing / done`；
- 事实核查可见步骤至少包括 `fact_check_query_generation / fact_check_retrieval / fact_check_analysis / fact_check_authority_sources / done`；
- 追问可见步骤至少包括 `follow_up_classification / follow_up_retrieval / follow_up_context_building / follow_up_answering / done`。

### 7. 当前 retrieval layer v1 假设
- query generation 依赖 LLM 输出，失败时退回模板化 fallback queries；
- query generation 当前会同时产出用户可读 query 与 search-friendly query；
- lightweight search source 当前是 Google News RSS 查询接口的最小实现；
- 当 primary search query 0 结果时，retrieval pipeline 会尝试 fallback query；
- retrieval rerank 只做关键词覆盖与 recency 混合打分，不做 embedding 或 LLM rerank；
- 去重当前只依赖 `title + url` 和简单字符串相似度。

### 8. 当前 fact check workflow 假设
- fact check 是独立子流程，不应混入普通 summarizer；
- fact check 输入至少包括标题、链接、摘要、来源、发布时间；
- fact check 通过二次检索 + LLM 分析输出可信度判断；
- authority_sources 当前是启发式排序结果，不是严格媒体信誉数据库结论；
- 所有 fact check 用户可见输出应为中文。

### 9. 当前 follow-up workflow 假设
- follow-up 是独立子流程，不应混入普通摘要流程；
- follow-up mode 是一次性临时状态，只对下一条消息生效；
- follow-up 输入至少包括用户追问文本与绑定新闻；
- 回答应优先基于绑定新闻，必要时再补充检索或抓取正文；
- follow-up 输出应是问答化中文回复，而不是新闻播报式摘要。

### 10. 当前 `/log` 浏览能力假设
- latest 视图默认对应活跃 `server.log`；
- archive 浏览不仅依赖 `logs/archive/`，还需要显式纳入当天未归档 hourly rotated logs；
- latest 自动刷新现在是前端可切换开关，不是固定强制行为；
- 行级复制交互当前依赖浏览器剪贴板 API。

## 不应默认作出的假设
以下内容当前没有足够代码证据，不应默认写成事实：
- 已支持多模型供应商切换；
- 已有来源可信度评分；
- `planner.py` 已经是主流程唯一 planner authority；
- `fetch_url` 已经接入主摘要链路；
- `DEFAULT_HOTLIST_LIMIT` 已实际驱动取数；
- 轻量 search source 已经过生产级限频与稳定性验证；
- 当前 search fallback 已具备通用跨语言翻译能力；
- 当前 fact check 已具备专业级外部事实认证能力；
- 当前 follow-up 已经具备持久多轮上下文记忆；
- `/log` 当前已经支持完整的专业日志分析与高级选择能力；
- 系统已经 production-ready；
- 已经支持中文主流新闻站点。
