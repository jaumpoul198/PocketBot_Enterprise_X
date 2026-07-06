"""
PocketBot Enterprise X

Score calculator.
"""

from __future__ import annotations

from collections.abc import Sequence

from pocketbot.indicators.base.result import IndicatorResult
from pocketbot.score.confidence import ConfidenceCalculator
from pocketbot.score.normalizer import WeightNormalizer
from pocketbot.score.result import ScoreResult


class ScoreCalculator:
    """
    Calculates the overall score of a group of indicators.

    This class is intentionally unaware of BUY, SELL or WAIT.
    Those decisions belong exclusively to the Decision Engine.
    """

    def __init__(self) -> None:
        self._normalizer = WeightNormalizer()
        self._confidence = ConfidenceCalculator()

    def calculate(
        self,
        results: Sequence[IndicatorResult],
    ) -> ScoreResult:
        """
        Calculate the final score.
        """

        if not results:
            return ScoreResult(
                score=0.0,
                confidence=0.0,
                strength=0.0,
                weight_sum=0.0,
                indicators=0,
                metadata={},
            )

        weights = self._normalizer.normalize(results)

        confidence = self._confidence.calculate(
            results,
            weights,
        )

        strength = sum(
            result.strength * weight
            for result, weight in zip(
                results,
                weights,
                strict=True,
            )
        )

        score = strength * confidence * 100.0

        return ScoreResult(
            score=score,
            confidence=confidence,
            strength=strength,
            weight_sum=sum(result.weight for result in results),
            indicators=len(results),
            metadata={
                "normalized_weights": weights,
            },
        )
