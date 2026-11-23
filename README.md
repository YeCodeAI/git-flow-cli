# git-flow-cli

> An interactive command-line utility built with Python to streamline routine Git and GitHub workflows right from your terminal.

## Features

- **Push to the repository** — Guided staging (`git add .`), committing with a custom message, linking a remote repository if missing, and pushing changes.
- **Show all commits in the repository** — Displays the project's full commit history (hash, timestamp, author, and message) in a clean, formatted terminal table powered by Rich.
- **Create a new GitHub repository** — Creates a public or private GitHub repository via GitHub CLI (`gh`), optionally links it as `origin`, and pushes existing local commits.

## Tech Stack

- **Python 3.13+**
- **[InquirerPy](https://github.com/kazhala/InquirerPy)** — Interactive CLI prompts and menus
- **[Rich](https://github.com/Textualize/rich)** — Styled terminal output and formatted tables
- **[uv](https://github.com/astral-sh/uv)** — Fast Python package and tool management
- **[Ruff](https://github.com/astral-sh/ruff)** — Linting and code formatting

## Prerequisites

Make sure the following tools are installed and available in your `PATH`:

- [Python 3.13+](https://www.python.org/)
- [Git](https://git-scm.com/)
- [uv](https://docs.astral.sh/uv/)
- [GitHub CLI (`gh`)](https://cli.github.com/) (authenticated via `gh auth login`, required for creating repositories)

## Installation

Clone the repository and install the CLI tool globally with `uv`:

```bash
git clone [https://github.com/YeCodeAI/git-flow-cli.git](https://github.com/YeCodeAI/git-flow-cli.git)
cd git-flow-cli
uv tool install .
```

## Usage
Run the tool inside any project directory:
```bash
git-flow-cli
```

## Project structure
```text
git-flow-cli/
├── .github/
│   └── workflows/
│       └── ci.yml          # GitHub Actions CI (Ruff lint & format check)
├── src/
│   └── git_flow_cli/
│       ├── tools/
│       │   ├── __init__.py
│       │   ├── commit_lists.py  # Commit history table viewer
│       │   ├── create_repo.py   # GitHub repository creation via gh
│       │   └── push.py          # Guided git add / commit / push
│       ├── main.py              # CLI entry point and interactive menu
│       ├── runner.py            # Subprocess command execution wrapper
│       └── ui.py                # Rich console output and table styling
├── pyproject.toml
├── ruff.toml
└── README.md
```

## License
This project is open-source and available under the MIT License.