from rich.console import Console
from rich.panel import Panel

console = Console()

class UI:
    def success(self, text: str) -> None:
        console.print(f'[green][+] {text}[/green]')

    def warning(self, text: str) -> None:
        console.print(f'[yellow][!] {text}[/yellow]')
    
    def error(self, text: str) -> None:
        console.print(f'[red][-] {text}[/red]')

    def info(self, text: str) -> None:
        console.print(f'[cyan][*] {text}[/cyan]')

    def log(self, text: str) -> None:
        console.log(text)
    
    def print_panel(self, text: str, title: str) -> None:
        panel = Panel(
            text,
            title=title,
            title_align='center',
            expand=False
        )

        console.print(panel)
