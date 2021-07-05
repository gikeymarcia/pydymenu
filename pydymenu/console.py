from rich.console import Console
from rich.theme import Theme

my_theme = Theme(
    {
        "good": "bold green",
        "bad": "underline red",
        "title": "bold blue",
    }
)

console = Console(theme=my_theme)
