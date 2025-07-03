"""Console script for yolo_mf."""
import yolo_mf

import typer
from rich.console import Console

app = typer.Typer()
console = Console()


@app.command()
def main():
    """Console script for yolo_mf."""
    console.print("Replace this message by putting your code into "
               "yolo_mf.cli.main")
    console.print("See Typer documentation at https://typer.tiangolo.com/")
    


if __name__ == "__main__":
    app()
