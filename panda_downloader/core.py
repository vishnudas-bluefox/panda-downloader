"""Download helpers and path resolution."""

from __future__ import annotations

import os
import platform
import re
from pathlib import Path

import yt_dlp

TAG = "[Panda]"


def detect_os() -> str:
    system = platform.system().lower()
    if "TERMUX_VERSION" in os.environ or Path("/data/data/com.termux").exists():
        return "termux"
    if system == "windows":
        return "windows"
    if system == "darwin":
        return "macos"
    return "linux"


def default_base() -> Path:
    kind = detect_os()
    home = Path.home()
    if kind == "termux":
        return Path("/storage/emulated/0/Download/panda-downloader")
    if kind == "windows":
        return Path(os.environ.get("USERPROFILE", home)) / "Desktop" / "panda-downloader"
    # linux / macos
    desktop = home / "Desktop"
    return (desktop if desktop.exists() else home / "Downloads") / "panda-downloader"


def ask_path(subdir: str = "") -> Path:
    base = default_base() / subdir if subdir else default_base()
    print(f"\nDetected OS: {detect_os()}")
    print(f"Default path: {base}")
    print("1. Use default")
    print("2. Current directory")
    print("3. Custom path")
    choice = input("Choose location [1]: ").strip() or "1"

    if choice == "2":
        path = Path.cwd()
    elif choice == "3":
        raw = input("Enter path: ").strip()
        path = Path(raw).expanduser() if raw else base
    else:
        path = base

    path.mkdir(parents=True, exist_ok=True)
    return path


def is_playlist(url: str) -> bool:
    return "list=" in url or "/playlist" in url


def fetch_info(url: str) -> dict:
    class _Quiet:
        def debug(self, msg): pass
        def info(self, msg): pass
        def warning(self, msg): pass
        def error(self, msg): pass

    opts = {
        "quiet": True,
        "no_warnings": True,
        "noprogress": True,
        "extract_flat": "in_playlist",
        "logger": _Quiet(),
    }
    with yt_dlp.YoutubeDL(opts) as ydl:
        return ydl.extract_info(url, download=False)


def _progress(d: dict) -> None:
    if d["status"] == "downloading":
        pct = d.get("_percent_str", "").strip()
        spd = d.get("_speed_str", "").strip()
        print(f"\r  {pct}  {spd}   ", end="", flush=True)
    elif d["status"] == "finished":
        print("\r  Download finished, processing...          ")


def download(url: str, dest: Path, media: str, quality: str) -> None:
    """media: 'video' | 'audio'. quality: 'best' | '1080' | '720' | ... | '128' (audio kbps)."""
    if media == "audio":
        fmt = "bestaudio/best"
        post = [{"key": "FFmpegExtractAudio", "preferredcodec": "mp3",
                 "preferredquality": quality if quality.isdigit() else "192"}]
        outtmpl = str(dest / f"%(title)s{TAG}.%(ext)s")
    else:
        if quality == "best":
            fmt = "bestvideo+bestaudio/best"
        else:
            h = quality.rstrip("pP")
            fmt = f"bestvideo[height<={h}]+bestaudio/best[height<={h}]/best"
        post = []
        outtmpl = str(dest / f"%(title)s{TAG}.%(ext)s")

    if is_playlist(url):
        outtmpl = str(dest / "%(playlist_title)s" / f"%(playlist_index)03d-%(title)s{TAG}.%(ext)s")

    opts = {
        "format": fmt,
        "outtmpl": outtmpl,
        "progress_hooks": [_progress],
        "ignoreerrors": True,
        "retries": 3,
        "merge_output_format": "mp4",
        "postprocessors": post,
        "noplaylist": not is_playlist(url),
    }
    with yt_dlp.YoutubeDL(opts) as ydl:
        ydl.download([url])


def available_heights(info: dict) -> list[str]:
    heights = {
        f"{f['height']}p"
        for f in info.get("formats") or []
        if f.get("height")
    }
    return sorted(heights, key=lambda x: int(x[:-1]), reverse=True) or ["best"]


def safe_name(name: str) -> str:
    return re.sub(r'[<>:"/\\|?*]', "_", name).strip() or "download"
