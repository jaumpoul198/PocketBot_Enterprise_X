"""
PocketBot Enterprise X

Application Runtime.
"""

from __future__ import annotations

from pocketbot.application.lifecycle.lifecycle_manager import (
    LifecycleManager,
)
from pocketbot.application.services.application_service import (
    ApplicationService,
)
from pocketbot.infrastructure.container.interfaces import (
    IServiceProvider,
)


class ApplicationRuntime:
    """
    Controls application lifecycle.
    """

    def __init__(
        self,
        provider: IServiceProvider,
        lifecycle: LifecycleManager,
    ) -> None:
        self._provider = provider
        self._lifecycle = lifecycle
        self._running = False

    def start(self) -> None:
        """
        Initializes application runtime.
        """

        self._provider.get_service(
            ApplicationService,
        )

        self._lifecycle.start()

        self._running = True

    def run(self) -> None:
        """
        Runs the application.
        """

        self.start()

    def stop(self) -> None:
        """
        Stops application runtime.
        """

        self._lifecycle.stop()

        self._running = False

    @property
    def is_running(self) -> bool:
        """
        Returns runtime state.
        """

        return self._running