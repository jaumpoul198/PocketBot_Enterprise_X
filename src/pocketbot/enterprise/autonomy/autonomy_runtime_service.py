from __future__ import annotations

from pocketbot.enterprise.autonomy.autonomy_metrics import (
    AutonomyMetrics,
)
from pocketbot.enterprise.autonomy.autonomy_monitor import (
    AutonomyMonitor,
    AutonomySnapshot,
)
from pocketbot.enterprise.autonomy.recovery import (
    AutonomyRecoveryEngine,
    RecoveryStatus,
)


class AutonomyRuntimeService:
    """
    Controls enterprise autonomy runtime lifecycle.
    """

    def __init__(
        self,
        monitor: AutonomyMonitor | None = None,
        metrics: AutonomyMetrics | None = None,
        recovery: AutonomyRecoveryEngine | None = None,
    ) -> None:

        self._monitor = monitor or AutonomyMonitor()
        self._metrics = metrics
        self._recovery = recovery or AutonomyRecoveryEngine()

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

    def detect_failure(
        self,
        reason: str,
    ) -> RecoveryStatus:
        """
        Register runtime failure.
        """

        status = self._recovery.detect_failure(reason)

        self._monitor.mark_failure()

        self._monitor.update_metric(
            "recovery_state",
            status.state.value,
        )

        return status

    def recover(self) -> bool:
        """
        Execute autonomous recovery.
        """

        self._monitor.mark_recovering()

        result = self._recovery.execute_recovery()

        status = self._recovery.get_status()

        self._monitor.update_metric(
            "recovery_state",
            status.state.value,
        )

        if result:
            self._monitor.mark_recovered()
        else:
            self._monitor.mark_failure()

        return result

    def recovery_status(self) -> RecoveryStatus:
        """
        Return recovery lifecycle state.
        """

        return self._recovery.get_status()

    def recovery_metrics(self) -> dict[str, object]:
        """
        Return recovery metrics.
        """

        return self._recovery.get_metrics()
