"""
PocketBot Enterprise X

Confluence Scorer.
"""

from __future__ import annotations

from collections.abc import Sequence

from pocketbot.indicators.base.result import IndicatorResult


class ConfluenceScorer:
    """
    Calculates the weighted confidence score.
    """

    def calculate(
        self,
        results: Sequence[IndicatorResult],
    ) -> float:

        total_weight = sum(result.weight for result in results)

        if total_weight == 0:
            return 0.0

        weighted_score = sum(result.confidence * result.weight for result in results)

        return weighted_score / total_weight
