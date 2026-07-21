# Panda Downloader

Interactive YouTube video and playlist downloader for Linux, macOS, Windows, and Termux.

Created by [Vishnudas-bluefox](https://github.com/vishnudas-bluefox)

## Features

- Single video and playlist downloads
- Video or audio (MP3) with quality selection
- Interactive save location: default folder, current directory, or custom path
- Cross-platform defaults (Desktop, Downloads, Termux storage)

## Requirements

- [uv](https://docs.astral.sh/uv/getting-started/installation/) (recommended)
- [ffmpeg](https://ffmpeg.org/) (required for audio/MP3 conversion)

## Setup

```bash
git clone https://github.com/vishnudas-bluefox/panda-downloader.git
cd panda-downloader
uv sync
```

## Run

```bash
uv run panda
```

Other entry points:

```bash
uv run python panda.py
uv run python -m panda_downloader
```

The CLI walks you through URL, format, quality, and output path, then asks for confirmation before downloading.

## Project docs

| File | Purpose |
| ---- | ------- |
| [CHANGELOG.md](CHANGELOG.md) | Version history |
| [CONTRIBUTING.md](CONTRIBUTING.md) | Development and PR guidelines |
| [LICENSE](LICENSE) | MIT license |
| [SECURITY.md](SECURITY.md) | Vulnerability reporting |

## Notes

- Uses **yt-dlp** (pytube is no longer reliable against current YouTube).
- Default save path: `~/Desktop/panda-downloader` (macOS/Linux), Windows Desktop, or Termux Download folder.

## License

MIT — see [LICENSE](LICENSE).
