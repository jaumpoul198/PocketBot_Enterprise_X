"""
PocketBot Enterprise X
Core - Settings
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class Settings:
    """
    Configurações globais da aplicação.
    """

    debug: bool = False
    environment: str = "development"

    app_name: str = "PocketBot Enterprise X"

    version: str = "0.1.0"

    timezone: str = "America/Sao_Paulo"

    log_level: str = "INFO"

    database_url: str = "sqlite:///pocketbot.db"

    cache_enabled: bool = True

    learning_enabled: bool = True
