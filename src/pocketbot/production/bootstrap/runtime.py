"""
PocketBot Enterprise X

Production Runtime.
"""

from __future__ import annotations

from pocketbot.application.lifecycle.lifecycle_manager import (
    LifecycleManager,
)
from pocketbot.enterprise.runtime.runtime_supervisor import (
    RuntimeSupervisor,
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
        supervisor: RuntimeSupervisor | None = None,
    ) -> None:

        self._settings = settings
        self._lifecycle = lifecycle
        self._supervisor = supervisor

        self._running = False

    @property
    def settings(self) -> ProductionSettings:
        return self._settings

    @property
    def started(self) -> bool:
        return self._running

    def start(self) -> bool:
        """
        Starts production runtime.
        """

        if self._lifecycle is not None:
            self._lifecycle.start()

        self._running = True

        if self._supervisor is not None:
            return self._supervisor.check(
                runtime_running=True,
                autonomy_running=True,
            )

        return True

    def shutdown(self) -> bool:
        """
        Stops production runtime.
        """

        if self._lifecycle is not None:
            self._lifecycle.stop()

        self._running = False

        return True
