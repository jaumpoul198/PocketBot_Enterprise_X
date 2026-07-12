"""
PocketBot Enterprise X

Application Runtime.
"""

from __future__ import annotations

from pocketbot.events.publisher import EventPublisher

from pocketbot.application.lifecycle.lifecycle_manager import (
    LifecycleManager,
)
from pocketbot.application.pipeline.models import (
    TradingRequest,
    TradingResult,
)
from pocketbot.application.runtime.state import (
    ApplicationState,
)
from pocketbot.application.session.trading_session_manager import (
    TradingSessionManager,
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
        session_manager: TradingSessionManager,
        publisher: EventPublisher,
    ) -> None:
        self._provider = provider
        self._lifecycle = lifecycle
        self._session_manager = session_manager
        self._state = ApplicationState.CREATED
        self._publisher = publisher

    def start(self) -> None:
        """
        Initializes application runtime.
        """

        self._state = ApplicationState.STARTING

        try:
            self._lifecycle.start()

            self._state = ApplicationState.RUNNING

            self._publisher.publish(
                "application.started",
                {},
            )

        except Exception as exc:
            self._state = ApplicationState.FAILED

            self._publisher.publish(
                "application.startup.failed",
                {
                    "error": str(exc),
                },
            )

            raise

    def run(
        self,
        request: TradingRequest,
    ) -> TradingResult:
        """
        Executes application trading session.
        """

        if not self.is_running:
            self.start()

        session = self._session_manager.create_session(
            request,
        )

        return self._session_manager.execute(
            session,
        )

    def stop(self) -> None:
        """
        Stops application runtime.
        """

        self._state = ApplicationState.STOPPING

        self._publisher.publish(
            "application.shutdown.requested",
            {},
        )

        try:
            self._lifecycle.stop()

        except Exception as exc:
            self._state = ApplicationState.FAILED

            self._publisher.publish(
                "application.shutdown.failed",
                {
                    "error": str(exc),
                },
            )

            raise

        else:
            self._state = ApplicationState.STOPPED

        self._publisher.publish(
            "application.shutdown.completed",
            {},
        )

        self._publisher.publish(
            "application.stopped",
            {},
        )

    @property
    def is_running(self) -> bool:
        """
        Returns whether the application is running.
        """

        return self._state == ApplicationState.RUNNING

    @property
    def state(self) -> ApplicationState:
        """
        Returns current application state.
        """

        return self._state
