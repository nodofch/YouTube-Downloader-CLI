# YT-DL CLI (Arch Linux Style)

A minimalist and interactive CLI application for downloading YouTube videos or audio. Built with Python, uv, Typer, and Rich for a modern terminal experience.

![Display YT-DL CLI](assets/screenshot_2026-03-03_17-46-06.png)

## ✨ Features
- 🖥️ **Interactive Dashboard**: Clean and colorful terminal user interface.
- 📥 **Simple Input**: No long arguments needed—just paste the URL when prompted.
- 🔄 **Format Options**: Choose between MP4 (Video) or MP3 (Audio) on the fly.
- 📊 **Beautiful Progress Bar**: Monitor download speed and ETA in real-time.
- ⚡ **Lightweight & Fast**: Powered by `uv` for efficient package management.

## 🛠️ Prerequisites
Ensure **FFmpeg** is installed on your system (required for merging video & audio streams):

```bash
# Arch Linux
sudo pacman -S ffmpeg

# Ubuntu / Debian
sudo apt install ffmpeg

# Fedora
sudo dnf install ffmpeg
```

## Instalation
Follow these steps to install the tool:
```bash
git clone https://github.com/nodofch/YouTube-Downloader-CLI.git
cd YouTube-Downloader-CLI
uv tool install . --force
uv tool update-shell
```

## Usage
Simply run the following command in your terminal::
```bash
ytdl
```
