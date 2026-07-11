"""
PocketBot Enterprise X

Metrics Registry.
"""

from __future__ import annotations

from pocketbot.infrastructure.metrics.metric import (
    Metric,
)


class MetricsRegistry:
    """
    Stores and manages operational metrics.
    """

    def __init__(self) -> None:
        self._metrics: dict[str, Metric] = {}

    def increment(
        self,
        name: str,
        amount: int = 1,
    ) -> None:
        """
        Increments a metric counter.
        """

        current = self._metrics.get(
            name,
            Metric(
                name=name,
                value=0,
            ),
        )

        current.value += amount

        self._metrics[name] = current

    def get(
        self,
        name: str,
    ) -> Metric | None:
        """
        Returns a metric.
        """

        return self._metrics.get(
            name,
        )

    def all(self) -> list[Metric]:
        """
        Returns all metrics.
        """

        return list(
            self._metrics.values(),
        )
