import typer
from rich.console import Console

# Create the main Typer application
app = typer.Typer(
    name="TodoApp",
    help="A simple command-line todo application.",
    add_completion=False,
)

# Create a rich console for styled output
console = Console()
