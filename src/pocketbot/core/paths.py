"""
PocketBot Enterprise X
Core - Paths

Gerenciamento centralizado de todos os caminhos do projeto.
"""

from __future__ import annotations

from pathlib import Path


class ProjectPaths:
    """
    Classe responsável por fornecer todos os caminhos do projeto.
    """

    ROOT = Path(__file__).resolve().parents[3]

    SRC = ROOT / "src"

    CONFIG = ROOT / "config"

    DOCS = ROOT / "docs"

    SCRIPTS = ROOT / "scripts"

    TESTS = ROOT / "tests"

    LOGS = ROOT / "logs"

    DATABASE = ROOT / "database"

    CACHE = ROOT / "cache"

    MODELS = ROOT / "models"

    TEMP = ROOT / "temp"

    @classmethod
    def create_directories(cls) -> None:
        """
        Cria automaticamente todas as pastas necessárias.
        """

        directories = (
            cls.LOGS,
            cls.DATABASE,
            cls.CACHE,
            cls.MODELS,
            cls.TEMP,
        )

        for directory in directories:
            directory.mkdir(parents=True, exist_ok=True)