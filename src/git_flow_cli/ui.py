from rich.console import Console

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