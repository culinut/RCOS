# CURRENT_BASELINE

## 当前系统状态

项目已具备基础运行骨架，但尚未进入“可用产品”阶段。

---

## 已存在能力

- FastAPI 最小应用入口
- 根路由 health endpoint
- 请求活跃检测与空闲停止逻辑
- systemd socket activation 运行链路
- 基础安装脚本（systemd 单元安装）
- Git 仓库初始化

已确认对应文件：

- `app/main.py`
- `app/lifecycle.py`
- `systemd/sanxing.service`
- `systemd/sanxing.socket`
- `scripts/install-systemd.sh`

---

## 缺失核心能力（阻塞项）

👉 评分系统（Scoring Model）

当前缺失：

- PDF → 结构化语义
- 行为 → 分数映射
- UI 输入模型
- check-in 提交闭环
- 已确认的 SQLite schema
- 导出 PDF 实现

---

## 当前系统类型

不是：

- 完整应用
- 数据产品

而是：

👉 一个“尚未定义语义核心的系统框架”

---

## 当前优先级排序

1. 评分语义结构化（最高）
2. 数据结构定义
3. API 完整化
4. UI 实现

---

## 已确认占位资源

- `data/SanXing.db` 已存在，但当前为空文件
- `pdf/export/` 已存在，但当前为空目录
- `pdf/template/` 已存在，但当前为空目录
- `.rcos/manifest/project/三省书_monthly.pdf` 已存在，作为评分语义参考源
- `.rcos/manifest/project/scoring_model_seed.json` 已存在，作为当前评分逻辑工作基线

这意味着：

- 仓库已经为 storage / export / PDF 参考材料预留位置
- 但这些位置目前不能视为功能已落地

补充说明：

- 已能确认 seed 在结构上是完整的：
  - 3 个时间切片
  - 6 个六度预读项
  - 8 个八正道预读项
  - 12 个评分维度
- 但由于 PDF 为扫描件、当前环境缺少 OCR / PDF 文本提取工具，尚未完成逐字级源文核对

---

## 禁止事项（当前阶段）

- 不优化 UI
- 不扩展功能
- 不引入 AI 分析
- 不做性能优化

---

## 当前开发原则

- 最小改动
- 明确意图
- 结构优先
- 语义优先于实现
- 已确认事实优先于计划性描述
