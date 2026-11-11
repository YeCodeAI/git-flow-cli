from git_flow_cli.ui import UI
from git_flow_cli.core import GitRunner

ui = UI()
runner = GitRunner()

def status():
    ui.info('Проверяем состояние репозитория...')

    output = runner.run(['status'])

    ui.print_panel(text=output.strip(), title='[bold]Git Status[/bold]')