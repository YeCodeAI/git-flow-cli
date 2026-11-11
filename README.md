# GitFlow CLI

> A modern CLI utility for automating Git workflows, fast staging, smart commits, and pushing code to GitHub. Built with Python.

## Tech Synk:
- **Python 3.13**
- **uv**: Extremely fast Python package and project manager.
- **Typer**: For building intuitive and robust CLI applications.
- **Rich**: For gorgeous terminal formatting, panels, and colored output.
- **InQuirerPy**: For interactive prompts and seamless UX in the CLI.

--- 

## Features

* **Interactive Auto-Push (`push`):** Automatically checks your remote repository, prompts for a GitHub URL if missing, asks for a commit message interactively (or via flag), runs `git add`, `git commit`, and `git push -u` in one smooth command.
* **Repository Status (`status`):** Clean and stylized visual summary of your current git workspace.

## Installation & Setup:
1) **Clone the repository:**
```bash
git clone [https://github.com/YeCodeAI/git-flow-cli.git](https://github.com/YeCodeAI/git-flow-cli.git)
cd git-flow-cli
```
2) Instalation CLI with uv:
```bash
uv tool install .
```

## Usage:
1) Check repository status:
```bash
git-flow status
```
2) Run automated push:
```bash
git-flow push
```