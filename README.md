# YT-DL CLI (Arch Linux Style)

Aplikasi CLI minimalis dan interaktif untuk mendownload video atau audio dari YouTube. Dibangun dengan Python, **uv**, **Typer**, dan **Rich** untuk pengalaman terminal yang modern.

![Tampilan YT-DL CLI](assets/screenshot_2026-03-03_14-37-09.png)

## ✨ Fitur
- 🖥️ **Dashboard Interaktif**: Antarmuka terminal yang bersih dan berwarna.
- 📥 **Input Mudah**: Tidak perlu argumen panjang, cukup masukkan URL saat diminta.
- 🔄 **Pilihan Format**: Pilih antara **MP4 (Video)** atau **MP3 (Audio)** secara langsung.
- 📊 **Progress Bar Cantik**: Pantau kecepatan download dan estimasi waktu secara real-time.
- ⚡ **Ringan & Cepat**: Menggunakan `uv` untuk manajemen paket yang efisien.

## 🛠️ Prasyarat
Pastikan sistem kamu sudah terinstall **FFmpeg** (untuk penggabungan video & audio):

```bash
sudo pacman -S ffmpeg
