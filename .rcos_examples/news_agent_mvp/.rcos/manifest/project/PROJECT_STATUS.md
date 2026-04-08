# Project Status

## 当前阶段
项目当前处于 **可运行 MVP / 单轮 agentic workflow 原型** 阶段。

它已经不是单文件脚本，而是一个有清晰目录分层的 Python 项目：
- FastAPI 提供 API 与浏览器页面；
- 独立工具脚本提供 RSS 热榜、轻量搜索与 URL 抓取能力；
- 服务层负责规划式判断、查询生成、检索、评分、本地化和摘要；
- 日志、重启与简单观测能力已经接入。

但它仍不是完整 agent：
- 没有循环决策；
- 没有长期记忆；
- 没有 reflection；
- 没有来源可信度模型；
- 没有基于失败状态自动补抓或补搜。

## 现在已经可以工作的部分

### 1. 基本主链路已打通
从当前源码可确认，系统已经可以：
1. 通过 `/query` 接收用户问题；
2. 通过 `/query-async` + `/query-status/{task_id}` 提供异步查询任务与进度查询；
3. 用 LLM 判断是否需要执行新闻检索；
4. 生成 2-5 个结构化检索 query，并同时产出 search-friendly query 变体；
5. 对 RSS source 与轻量 search source 执行多源 retrieval，并在 search 0 结果时尝试 fallback query；
6. 对结果做 normalization、dedup 与基于 query match + recency 的 rerank；
7. 用 LLM 打相关性分；
8. 通过 `freshness.py` 的统一入口计算时效性分与标签；
9. 生成中文标题 / 中文摘要 / 相关标签；
10. 生成最终总结、重点条目和追问建议；
11. 通过 `/chat` 展示结果，并在普通查询等待期间显示 spinner、步骤文案和进度条。

### 1.1 单条精选新闻已支持事实核查子流程
当前源码还支持从精选新闻卡片发起独立 fact check：
1. 用户点击候选卡片上的“事实核查”按钮；
2. 前端先追加“事实核查：{标题}”用户气泡；
3. 前端显示 spinner、步骤文案和进度条；
4. 后端通过异步 task 执行独立 fact-check pipeline；
5. 返回专用 `mode="fact_check"` 结构；
5. 前端用专门样式展示可信度、依据说明、权威信源和一致性判断。

### 1.2 单条精选新闻已支持一次性追问子流程
当前源码还支持从精选新闻卡片发起一次性 follow-up mode：
1. 用户点击候选卡片上的“追问”按钮；
2. 前端进入一次性追问模式，并显示轻量提示；
3. 用户下一条消息被路由到 follow-up pipeline；
4. 提交后前端显示 spinner、步骤文案和进度条；
5. 回答完成后自动退出追问模式；
6. 后续消息恢复普通新闻 agent 流程。

### 2. 工具层已有最小可用实现
`mcp_news_server.py` 当前已实现：
- `list_sources`
- `get_hotlist`
- `search_news`
- `fetch_url`

`hotlists.yaml` 当前包含 3 个 source：
- `hn_frontpage`
- `hn_newest`
- `reddit_openai`

### 3. Web / 运行辅助能力可直接使用
当前已有：
- `GET /health`
- `GET /chat`
- `GET /refresh`
- `GET /log`
- `GET /log/raw`
- `POST /query`
- `POST /query-async`
- `POST /fact-check`
- `POST /fact-check-async`
- `POST /follow-up`
- `POST /follow-up-async`
- `GET /query-status/{task_id}`

当前日志机制还包括：
- 活跃日志持续写入 `logs/server.log`；
- 每小时第一条日志触发 hourly rollover，生成 `server.log.YYYY-MM-DD-HH`；
- 跨天后的第一批日志会将当天之前的 hourly logs 归档到 `logs/archive/yyyy/mm/dd/hh/`。
- `/log` 现已支持浏览 archive 中实际存在的年月日小时日志文件，并可返回最新 `server.log` 视图；
- `/log` 现在还会 pick up 当天已产生、但尚未归档进 archive 目录结构的 hourly rotated log files；
- latest `server.log` 视图的 5 秒自动刷新现在可切换开关；
- `/log` 页面支持行级复制交互，可从某一行复制到结尾，或先设起点再复制区间。

### 4. 排序与本地化能力已经进入产品返回
返回结果中已经包含：
- `freshness_score`
- `freshness_label`
- `relevance_score`
- `relevance_reason`
- `relevance_label`
- `title_zh`
- `summary_zh`
- `total_score`

这说明当前系统已经不只是“抓取 + 总结”，而是“query-driven retrieval + 排序 + 中文展示”。

### 5. 事实核查结果已有专用返回结构
fact check 不再复用普通摘要输出，而是返回独立结构，至少包含：
- `mode = "fact_check"`
- `news_title`
- `credibility_score`
- `credibility_label`
- `overview`
- `evidence_summary`
- `authority_sources`
- `consistency_assessment`

### 6. 追问结果已有专用返回结构
follow-up 也不再复用普通摘要输出，而是返回独立结构，至少包含：
- `mode = "follow_up"`
- `news_title`
- `follow_up_question`
- `question_type`
- `answer`
- `supporting_points`
- `used_context`

### 7. 主查询流程已有真实步骤驱动的等待反馈
当前 `/chat` 中的普通查询、事实核查和追问都不再只是前端静默等待：
- 前端先创建一个处理中占位卡；
- 占位卡显示 spinner、当前步骤文案和进度条；
- 后端通过轻量异步 task 维护 `queued / running / done / failed` 状态；
- 普通查询步骤至少覆盖 `planner / retrieval / relevance_scoring / enrichment / summarizing / done`；
- 事实核查步骤至少覆盖 `fact_check_query_generation / fact_check_retrieval / fact_check_analysis / fact_check_authority_sources / done`；
- 追问步骤至少覆盖 `follow_up_classification / follow_up_retrieval / follow_up_context_building / follow_up_answering / done`。

## 当前限制

### 1. 主流程里的 planner 仍是内联实现
虽然仓库里存在 `app/services/planner.py`，但 `run_agent()` 当前没有调用它，而是自己内联构造 planner prompt、调用 LLM 并解析 JSON。

这意味着：
- `planner.py` 目前更像备用/未接入模块；
- planner authority 事实上仍在 `app/services/agent.py`。

### 2. 仍是单轮线性执行
当前流程固定是：
- planner
- query generation
- multi-source retrieval
- dedup / rerank
- relevance scoring
- enrichment
- summarizer

没有“信息不够再抓一次”的 loop，也没有条件性多工具链路。

### 3. 信息源仍然很窄
当前虽然从单一热榜升级为“RSS + 轻量搜索源”，但默认 RSS source 仍只有 3 个，轻量搜索也只有一个最小实现，不足以支撑泛新闻场景，也不足以覆盖中文新闻场景。

### 4. 跨语言 search fallback 仍是启发式 v1
当前 search 分支已经支持 search-friendly query 和 0 结果 fallback，但 fallback 仍是启发式规则，不是通用翻译检索层。

### 5. `fetch_url` 已存在，但未接入主 pipeline
工具层能抓正文预览，但 `run_agent()` 当前没有把 `fetch_url` 纳入正式处理链路。

### 6. fact check 仍是 MVP 级可信度分析
当前 fact check 主要基于二次检索 + LLM 分析，不是严格的外部事实认证系统，也没有接入专门的媒体信誉数据库或专业 fact-check API。

### 7. follow-up mode 是一次性临时模式
当前 follow-up mode 只对下一条消息有效，不是持久会话状态，也没有长期 memory。

### 8. `max_steps` 尚未实际生效
- schema 暴露了 `max_steps`；
- API 将它传入 `run_agent()`；
- 前端也固定发 `max_steps: 3`；
- 但当前主流程并未按这个参数动态控制步骤数。

### 9. 配置示例与实现不一致
`.env.example` 仍是旧变量名，而当前代码实际读取的是：
- `HOST` / `PORT`
- `MODEL_PROVIDER` / `MODEL_NAME`
- `OPENAI_API_KEY`
- `DEFAULT_SOURCE_ID` / `DEFAULT_MAX_STEPS` / `DEFAULT_HOTLIST_LIMIT`
- `DEFAULT_RETRIEVAL_QUERY_COUNT` / `DEFAULT_RETRIEVAL_TOP_N`
- `DEFAULT_RETRIEVAL_RSS_LIMIT` / `DEFAULT_RETRIEVAL_SEARCH_LIMIT`
- `GOOGLE_NEWS_RSS_LOCALE`

## 已知问题 / 风险

### 1. 配置文档与实现不一致
这是当前最明确的仓库级事实不一致：
- `.env.example` 使用 `ZHIPU_API_KEY`、`ZHIPU_MODEL`、`API_HOST`、`API_PORT`；
- 实际代码使用 OpenAI 与另一组配置名。

### 2. retrieval query generation 仍依赖 prompt
query generation 目前通过 LLM prompt 生成 2-5 个查询，并补充 search-friendly query。虽然这比“planner 只选固定 source”更灵活，但查询质量、覆盖度和稳定性仍受 prompt 与模型输出影响。

### 3. 工具调用依赖本地 Python 子进程
`mcp_client.py` 通过 `subprocess.run(["python", ...])` 调工具脚本，当前没有网络化 service discovery、没有超时策略、也没有重试机制。

### 4. 重启脚本带有强机器路径假设
`scripts/restart.sh` 把项目目录写死为 `/home/culinut/Workspace/news_agent_mvp`，当前显然偏个人环境，不适合直接泛化部署。

### 5. `/log/raw` 仍只查看活跃日志
虽然 `/log` 页面现已支持 archive 浏览，但 `/log/raw` 仍只读取当前 `logs/server.log`，没有 archive raw 输出入口。

### 6. 质量闭环仍缺失
当前虽然能评分，但还不能：
- 自动发现摘要失败；
- 自动补抓正文；
- 按历史效果修正行为；
- 建立来源可信度加权。

### 7. live 外部检索路径尚未完成真实联调验证
当前 retrieval layer v1 已有端到端单测，但主要依赖 mock。`search_news` 的真实外部返回质量、限频表现和失败回退路径，还没有形成更完整的运行期验证结论。

### 8. 当前 fallback 对非英文主题的覆盖仍有限
检索层已经能在中文 query 0 结果时尝试 search fallback，但当前 fallback 仍偏规则驱动，主题泛化能力有限。

### 9. fact check 的权威性排序仍是启发式
当前 authority_sources 的排序主要依赖检索结果与 LLM 分析，不是严格的机构级信誉排序系统。

### 10. follow-up 回答仍是 MVP 级上下文问答
当前 follow-up 主要基于绑定新闻、必要时补充检索、按需抓取正文，然后生成一次性问答式回复；还不是多轮对话 agent。

### 11. `/log` 的复制交互仍是 MVP 级实现
当前 `/log` 的行级复制更接近 code review 风格的轻量交互，但还不是完整的多选日志分析工具。

### 12. 当前等待反馈仍是轮询式，而非流式推送
当前三类等待反馈都基于前端轮询 task 状态，而不是 WebSocket / SSE 流式推送。
这对 MVP 演示已经足够，但仍不是最低延迟或最细粒度的实时状态同步。

## 下一步优先级
结合当前源码事实，较合理的下一步优先级是：

### 1. 先清理“代码事实 vs RCOS / 配置文档”不一致
优先修正：
- `.env.example`
- planner authority 表述
- source / prompt 的单点写死问题
- `max_steps` 的语义

### 2. 把 planner authority 收敛到单一实现
要么让 `run_agent()` 正式调用 `planner.py`，要么删除重复实现，避免后续漂移。

### 3. 扩展 source 与正文抓取能力
在现有 query-driven retrieval 基础上，优先引入：
- 更多稳定 source；
- `fetch_url` 的主流程接入；
- 更细的 source 选择逻辑。

### 4. 引入更明确的排序因子设计
当前 `total_score = relevance * 0.7 + freshness * 0.3` 是硬编码规则。

另外，时效性分与时效性标签现已统一由 `app/services/freshness.py` 单点产出，避免在 `scoring.py` 侧重复解析发布时间。后续若要提升质量，较可能从：
- 权重策略；
- 来源可信度；
- 用户意图类型；
- 结果覆盖度
继续演进。
