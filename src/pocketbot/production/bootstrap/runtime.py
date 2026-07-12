from __future__ import annotations

from pocketbot.production.config.settings import ProductionSettings


class ProductionRuntime:
    def __init__(self, settings: ProductionSettings) -> None:
        self._settings = settings

    @property
    def settings(self) -> ProductionSettings:
        return self._settings

    def start(self) -> bool:
        return True

    def shutdown(self) -> bool:
        return True
