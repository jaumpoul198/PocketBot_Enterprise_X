"""
PocketBot Enterprise X

Confluence scorer.
"""

from __future__ import annotations

from collections.abc import Sequence

from pocketbot.indicators.base.result import IndicatorResult


class ConfluenceScorer:
    """
    Calculates the overall confidence score.
    """

    def calculate(
        self,
        results: Sequence[IndicatorResult],
    ) -> float:

        if not results:
            return 0.0

        total_weight = sum(r.weight for r in results)

        if total_weight == 0:
            return 0.0

        return sum(r.confidence * r.weight for r in results) / total_weight
