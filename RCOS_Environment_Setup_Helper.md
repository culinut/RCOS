# RCOS Environment Setup Helper

中文版: [RCOS_Environment_Setup_Helper.zh-CN.md](./RCOS_Environment_Setup_Helper.zh-CN.md)

This is an optional helper document.

If you are not yet comfortable with environment setup, or you want to prepare Windows, WSL, Cursor, and coding-agent access before entering the formal RCOS project startup flow, use this document first.

This is especially useful if you:

- are new to WSL, Ubuntu, or Python development environments
- are not yet comfortable with git repos, Cursor, or coding-agent plugin setup
- want to separate environment work from project-definition work

## Recommended usage

A good pattern is:

1. open a fresh conversation with your conversational model
2. first edit the first paragraph so the project name and high-level description match your own project
3. then paste the full prompt
4. follow the replies step by step until the environment is ready
5. return to the formal RCOS project startup flow once setup is complete

## Copy-ready prompt for environment setup

Before pasting it, usually only these parts need to be customized in the first paragraph:

- your project type or project name
- your own high-level project description

The rest of the environment-setup request can usually stay the same.

    I want to start a Python FastAPI server project on a Windows 11 laptop. The project will probably be a system for storing and organizing multimedia interests, but the project details are not important in this conversation; I will describe the actual project in another thread.

    In this conversation, please help me only with initial environment setup, and guide me step by step without skipping ahead. Assume I am a beginner and break each step down clearly.

    The goal is to help me do the following:
    - set up WSL2 (Ubuntu)
    - install the necessary base packages, including screen
    - explain how to start and shut down the WSL system
    - create ~/Workspace
    - create a new git repo directory and initialize it; the directory name should match the project name or high-level description from the first paragraph, but do not commit anything yet
    - install Cursor on Windows and open the WSL git repo directory as the working project
    - configure an appropriate coding-agent / Codex plugin in Cursor so it can talk with the project folder as context and has permission to access project files

    Important notes:
    - the goal of this conversation is only environment setup, not project design and not writing code
    - if one step depends on me finishing a previous step, stop and wait for my confirmation
    - if there are multiple ways to do something, prefer the safest beginner-friendly option first
    - if I need to run commands separately in Windows and WSL, label that clearly

## What to do after setup

Once the environment is ready, return to the main startup guide:

- [RCOS_Project_Startup_Guide.md](./RCOS_Project_Startup_Guide.md)

From there you can continue with the formal RCOS project startup flow.
