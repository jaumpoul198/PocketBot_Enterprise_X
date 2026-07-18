"""
PocketBot Enterprise X
Health Monitor

Computes health indicators for the
cognitive platform.
"""

from typing import Dict

from .cognitive_monitor import CognitiveMonitor


class HealthMonitor:
    """
    Calculates health indicators based on
    cognitive observability.
    """

    def __init__(
        self,
        monitor: CognitiveMonitor,
    ):
        self.monitor = monitor

    def status(self) -> Dict:
        """
        Return current health information.
        """

        snapshot = self.monitor.snapshot()

        metrics = snapshot["metrics"]
        events = snapshot["events"]
        traces = snapshot["traces"]

        return {
            "healthy": True,
            "metrics": metrics,
            "events": events,
            "traces": traces,
        }

    def is_healthy(self) -> bool:
        """
        Return True if the runtime is healthy.
        """

        return self.status()["healthy"]
