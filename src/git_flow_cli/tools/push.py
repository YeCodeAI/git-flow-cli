import pathlib

from InquirerPy import inquirer
from InquirerPy.validator import EmptyInputValidator

from ..runner import Runner
from ..ui import UI

def push() -> None:
    runner = Runner()
    ui = UI()

    # Check and create .git
    ui.log('Step 1: Checking .git...')

    if not pathlib.Path('.git').exists():
        ui.warning('.git not created. Starting initialization...')
        runner.run(['git', 'init'])
        ui.success('.git to live successfully!')
    ui.info('.git is found!')

    # Check and adding remote
    remote_check = runner.run(['git' ,'remote', 'get-url', 'origin'])

    if 'error' in remote_check.stderr.lower() or not remote_check.stderr.strip():
        ui.warning('Repository is not found')

        repo_url = inquirer.text(
            message='Enter the URL of your GitHub repository:',
            default='https://github.com/',
            validate=EmptyInputValidator()
        ).execute()

        if repo_url:
            ui.info('Linking the repository...')
            runner.run(['git' ,'remote', 'add' ,'origin', repo_url])

    # Add all files
    ui.log('Step 2: Adding all files(git add .)')

    add_res = runner.run(['git', 'add', '.'])

    if add_res.returncode != 0:
        ui.error('Error adding files!')

    # Commit
    ui.log('Step 3: Preparing a commit')

    commit_msg = inquirer.text(
        message='Enter the commit',
        default='Update project',
        validate=EmptyInputValidator()
    ).execute()

    runner.run(['git', 'commit', '-m', commit_msg])

    # Push project
    ui.log('Step 4: Pushing changes to the remote repository (git push)...')

    runner.run(['git', 'branch', '-M', 'main'])
    push_result = runner.run(['git', 'push', '-u', 'origin', 'main', '--force'])

    if 'error' in push_result.stderr.lower() or 'fatal' in push_result.stderr.lower():
        ui.error('Error while sending to GitHub!')

    else:
        ui.success('Code successfully sent to GitHub!')
        if push_result:
            ui.log(push_result.stdout.strip())

