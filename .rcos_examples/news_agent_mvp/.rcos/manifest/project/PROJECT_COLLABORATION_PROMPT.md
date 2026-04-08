# Project Collaboration Prompt

```text
你正在 `news_agent_mvp` 仓库中协作。该仓库受 RCOS 管控。

## 上下文优先级
始终按以下优先级取事实：
1. manifest/repo_facts.json（若存在）
2. manifest/generated_module_index.yaml（若存在）
3. manifest/project/module_index.yaml
4. manifest/project/CODEBASE_MAP.md
5. manifest/project/PROJECT_BACKGROUND.md
6. manifest/project/PROJECT_STATUS.md
7. manifest/project/PROJECT_ASSUMPTIONS.md
8. 当前任务所需代码文件
9. 人类未明说的猜测

## 每日协作硬规则
1. 先 plan，再 code。
2. 默认最小 scope、最小 attention。
3. 未确认前，不做顺手清理、不加 bonus 重构。
4. 若信息不足，先问最小必要问题，不要猜。
5. 不要复制 authority 模块已有逻辑。
6. 如果 scope 必须扩大，要明确说明：
   - 为什么当前文件不够；
   - 新增读取哪些文件；
   - 这会带来什么风险。

## 输出顺序（非 trivial 任务必须遵守）
1. Scope Check
2. Context Summary
3. Change Intent
4. Change Plan
5. Implementation 或 Full-file Output / Patch
6. Verification
7. RCOS Update Impact

## 这个项目的协作约束
- 主编排 authority 默认为 `app/services/agent.py`；
- 当前实际 planner authority 也默认为 `app/services/agent.py`；
- `app/services/planner.py` 当前是 planner 辅助模块，不应假设已经接线；
- 配置 authority 默认为 `app/config/settings.py`；
- 热榜工具 authority 默认为 `mcp_news_server.py`；
- 工具桥接 authority 默认为 `app/services/mcp_client.py`；
- 时效性 authority 默认为 `app/services/freshness.py`；
- 评分组装 authority 默认为 `app/services/scoring.py`；
- 本地化 authority 默认为 `app/services/enrichment.py`；
- 摘要 authority 默认为 `app/services/summarizer.py`。

如果某个改动会改变这些 authority，必须在计划阶段明确提出，而不是实现后再解释。

## 针对本项目的特别提醒
- 当前系统仍是单轮 agentic workflow，不要把未来能力写成当前能力；
- 不要假设 `planner.py` 已经是主流程入口；
- 不要在 orchestration 文件里重复实现已有 scoring / enrichment / summarizer 逻辑；
- 涉及 `.env.example`、`settings.py`、启动脚本时，要特别检查配置名是否一致；
- 涉及数据源与抓取时，要区分“已有工具能力”和“主 pipeline 实际是否调用”；
- 涉及 UI 时，尽量只碰 `app/web/` 与 `app/api/routes.py`，不要把展示逻辑重新塞回服务层；
- `max_steps` 当前是弱语义参数；若某次改动要让它真正生效，必须在计划中明确说明行为变化。

## RCOS Update Awareness（必须显式输出）
每次经批准的代码改动后，必须单独输出：

## RCOS Update Impact
- 是否需要更新 PROJECT_STATUS.md？为什么？
- 是否需要更新 CODEBASE_MAP.md？为什么？
- 是否需要更新 PROJECT_ASSUMPTIONS.md？为什么？
- 是否需要更新 module_index.yaml？为什么？

如果需要，请提供对应文件的完整更新内容，而不是只说“建议更新”。
```
