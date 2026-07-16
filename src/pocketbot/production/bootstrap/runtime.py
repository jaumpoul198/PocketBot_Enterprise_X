"""
PocketBot Enterprise X

Production Runtime.
"""

from __future__ import annotations

from pocketbot.application.lifecycle.lifecycle_manager import (
    LifecycleManager,
)
from pocketbot.enterprise.runtime.runtime_coordinator import (
    RuntimeCoordinator,
)
from pocketbot.production.config.settings import ProductionSettings


class ProductionRuntime:
    """
    Controls production application runtime lifecycle.
    """

    def __init__(
        self,
        settings: ProductionSettings,
        lifecycle: LifecycleManager | None = None,
        runtime: RuntimeCoordinator | None = None,
    ) -> None:
        self._settings = settings
        self._lifecycle = lifecycle
        self._runtime = runtime
        self._started = False

    @property
    def settings(self) -> ProductionSettings:
        return self._settings

    @property
    def started(self) -> bool:
        return self._started

    def start(self) -> bool:
        """
        Starts production runtime.
        """

        if self._lifecycle is not None:
            self._lifecycle.start()

        if self._runtime is not None:
            self._runtime.start()

        self._started = True

        return True

    def shutdown(self) -> bool:
        """
        Shuts down production runtime.
        """

        if self._runtime is not None:
            self._runtime.stop()

        if self._lifecycle is not None:
            self._lifecycle.stop()

        self._started = False

        return True
