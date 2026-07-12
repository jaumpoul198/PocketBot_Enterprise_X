"""
PocketBot Enterprise X

Configuration Service.
"""

from __future__ import annotations

from copy import deepcopy
from pathlib import Path
from typing import Any

from pocketbot.config.loader import ConfigLoader


class ConfigService:
    """
    Central configuration access service.
    """

    def __init__(
        self,
        config_directory: Path,
    ) -> None:
        self._loader = ConfigLoader(
            config_directory,
        )

        self._cache: dict[str, dict[str, Any]] = {}

    def load(
        self,
        filename: str,
    ) -> dict[str, Any]:
        """
        Loads isolated configuration copy.
        """

        if filename not in self._cache:
            self._cache[filename] = self._loader.load(
                filename,
            )

        return deepcopy(
            self._cache[filename],
        )
