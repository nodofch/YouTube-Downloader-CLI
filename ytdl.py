import typer
import yt_dlp
import os
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn, DownloadColumn, TransferSpeedColumn, TimeRemainingColumn

# Dashboard Rich
console = Console()
app = typer.Typer()

def show_dashboard():
    dashboard_text = Text()
    dashboard_text.append("=== YT-DL CLI ===\n", style="bold sea_green1")
    dashboard_text.append("CLI Tools YouTube Video/Audio Downloader\n", style="italic grey50")
    dashboard_text.append("-" * 40, style="grey37")
    
    console.print(Panel(dashboard_text, expand=False, border_style="sea_green1"))

def download_progress_hook(d, progress, task_id):
    if d['status'] == 'downloading':
        p = d.get('_percent_str', '0%').replace('%','')
        try:
            p_float = float(p)
        except:
            p_float = 0
        progress.update(task_id, completed=p_float, total=100)
    elif d['status'] == 'finished':
        progress.update(task_id, completed=100, description="[bold green]Finish![/bold green]")

@app.command()
def main():
    # 1. Dashboard
    show_dashboard()

    # 2. Input URL
    url = typer.prompt("🌐 Enter the YouTube video URL")

    if not url:
        console.print("[bold red]Error:[/bold red] URLs cannot be empty!")
        raise typer.Exit()

    # 3. Select Format Menu
    console.print("\n[bold yellow]Select Download Format:[/bold yellow]")
    console.print("1. [bold cyan]MP4[/bold cyan] (Video)")
    console.print("2. [bold magenta]MP3[/bold magenta] (Audio)")
    
    pilihan = typer.prompt("\nEnter Options (1/2)", default="1")

    # 4. Configuration yt-dlp
    ydl_opts = {
        'outtmpl': '%(title)s.%(ext)s',
        'quiet': True,
        'no_warnings': True,
    }

    if pilihan == "2":
        console.print("[bold magenta]Choose: MP3 (Audio)[/bold magenta]")
        ydl_opts.update({
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        })
    else:
        console.print("[bold cyan]Choose: MP4 (Video)[/bold cyan]")
        ydl_opts['format'] = 'bestvideo+bestaudio/best'

    # 5. Download Process
    rich_progress = Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        BarColumn(bar_width=None),
        DownloadColumn(),
        TransferSpeedColumn(),
        TimeRemainingColumn(),
        console=console
    )

    console.print(f"\n[bold white]Starting Process...[/bold white]")
    
    with rich_progress:
        task_id = rich_progress.add_task("[cyan]Providing Data...", total=100)
        ydl_opts['progress_hooks'] = [lambda d: download_progress_hook(d, rich_progress, task_id)]

        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
        except Exception as e:
            console.print(f"\n[bold red]Error Occurs:[/bold red] {e}")

if __name__ == "__main__":
    app()
