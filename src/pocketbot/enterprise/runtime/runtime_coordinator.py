from __future__ import annotations

from pocketbot.enterprise.autonomy.autonomy_runtime_service import (
    AutonomyRuntimeService,
)

from pocketbot.enterprise.runtime.runtime_snapshot import (
    RuntimeSnapshot,
)


class RuntimeCoordinator:
    """
    Coordinates enterprise runtime lifecycle.
    """

    def __init__(
        self,
        autonomy: AutonomyRuntimeService,
    ) -> None:
        self._autonomy = autonomy
        self._running = False

    def start(self) -> None:
        """
        Starts enterprise runtime.
        """

        if self._running:
            return

        self._running = True

        self._autonomy.start()

    def stop(self) -> None:
        """
        Stops enterprise runtime.
        """

        if not self._running:
            return

        self._running = False

        self._autonomy.stop()

    def snapshot(self) -> RuntimeSnapshot:
        """
        Returns runtime snapshot.
        """

        return RuntimeSnapshot(
            running=self._running,
            autonomy_running=self._autonomy.running,
        )

    @property
    def running(self) -> bool:
        """
        Runtime state.
        """

        return self._running
