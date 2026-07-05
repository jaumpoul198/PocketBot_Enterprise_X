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
    Converts validated indicator results into a ScoreResult.
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

        total_weight = sum(
            result.weight
            for result in results
        )

        if total_weight <= 0:
            return ScoreResult(
                score=0.0,
                confidence=0.0,
                strength=0.0,
                weight_sum=0.0,
                indicators=len(results),
            )

        weighted_score = sum(
            result.score * result.weight
            for result in results
        )

        score = weighted_score / total_weight

        score = max(
            0.0,
            min(
                100.0,
                round(score, 2),
            ),
        )

        confidence = round(score / 100.0, 4)

        strength = round(
            weighted_score / (100.0 * total_weight),
            4,
        )

        return ScoreResult(
            score=score,
            confidence=confidence,
            strength=strength,
            weight_sum=total_weight,
            indicators=len(results),
        )