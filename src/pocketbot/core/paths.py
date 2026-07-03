"""
PocketBot Enterprise X
Core - Project Paths
"""

from __future__ import annotations

from pathlib import Path


class ProjectPaths:
    """
    Centraliza todos os caminhos utilizados pelo projeto.
    """

    ROOT = Path(__file__).resolve().parents[3]

    SRC = ROOT / "src"
    CONFIG = ROOT / "config"
    DOCS = ROOT / "docs"
    SCRIPTS = ROOT / "scripts"
    TESTS = ROOT / "tests"

    LOGS = ROOT / "logs"
    CACHE = ROOT / "cache"
    DATA = ROOT / "data"

    @classmethod
    def create_directories(cls) -> None:
        """
        Cria automaticamente as pastas utilizadas pelo projeto.
        """

        directories = (
            cls.LOGS,
            cls.CACHE,
            cls.DATA,
        )

        for directory in directories:
            directory.mkdir(parents=True, exist_ok=True)
