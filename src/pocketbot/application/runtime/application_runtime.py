"""
PocketBot Enterprise X

Application Runtime.
"""

from __future__ import annotations

from pocketbot.application.lifecycle.lifecycle_manager import (
    LifecycleManager,
)
from pocketbot.application.orchestrator.trading_orchestrator import (
    TradingOrchestrator,
)
from pocketbot.application.runtime.state import (
    ApplicationState,
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
        self._state = ApplicationState.CREATED

    def start(self) -> None:
        """
        Initializes application runtime.
        """

        self._provider.get_service(
            TradingOrchestrator,
        )

        self._state = ApplicationState.STARTING

        self._lifecycle.start()

        self._state = ApplicationState.RUNNING

    def run(self) -> None:
        """
        Runs the application.
        """

        self.start()

    def stop(self) -> None:
        """
        Stops application runtime.
        """

        self._state = ApplicationState.STOPPING

        self._lifecycle.stop()

        self._state = ApplicationState.STOPPED

    @property
    def is_running(self) -> bool:
        """
        Returns whether the application is running.
        """

        return self._state == ApplicationState.RUNNING

    @property
    def state(self) -> ApplicationState:
        """
        Returns the current application state.
        """

        return self._state
