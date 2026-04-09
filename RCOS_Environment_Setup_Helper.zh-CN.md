# RCOS 环境配置辅助指南

English version: [RCOS_Environment_Setup_Helper.md](./RCOS_Environment_Setup_Helper.md)

这是一份可选辅助文档。

如果你还不熟悉环境配置，或者希望先把 Windows、WSL、Cursor 和 coding agent 的基础环境准备好，再进入正式的 RCOS 项目启动流程，可以先使用这份文档。

适合这种情况的读者：

- 刚开始接触 WSL、Ubuntu 或 Python 开发环境
- 不熟悉 git repo、Cursor、或 coding agent 插件配置
- 希望先把环境问题拆开，不和项目设计讨论混在一起

## 推荐使用方式

建议你：

1. 先单独开一个新的对话模型 conversation
2. 先把下面 prompt 第一段中的项目名称和 high-level 描述改成你自己的
3. 再把整段 prompt 贴进去
4. 跟着回复一步步完成环境配置
5. 环境准备完成后，再回到正式的 RCOS 项目启动流程

## 可直接复制的环境配置 prompt

在粘贴之前，建议先只改第一段里这两类内容：

- 你的项目类型或名称
- 你的项目 high-level 描述

其余环境配置要求通常可以直接保留。

    我想在一台 Windows 11 笔记本上开始一个 Python FastAPI server project。项目主题大致会是一个用于存放多媒体兴趣收藏的系统，但这个对话里不需要展开项目细节；我会在另一个对话中详细说明项目本身。

    请在这个对话中只帮助我完成初始环境配置，并尽量按步骤引导我，不要跳步。请把每一步拆得足够具体，默认我是新手。

    目标是帮助我完成这些事情：
    - 配置 WSL2（Ubuntu）
    - 安装必要的基础库，以及 screen
    - 告诉我怎么启动和关闭 WSL 系统
    - 创建 ~/Workspace
    - 创建一个新的 git repo 目录并初始化，目录名称应与我在第一段里提供的项目名称或 high-level 描述一致，暂时不要 commit 任何东西
    - 在 Windows 上安装 Cursor，并打开 WSL 中的 git repo 目录作为工作项目
    - 在 Cursor 中配置合适的 coding agent / Codex 插件，确保它可以以项目文件夹为 context 进行对话，并且具有访问项目文件的权限

    请注意：
    - 这个对话的目标只是环境配置，不是项目设计，也不是写代码
    - 如果某一步依赖我先完成前一步，请明确停下来等待我确认
    - 如果存在多种做法，请优先给出最稳、最适合新手的一种
    - 如果需要我在 Windows 或 WSL 中分别执行命令，请清楚标注

## 完成之后做什么

当环境准备完成后，回到主启动指南继续：

- [RCOS_Project_Startup_Guide.zh-CN.md](./RCOS_Project_Startup_Guide.zh-CN.md)

此时再进入正式的 RCOS 项目启动流程会更顺畅。
