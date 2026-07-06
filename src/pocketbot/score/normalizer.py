"""
PocketBot Enterprise X

Score weight normalizer.
"""

from __future__ import annotations

from collections.abc import Sequence

from pocketbot.indicators.base.result import IndicatorResult


class WeightNormalizer:
    """
    Normalize indicator weights so their sum equals 1.0.
    """

    def normalize(
        self,
        results: Sequence[IndicatorResult],
    ) -> list[float]:
        """
        Returns normalized weights.
        """

        if not results:
            return []

        total_weight = sum(result.weight for result in results)

        if total_weight <= 0:
            return [1.0 / len(results)] * len(results)

        return [result.weight / total_weight for result in results]
