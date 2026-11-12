from InquirerPy import inquirer

from git_flow_cli.ui import UI
from git_flow_cli.core import GitRunner

ui = UI()
runner = GitRunner()

def push():
    ui.log('Starting the synchronization process with GitHub...')

    remote_check = runner.run(['remote', 'get-url', 'origin'])

    if 'error' in remote_check.lower() or not remote_check.strip():
        ui.warning('Repository in not found')

        repo_url = inquirer.text(
            message='Enter the URL of your GitHub repository:',
            default='https://github.com/'
        ).execute()

        if repo_url:
            ui.info('Linking the repository...')
            runner.run(['remote', 'add' ,'origin', repo_url])

    message = inquirer.text(
        message='Enter the commit text (message):',
        default='Auto-sync update'
    ).execute()

    ui.info('Step 1: Preparing files')
    add_result = runner.run(['add', '.'])
    if add_result:
        ui.log(add_result.strip())

    ui.info(f'Step 2: Creating a commit with a message "{message}"')
    commit_result = runner.run(['commit', '-m', message])
    if commit_result:
        ui.log(commit_result.strip())

    ui.info('Step 3: Pushing changes to the remote repository (git push)...')

    runner.run(['brahch', '-M', 'main'])
    push_result = runner.run(['push', '-u', 'origin', 'main', '--force'])

    if 'error' in push_result.lower() or 'fatal' in push_result.lower():
        ui.error('Error while sending to GitHub!')
        ui.print_panel(text=push_result.strip(), title='[bold red]Git Error[/bold red')

    else:
        ui.success('Code successfully sent to GitHub!')
        if push_result:
            ui.log(push_result.strip())