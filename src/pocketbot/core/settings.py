"""
PocketBot Enterprise X
Core - Settings
"""

from __future__ import annotations

import os
from dataclasses import dataclass


@dataclass(slots=True)
class Settings:
    """
    Configurações básicas da aplicação.
    """

    app_name: str = "PocketBot Enterprise X"
    environment: str = os.getenv("APP_ENV", "development")
    log_level: str = os.getenv("LOG_LEVEL", "INFO")
    database_url: str = os.getenv(
        "DATABASE_URL",
        "sqlite:///database/pocketbot.db",
    )


settings = Settings()