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
    Controls enterprise autonomy runtime lifecycle.
    """

    def __init__(
        self,
        monitor: AutonomyMonitor | None = None,
        metrics: AutonomyMetrics | None = None,
    ) -> None:

        self._monitor = monitor or AutonomyMonitor()
        self._metrics = metrics
        self._started = False

    @property
    def started(self) -> bool:
        return self._started

    def start(self) -> None:
        if self._started:
            return

        self._monitor.start()

        if self._metrics is not None:
            self._metrics.record_start()

        self._started = True

    def stop(self) -> None:
        if not self._started:
            return

        self._monitor.stop()

        if self._metrics is not None:
            self._metrics.record_stop()

        self._started = False

    def snapshot(self) -> AutonomySnapshot:
        return self._monitor.snapshot()
