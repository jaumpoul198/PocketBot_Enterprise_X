from __future__ import annotations

from pocketbot.infrastructure.metrics import (
    MetricsRegistry,
)


class AutonomyMetrics:
    """
    Enterprise autonomy metrics adapter.

    Provides metrics related to autonomy lifecycle.
    """

    AUTONOMY_STARTED = "autonomy_started"
    AUTONOMY_STOPPED = "autonomy_stopped"
    AUTONOMY_FAILURES = "autonomy_failures"
    AUTONOMY_RECOVERIES = "autonomy_recoveries"

    def __init__(
        self,
        metrics: MetricsRegistry,
    ) -> None:
        self._metrics = metrics

    def record_start(self) -> None:
        self._metrics.increment(
            self.AUTONOMY_STARTED,
        )

    def record_stop(self) -> None:
        self._metrics.increment(
            self.AUTONOMY_STOPPED,
        )

    def record_failure(self) -> None:
        self._metrics.increment(
            self.AUTONOMY_FAILURES,
        )

    def record_recovery(self) -> None:
        self._metrics.increment(
            self.AUTONOMY_RECOVERIES,
        )

    def failures(self) -> int:
        metric = self._metrics.get(
            self.AUTONOMY_FAILURES,
        )

        if metric is None:
            return 0

        return metric.value
