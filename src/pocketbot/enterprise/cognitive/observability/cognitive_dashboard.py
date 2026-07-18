"""
PocketBot Enterprise X
Cognitive Dashboard

Provides a unified view of cognitive
observability data.
"""

from typing import Dict

from .cognitive_monitor import CognitiveMonitor


class CognitiveDashboard:
    """
    Read-only dashboard facade for
    cognitive observability.
    """

    def __init__(
        self,
        monitor: CognitiveMonitor,
    ):
        self.monitor = monitor

    def summary(self) -> Dict:
        """
        Return dashboard summary.
        """

        return self.monitor.snapshot()

    def metrics(self):
        """
        Return recorded metrics.
        """

        return self.monitor.metrics.get_all()

    def events(self):
        """
        Return recorded events.
        """

        return self.monitor.events.get_all()

    def traces(self):
        """
        Return execution traces.
        """

        return self.monitor.traces.get_all()
