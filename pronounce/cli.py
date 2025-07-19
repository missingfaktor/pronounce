import threading
import time
from contextlib import contextmanager
from typing import Any, Generator

import click
from rich.console import Console
from rich.live import Live
from rich.table import Table
from rich.text import Text

from .cube import fetch_cube_pronunciations


@contextmanager
def loading(word: str, console: Console, refresh_per_second: int = 24) -> Generator[None, Any, None]:
    start = time.perf_counter()
    stop_signal = threading.Event()
    live_text = Text()

    def updater(live):
        while not stop_signal.is_set():
            elapsed = time.perf_counter() - start
            new_text = Text.from_markup(
                f"[cyan]⠋ Looking up [bold]{word}[/] • [yellow]{elapsed:.1f}s[/]"
            )
            live.update(new_text)
            time.sleep(1 / refresh_per_second)

    with Live(live_text, console=console, refresh_per_second=refresh_per_second, transient=False) as live:
        thread = threading.Thread(target=updater, args=(live,), daemon=True)
        thread.start()
        try:
            yield
        finally:
            stop_signal.set()
            thread.join()
            elapsed = time.perf_counter() - start
            final_text = Text.from_markup(
                f"[green]✅ Looked up [bold]{word}[/] in [yellow]{elapsed:.1f}s[/]"
            )
            live.update(final_text)


def render_table(entries) -> None:
    table = Table(title="CUBE Pronunciations", show_lines=True)
    table.add_column("#", style="dim", justify="right")
    table.add_column("Word", style="bold cyan")
    table.add_column("Pronunciation", style="green")

    for i, (word, ipa) in enumerate(entries, start=1):
        table.add_row(str(i), word, ipa)

    console = Console()
    console.print(table)


@click.command()
@click.argument("word")
def run(word: str) -> None:
    console = Console()

    with loading(word, console):
        results = fetch_cube_pronunciations(word)

    if results:
        render_table(results)
    else:
        console.print(f"[yellow]No CUBE-style transcription found for:[/] {word}")
