# Contributing

Thanks for your interest in improving Panda Downloader.

## Development setup

This project uses [uv](https://docs.astral.sh/uv/) for dependency management.

```bash
git clone https://github.com/vishnudas-bluefox/panda-downloader.git
cd panda-downloader
uv sync
```

Run the CLI:

```bash
uv run panda
# or
uv run python panda.py
```

## Making changes

1. Create a branch from `main` (or your team's default branch).
2. Keep changes focused and minimal.
3. Update `CHANGELOG.md` under **Unreleased** for user-visible changes.
4. Test manually with a short YouTube URL before opening a PR.

## Pull requests

- Describe what changed and why.
- Link related issues when applicable.
- Ensure the CLI still starts with `uv run panda`.

## Reporting issues

Include:

- OS and Python version (`uv run python --version`)
- Full command or steps to reproduce
- Error output (redact personal paths if needed)

See [SECURITY.md](SECURITY.md) for reporting security issues.
