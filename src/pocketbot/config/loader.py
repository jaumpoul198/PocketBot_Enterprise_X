"""
PocketBot Enterprise X
Configuration Loader
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml


class ConfigLoader:
    """
    Responsável por carregar arquivos YAML.
    """

    def __init__(self, config_directory: Path) -> None:
        self._config_directory = config_directory

    def load(self, filename: str) -> dict[str, Any]:
        """
        Carrega um arquivo YAML da pasta de configuração.
        """

        file_path = self._config_directory / filename

        if not file_path.exists():
            raise FileNotFoundError(
                f"Arquivo de configuração não encontrado: {file_path}"
            )

        with file_path.open(
            mode="r",
            encoding="utf-8",
        ) as file:
            data = yaml.safe_load(file) or {}

        return data
