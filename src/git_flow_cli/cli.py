import typer

from .commands import status, push

app = typer.Typer(
    help='Comfortable utilities for help in Git',
    add_completion=False
)

@app.command('status')
def status_command():
    """Check status repository"""
    status()

@app.command('push')
def push_command():
    """Push project in GitHub repository"""
    push()