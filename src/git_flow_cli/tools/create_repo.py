from pathlib import Path

from InquirerPy import inquirer
from InquirerPy.validator import EmptyInputValidator

from ..runner import Runner
from ..ui import UI

def create_repo():
    ui = UI()
    runner = Runner()

    ui.rule('Create GitHub Repository')
    
    # Check auth
    ui.log('Step 1: Check auth')
    auth_check = runner.run(['gh', 'auth', 'status'])
    if auth_check.returncode != 0:
        ui.error('GitHub CLI (gh) is not found or not authenticated. Run `gh auth login` first.')
        return
    
    # Repository parameters
    ui.log('Step 2: Requesting repository parameters')
    default_name = Path.cwd().name.strip()

    repo_name = inquirer.text(
        message='Repository name:',
        default=default_name,
        validate=EmptyInputValidator('Repository name cannot be empty')
    ).execute()

    visibility = inquirer.select(
        message='Repository visibility:',
        choices=['public', 'private'],
        default='public',
    ).execute()

    description = inquirer.text(
        message='Description (optional):',
        default='',
    ).execute()

    cmd = ['gh', 'repo', 'create', repo_name, f'--{visibility}']

    if description:
        cmd.extend(['--description', description])

    in_git_repo = runner.run(['git', 'rev-parse', '--is-inside-work-tree']).returncode == 0
    link_remote = False

    if in_git_repo:
        link_remote = inquirer.confirm(
            message='Link current local repository to this new remote (origin)?',
            default=True
        ).execute()
        if link_remote:
            cmd.extend(['--source', '.', '--remote', 'origin'])

    ui.info(f'Creating "{repo_name}" ({visibility}) on GitHub...')
    result = runner.run(cmd)

    if result.returncode != 0:
        ui.error(result.stderr or 'Failed to create repository.')
        return

    ui.success(f'Repository "{repo_name}" created successfully!')