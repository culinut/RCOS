你正在 RCOS 严格模式下工作，并且刚刚触发了 RCOS audit / patch guard 的失败。

请基于以下失败输出：

[粘贴 audit 或 guard 输出]

执行如下步骤：
1. 先总结失败原因
2. 判断这是：
   - 缺少 RCOS 文档同步
   - 越权修改
   - scope 失控
   - authority 冲突
   - 其他
3. 只提出最小修复方案
4. 输出修复前的 Change Plan
5. 在得到确认前不要写代码

额外要求：
- 不要扩大 scope
- 不要顺手优化
- 优先修复 RCOS 一致性
