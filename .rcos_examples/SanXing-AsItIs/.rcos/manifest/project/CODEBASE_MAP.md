# CODEBASE_MAP

## 代码库定位

当前仓库是一个“已有最小运行骨架，但尚未进入完整产品实现”的 SanXing 数字 check-in 项目。

其现状更接近：

- 已有运行壳层
- 已有 RCOS 项目上下文
- 已有评分语义种子
- 尚未形成完整 check-in / storage / UI / export 功能链路

---

## 已确认入口点

### 应用入口

- `app/main.py`

职责：

- 创建 FastAPI 应用
- 注册请求活动 middleware
- 提供根路由 health endpoint
- 提供 `/favicon.ico`

### 生命周期与空闲控制

- `app/lifecycle.py`

职责：

- 管理请求活跃计数
- 记录最近活动时间
- 在空闲超时后停止 `sanxing.service`

---

## 已确认运行链路

### systemd socket / service

- `systemd/sanxing.socket`
- `systemd/sanxing.service`
- `scripts/install-systemd.sh`

当前运行方式：

1. `sanxing.socket` 监听 `8123`
2. `sanxing.service` 使用 `.venv/bin/uvicorn app.main:app --fd 3`
3. 安装脚本会把 systemd 单元复制到 `/etc/systemd/system`
4. socket 被启用后可按需拉起服务
5. 应用空闲时，`app/lifecycle.py` 会主动停止 `sanxing.service`

这说明：

- systemd socket activation 不是纯计划项，而是仓库中已有明确实现
- 当前运行耦合了本机路径与本机 `.venv`

---

## 目录结构（已确认）

### `app/`

当前仅确认存在：

- `main.py`
- `lifecycle.py`

尚未确认有：

- 独立 router 模块
- schema / model 模块
- storage 层实现
- check-in 业务逻辑模块

### `data/`

当前存在：

- `data/SanXing.db`

现状：

- 文件已创建
- 当前为空文件
- 尚无已确认 schema

因此：

- 可以认为仓库已为 SQLite 留出位置
- 不能认为存储层已经实现完成

### `pdf/`

当前存在目录：

- `pdf/export/`
- `pdf/template/`

现状：

- 两个目录当前为空

当前理解：

- `pdf/export/` 预期用于保存由 check-in 记录生成的导出 PDF
- 导出目标是模拟手填在纸质《三省书》上的效果
- `pdf/template/` 预期用于保存后续导出所需模板资源

目前仍不能确认：

- 实际导出逻辑是否已开始实现
- 模板文件是否已经确定

---

## RCOS / 语义材料

### 项目级 RCOS 文件

- `.rcos/manifest/project/PROJECT_BACKGROUND.md`
- `.rcos/manifest/project/PROJECT_STATUS.md`
- `.rcos/manifest/project/PROJECT_ASSUMPTIONS.md`
- `.rcos/manifest/project/CURRENT_BASELINE.md`
- `.rcos/manifest/project/module_index.yaml`

### 评分语义种子

- `.rcos/manifest/project/scoring_model_seed.json`

用途：

- 作为《三省书》评分维度、行为锚点、时间切片结构的当前语义种子

已确认的结构：

- `time_slices = morning / midday / evening`
- `pre_read_requirements.liudu = 6 项`
- `pre_read_requirements.bazhengdao = 8 项`
- `dimensions = 12 项`

当前验证边界：

- 已确认结构完整且与项目方向一致
- 尚未在本机环境中完成基于扫描件 PDF 的逐字级文字核对

### 扫描件 PDF 参考源

- `.rcos/manifest/project/三省书_monthly.pdf`

已确认：

- 文件存在
- 为 64 页 PDF

用途：

- 作为当前评分逻辑 JSON 的主要参考来源之一
- 后续应作为语义核对材料，而非自动等同于最终结构化模型

当前限制：

- 该 PDF 更接近扫描件来源
- 本机当前没有 OCR / PDF 文本提取工具
- 因此当前只能完成结构一致性核对，不能完成严格的逐条原文复录校验

---

## 模块状态解读

`module_index.yaml` 当前更像“目标模块规划 + 部分现状标记”，不能直接视为“已实现模块清单”。

按已确认源码判断：

- 已有最小 `api` 壳层
- 已有运行时/生命周期控制
- 尚未看到独立 `checkin` 模块实现
- 尚未看到独立 `storage` 模块实现
- 尚未看到 `ui` 实现
- 尚未看到 `eightfold_display` 实现
- 尚未看到 `export_pdf` 实现

---

## 当前主数据流（已确认到的最小链路）

当前实际链路只有：

1. 请求进入 FastAPI
2. middleware 更新活跃状态
3. 根路由返回 health 响应
4. 空闲 watcher 在超时后停止 service

尚未确认的后续链路：

- 八正道预读展示
- check-in 提交
- SQLite 写入
- 导出 PDF

---

## 当前缺口

从“目标产品流”到“当前仓库状态”的主要缺口包括：

- 评分语义尚未落成可执行代码结构
- check-in 数据模型未在代码中出现
- SQLite 仅有空文件，没有已确认 schema
- UI 与分步交互未落地
- 导出 PDF 目录存在，但实现未出现

---

## 结论

当前代码库的真实状态是：

一个带有 FastAPI + systemd 运行骨架、RCOS 项目上下文、评分语义种子和若干占位目录的早期仓库。

它已经具备：

- 可运行的最小服务入口
- 明确的产品方向
- 明确的语义建模优先级

但尚未具备：

- 可执行的 check-in 业务闭环
- 可用的数据存储实现
- 可操作的 UI
- PDF 导出功能
