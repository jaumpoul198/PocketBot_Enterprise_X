"""
PocketBot Enterprise X
Cognitive Metrics Manager

Responsible for collecting and querying
cognitive performance metrics.
"""

from typing import Dict, List

from .observability_models import CognitiveMetric


class CognitiveMetrics:
    """
    Stores cognitive system metrics.
    """

    def __init__(self):
        self._metrics: List[CognitiveMetric] = []


    def record(
        self,
        name: str,
        value: float,
        component: str,
        metadata: Dict = None,
    ) -> CognitiveMetric:
        """
        Register a cognitive metric.
        """

        metric = CognitiveMetric(
            name=name,
            value=value,
            component=component,
            metadata=metadata or {},
        )

        self._metrics.append(metric)

        return metric


    def get_all(self) -> List[CognitiveMetric]:
        """
        Return all metrics.
        """

        return list(self._metrics)


    def get_by_component(
        self,
        component: str,
    ) -> List[CognitiveMetric]:
        """
        Filter metrics by component.
        """

        return [
            metric
            for metric in self._metrics
            if metric.component == component
        ]


    def latest(
        self,
        name: str,
    ) -> CognitiveMetric | None:
        """
        Return latest metric by name.
        """

        for metric in reversed(self._metrics):
            if metric.name == name:
                return metric

        return None


    def count(self) -> int:
        """
        Return total metrics stored.
        """

        return len(self._metrics)
