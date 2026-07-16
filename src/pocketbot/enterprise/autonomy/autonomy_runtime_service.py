from __future__ import annotations

from pocketbot.enterprise.autonomy.autonomy_metrics import (
    AutonomyMetrics,
)

from pocketbot.enterprise.autonomy.autonomy_monitor import (
    AutonomyMonitor,
    AutonomySnapshot,
)


class AutonomyRuntimeService:
    """
    Enterprise autonomy runtime service.
    """

    def __init__(
        self,
        monitor: AutonomyMonitor,
        metrics: AutonomyMetrics | None = None,
    ) -> None:
        self._monitor = monitor
        self._metrics = metrics
        self._running = False

    def start(self) -> None:
        """
        Starts autonomy runtime.
        """

        if self._running:
            return

        self._running = True

        self._monitor.activate()

        if self._metrics is not None:
            self._metrics.record_start()

    def stop(self) -> None:
        """
        Stops autonomy runtime.
        """

        if not self._running:
            return

        self._running = False

        self._monitor.deactivate()

        if self._metrics is not None:
            self._metrics.record_stop()

    def snapshot(self) -> AutonomySnapshot:
        """
        Returns autonomy snapshot.
        """

        return self._monitor.snapshot()

    @property
    def started(self) -> bool:
        """
        Returns runtime started state.
        """

        return self._running

    @property
    def running(self) -> bool:
        """
        Returns runtime state.
        """

        return self._running
