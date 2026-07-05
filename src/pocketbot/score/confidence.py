"""
PocketBot Enterprise X

Confidence calculator.
"""

from __future__ import annotations

from collections.abc import Sequence

from pocketbot.indicators.base.result import IndicatorResult


class ConfidenceCalculator:
    """
    Calculates the overall confidence of a group of indicators.

    The confidence is the weighted average of all indicator
    confidences using their normalized weights.
    """

    def calculate(
        self,
        results: Sequence[IndicatorResult],
        weights: Sequence[float],
    ) -> float:
        """
        Calculate confidence.

        Parameters
        ----------
        results
            Indicator results.

        weights
            Normalized weights.

        Returns
        -------
        float
            Confidence between 0.0 and 1.0.
        """

        if not results:
            return 0.0

        if len(results) != len(weights):
            raise ValueError(
                "results and weights must have the same size."
            )

        confidence = sum(
            result.confidence * weight
            for result, weight in zip(
                results,
                weights,
                strict=True,
            )
        )

        return max(0.0, min(1.0, confidence))