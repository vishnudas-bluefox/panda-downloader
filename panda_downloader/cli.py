"""Interactive CLI for Panda Downloader."""

from __future__ import annotations

import sys

from . import __version__
from .core import (
    ask_path,
    available_heights,
    download,
    fetch_info,
    is_playlist,
)

C = {
    "c": "\033[36m",
    "g": "\033[32m",
    "r": "\033[31m",
    "y": "\033[33m",
    "b": "\033[1m",
    "x": "\033[0m",
}


def c(key: str, text: str) -> str:
    return f"{C[key]}{text}{C['x']}"


def banner() -> None:
    print(c("c", f"""
╔══════════════════════════════════════╗
║         Panda Downloader  v{__version__}     ║
║     YouTube video & playlist CLI     ║
╚══════════════════════════════════════╝
"""))


def ask(prompt: str, valid: set[str] | None = None, default: str = "") -> str:
    while True:
        tip = f" [{default}]" if default else ""
        val = (input(c("c", f"{prompt}{tip}: ")).strip() or default)
        if valid is None:
            return val
        match = next((v for v in valid if v.lower() == val.lower()), None)
        if match is not None:
            return match.lower() if match.lower() in {"y", "n"} else match
        print(c("r", f"Invalid. Options: {', '.join(sorted(valid))}"))


def pick_quality(info: dict, media: str) -> str:
    if media == "audio":
        print(c("g", "\nAudio quality (kbps):"))
        options = ["320", "192", "128", "64"]
        for i, q in enumerate(options, 1):
            print(f"  {i}. {q} kbps")
        choice = ask("Select", {str(i) for i in range(1, 5)}, "2")
        return options[int(choice) - 1]

    heights = available_heights(info)
    # playlist flat extract may lack formats — offer common presets
    if heights == ["best"] and not info.get("formats"):
        heights = ["best", "1080p", "720p", "480p", "360p"]
    else:
        heights = ["best"] + [h for h in heights if h != "best"]

    print(c("g", "\nVideo quality:"))
    for i, q in enumerate(heights, 1):
        print(f"  {i}. {q}")
    choice = ask("Select", {str(i) for i in range(1, len(heights) + 1)}, "1")
    q = heights[int(choice) - 1]
    return "best" if q == "best" else q.rstrip("pP")


def run_once() -> None:
    url = ask("YouTube URL")
    if "youtube.com" not in url and "youtu.be" not in url:
        print(c("r", "That does not look like a YouTube URL."))
        return

    print(c("y", "\nFetching info..."))
    try:
        info = fetch_info(url)
    except Exception as exc:
        print(c("r", f"Failed to fetch info: {exc}"))
        return

    playlist = is_playlist(url)
    title = info.get("title") or "Unknown"
    if playlist:
        count = len(info.get("entries") or [])
        print(c("g", f"Playlist: {title}  ({count} videos)"))
    else:
        print(c("g", f"Video: {title}"))

    media = "video" if ask("1. Video  2. Audio", {"1", "2"}, "1") == "1" else "audio"
    quality = pick_quality(info, media)
    dest = ask_path("Videos" if media == "video" else "Audio")

    print(c("b", "\n── Summary ──"))
    print(f"  Title   : {title}")
    print(f"  Type    : {'Playlist' if playlist else 'Video'} / {media}")
    print(f"  Quality : {quality}{'p' if media == 'video' and quality != 'best' else ''}")
    print(f"  Save to : {dest}")

    if ask("Start download? (y/n)", {"y", "n", "Y", "N"}, "y").lower() != "y":
        print(c("y", "Cancelled."))
        return

    print(c("c", "\nDownloading..."))
    try:
        download(url, dest, media, quality)
        print(c("g", f"\nDone! Files saved in:\n  {dest}"))
    except Exception as exc:
        print(c("r", f"\nDownload failed: {exc}"))


def main() -> None:
    banner()
    try:
        while True:
            run_once()
            if ask("\nDownload more? (y/n)", {"y", "n", "Y", "N"}, "n").lower() != "y":
                print(c("c", "\nPanda is going to sleep. Bye!\n"))
                break
            print()
    except KeyboardInterrupt:
        print(c("y", "\n\nInterrupted. Bye!\n"))
        sys.exit(0)


if __name__ == "__main__":
    main()
