from __future__ import annotations

from pocketbot.production.config.settings import ProductionSettings


class ProductionRuntime:
    def __init__(self, settings: ProductionSettings) -> None:
        self._settings = settings
        self._started = False

    @property
    def settings(self) -> ProductionSettings:
        return self._settings

    @property
    def started(self) -> bool:
        return self._started

    def start(self) -> bool:
        self._started = True
        return True

    def shutdown(self) -> bool:
        self._started = False
        return True
