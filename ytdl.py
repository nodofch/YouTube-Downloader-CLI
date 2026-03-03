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
    dashboard_text.append("CLI Tools YouTube Downloader for my Arch Linux\n", style="italic grey50")
    dashboard_text.append("-" * 30, style="grey37")
    
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
        progress.update(task_id, completed=100, description="[bold green]Selesai![/bold green]")

@app.command()
def main():
    # 1. Paparkan Dashboard
    show_dashboard()

    # 2. Input URL
    url = typer.prompt("🌐 Masukkan URL video YouTube")

    if not url:
        console.print("[bold red]Ralat:[/bold red] URL tidak boleh kosong!")
        raise typer.Exit()

    # 3. Menu Pilihan Format
    console.print("\n[bold yellow]Pilih Format Muat Turun:[/bold yellow]")
    console.print("1. [bold cyan]MP4[/bold cyan] (Video)")
    console.print("2. [bold magenta]MP3[/bold magenta] (Audio)")
    
    pilihan = typer.prompt("\nMasukkan pilihan (1/2)", default="1")

    # 4. Konfigurasi yt-dlp berdasarkan pilihan
    ydl_opts = {
        'outtmpl': '%(title)s.%(ext)s',
        'quiet': True,
        'no_warnings': True,
    }

    if pilihan == "2":
        console.print("[bold magenta]Memilih: MP3 (Audio)[/bold magenta]")
        ydl_opts.update({
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        })
    else:
        console.print("[bold cyan]Memilih: MP4 (Video)[/bold cyan]")
        ydl_opts['format'] = 'bestvideo+bestaudio/best'

    # 5. Proses Download
    rich_progress = Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        BarColumn(bar_width=None),
        DownloadColumn(),
        TransferSpeedColumn(),
        TimeRemainingColumn(),
        console=console
    )

    console.print(f"\n[bold white]Memulai proses...[/bold white]")
    
    with rich_progress:
        task_id = rich_progress.add_task("[cyan]Menyediakan data...", total=100)
        ydl_opts['progress_hooks'] = [lambda d: download_progress_hook(d, rich_progress, task_id)]

        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
        except Exception as e:
            console.print(f"\n[bold red]Ralat terjadi:[/bold red] {e}")

if __name__ == "__main__":
    app()