# Changelog

All notable changes to this project are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

- `uv` package management with `pyproject.toml` and lockfile
- Standard project docs: `CHANGELOG.md`, `CONTRIBUTING.md`, `LICENSE`, `SECURITY.md`

## [2.0.0] - 2026-07-20

### Added

- Interactive CLI for single videos and playlists
- Cross-platform save locations (Linux, macOS, Windows, Termux)
- Video and audio (MP3) download with quality selection
- Download summary and confirmation before starting

### Changed

- Replaced broken pytube-based flow with **yt-dlp**
- Refactored monolithic `panda.py` into `panda_downloader` package

### Removed

- Vendored pytube dependency and duplicate download helpers
- Legacy beta scripts (`panda_downlaoder_beta.py`, `test.py`, `spin.py`)

## [1.0.0] - 2021

### Added

- Original Panda Downloader CLI with ASCII art and pytube integration
- Playlist and single-video download modes
- Platform-specific default paths for Linux, Windows, and Termux

[Unreleased]: https://github.com/vishnudas-bluefox/panda-downloader/compare/v2.0.0...HEAD
[2.0.0]: https://github.com/vishnudas-bluefox/panda-downloader/compare/v1.0.0...v2.0.0
[1.0.0]: https://github.com/vishnudas-bluefox/panda-downloader/releases/tag/v1.0.0
