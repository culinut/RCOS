# PROJECT_RCOS_EVOLUTION

## 目的

本文记录 `SanXing-AsItIs` 作为 RCOS tenant project 的 DNA 状态。

它用于追踪：

- 当前 tenant 正在遵守哪个 DNA 协议版本
- 当前 tenant 已吸收了本体 RCOS 的哪些核心 DNA
- 当前 tenant 本地产生了哪些候选进化项
- 哪些 DNA 已上行同步到本体 RCOS
- 哪些来自本体 RCOS 的 DNA 仍待下行吸收

---

## Tenant 身份

- `tenant_project`: `SanXing-AsItIs`
- `tenant_role`: `RCOS tenant project`
- `contributor_project_tag`: `SanXing-AsItIs`

---

## 当前 DNA 基线

- `tenant_protocol_version`: `rcos-evolution-v1`
- `tenant_core_dna_base_release`: `core-dna-bootstrap-2026-04-09`

说明：

- 当前项目已进入 RCOS DNA system 的第一版协议
- 当前记录的 `tenant_core_dna_base_release` 是本次 DNA system 正式落盘时的基线快照
- 该值用于标记“本项目当前已知吸收到的本体 RCOS 核心 DNA 基线”

---

## 已吸收的核心 DNA

### DNA-2026-0001: `project-roadmap-first-class-file`

状态：

- `adopted`

说明：

- `PROJECT_ROADMAP.md` 被提升为正式 project-specific RCOS 文件
- 其职责是定义推荐实现顺序、里程碑、交付物与验收标准

### DNA-2026-0002: `contributor-tagged-upstream-sync`

状态：

- `adopted`

说明：

- tenant project 发现可复用 RCOS 改进时，应先本地沉淀
- 再显式标记 contributor project
- 在人类确认后再提议同步到本体 RCOS

### DNA-2026-0003: `contributor-seed-matching`

状态：

- `adopted`

说明：

- 若要同步到本体 RCOS 的 example seed，应优先落到与 contributor project 对应的 seed 路径
- 不应把某个项目的 RCOS 进化误写进无关 seed

### DNA-2026-0004: `decoupled-core-seed-artifact-cadence`

状态：

- `adopted`

说明：

- 本体主 `.rcos`、example seed、zip artifact 应具有不同同步节奏
- 默认不要求 seed 与 zip 跟随主 DNA 的每次小演化一起更新

---

## 本地候选 DNA

当前暂无尚未登记到本体 RCOS 的额外候选项。

后续若出现新的 tenant-local RCOS 进化，应按以下状态登记：

- `local_only`
- `candidate_upstream`
- `promoted_upstream`
- `candidate_downstream_intake`
- `intake_applied`

---

## 本次已上行同步的 DNA

本次已上行同步到本体 RCOS 的内容包括：

- `DNA-2026-0001`
- `DNA-2026-0002`
- `DNA-2026-0003`
- `DNA-2026-0004`

说明：

- 本次属于 DNA system 初始化阶段
- 因此主 `.rcos`、example seed 与 zip artifact 被允许进行一次特批例外同步

---

## 待下行吸收的本体 DNA

当前无待下行吸收项。

后续如果本体 RCOS 新增 promoted DNA，而本项目暂未吸收，应在此处记录：

- DNA 标识
- 是否需要 intake
- 为什么暂缓 intake
- 下次评估时机

---

## Seed 与 Artifact 节奏约束

### 默认规则

- tenant 项目中的 RCOS DNA 可先同步到本体主 `.rcos`
- example seed 不应默认跟随每次主 DNA 微小变化立即更新
- zip artifact 也不应默认跟随每次 seed 变化立即重打包

### 本次例外

本次为了初始化 DNA system，允许一次计划外同步：

- 同步 tenant DNA 到本体主 `.rcos`
- 同步对应 example seed
- 重打包 zip artifact

此后恢复默认分离节奏。

---

## 维护规则

以下情况发生时，应更新本文：

- tenant 吸收了新的本体 DNA
- tenant 产生了新的 local candidate DNA
- 某个 candidate 被 promotion 到本体 RCOS
- 某个 promoted DNA 被本项目暂缓 intake
- 当前 `tenant_protocol_version` 或 `tenant_core_dna_base_release` 变化
