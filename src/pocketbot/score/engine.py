"""
PocketBot Enterprise X

Score Engine
"""

from __future__ import annotations

from collections.abc import Sequence

from pocketbot.indicators.base.result import IndicatorResult
from pocketbot.score.result import ScoreResult


class ScoreEngine:
    """
    Converts indicator results into a ScoreResult.
    """

    def calculate(
        self,
        results: Sequence[IndicatorResult],
    ) -> ScoreResult:

        if not results:
            return ScoreResult(
                score=0.0,
                confidence=0.0,
                strength=0.0,
                weight_sum=0.0,
                indicators=0,
            )

        total_weight = sum(result.weight for result in results)

        if total_weight <= 0:
            return ScoreResult(
                score=0.0,
                confidence=0.0,
                strength=0.0,
                weight_sum=0.0,
                indicators=len(results),
            )

        weighted_confidence = sum(
            result.confidence * result.weight for result in results
        )

        weighted_strength = sum(result.strength * result.weight for result in results)

        confidence = weighted_confidence / total_weight

        strength = weighted_strength / total_weight

        score = round(confidence * 100.0, 2)

        return ScoreResult(
            score=score,
            confidence=round(confidence, 4),
            strength=round(strength, 4),
            weight_sum=total_weight,
            indicators=len(results),
        )
