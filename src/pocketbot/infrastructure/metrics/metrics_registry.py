"""
PocketBot Enterprise X

Metrics Registry.
"""

from __future__ import annotations

from copy import deepcopy

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

        Internal state updates are isolated.
        """

        current = self._metrics.get(
            name,
            Metric(
                name=name,
                value=0,
            ),
         )

        updated = deepcopy(current)

        updated.value += amount

        self._metrics[name] = updated

    def get(
        self,
        name: str,
    ) -> Metric | None:
        """
        Returns an isolated metric copy.
        """

        metric = self._metrics.get(
            name,
        )

        if metric is None:
            return None

        return deepcopy(
            metric,
        )

    def all(self) -> list[Metric]:
        """
        Returns isolated metric copies.
        """

        return deepcopy(
            list(
                self._metrics.values(),
            ),
        )
