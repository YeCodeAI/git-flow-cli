from typing import List, Dict

from rich.console import Console
from rich.table import Table

console = Console()
error_console = Console(stderr=True)

class UI:
    def success(self, text: str) -> None:
        console.print(f'[green][+] {text}[/green]')
    
    def warning(self, text: str) -> None:
        console.print(f'[yellow][!] {text}[/yellow]')
    
    def error(self, text: str) -> None:
        error_console.print(f'[red][-] {text}[/red]')
    
    def info(self, text: str) -> None:
        console.print(f'[cyan][*] {text}[/cyan]')
    
    def log(self, text: str) -> None:
        console.log(text, _stack_offset=2)
    
    def rule(self, text: str) -> None:
        console.rule(text)

    def commit_table(self, commits: List[Dict[str, str]]) -> None:
        if not commits:
            self.warning('Commits are not found!')
            return
        
        table = Table(
            title='History commits',
            title_style='bold cyan',
            border_style='dim',
            header_style='bold magenta',
            show_lines=False,
            expand=True
        )

        table.add_column('Hash', style='yellow', no_wrap=True, width=10)
        table.add_column('Date', style='green', no_wrap=True, width=19)
        table.add_column('Author', style='cyan', no_wrap=True, max_width=24)
        table.add_column('Commit', style='white', overflow='fold')

        for commit in commits:
            table.add_row(
                commit.get('hash', ''),
                commit.get('date', ''),
                commit.get('author', ''),
                commit.get('subject', ''),
            )

        console.print(table)