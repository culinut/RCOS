你现在在一个 RCOS 约束的项目中工作。

上下文优先级：
1. .rcos/manifest/project/CODEBASE_MAP.md
2. .rcos/manifest/project/PROJECT_BACKGROUND.md
3. .rcos/manifest/project/PROJECT_STATUS.md
4. .rcos/manifest/project/PROJECT_ASSUMPTIONS.md
5. .rcos/manifest/project/module_index.yaml
6. 当前任务文件

要求：
- 先输出 Scope Check / Context Summary / Change Intent / Change Plan
- 在我确认前不要写代码
- 不要默认读取整个 repo
- 仅在必要时追加读取文件，并说明原因
- 缺信息就提问，不要猜

代码变更确认后，必须额外输出：

## RCOS Update Impact
检查并说明是否需要同步更新：
- PROJECT_STATUS.md
- CODEBASE_MAP.md
- PROJECT_ASSUMPTIONS.md
- module_index.yaml

当前任务：
[在这里写任务]
