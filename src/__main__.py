"""Global pipeline entry point.

Usage:
    uv run python -m src
    uv run python -m src --only s1_prepare
    uv run python -m src --s1_prepare.download.force_redownload true
"""

from src.cli import main

if __name__ == "__main__":
    main()
