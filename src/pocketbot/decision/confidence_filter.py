"""
PocketBot Enterprise X

Confidence decision filter.
"""

from __future__ import annotations

import math

from pocketbot.decision.filter import DecisionFilter
from pocketbot.decision.result import DecisionResult
from pocketbot.domain.enums import SignalType
from pocketbot.score.result import ScoreResult


class ConfidenceFilter(DecisionFilter):
    """
    Validates whether the confidence level is sufficient.
    """

    def __init__(
        self,
        minimum_confidence: float = 0.70,
    ) -> None:
        if isinstance(minimum_confidence, bool):
            raise TypeError(
                "minimum_confidence cannot be boolean"
            )

        if not isinstance(
            minimum_confidence,
            (int, float),
        ):
            raise TypeError(
                "minimum_confidence must be numeric"
            )

        value = float(minimum_confidence)

        if not math.isfinite(value):
            raise ValueError(
                "minimum_confidence must be finite"
            )

        if not 0 < value <= 1:
            raise ValueError(
                "minimum_confidence must be between 0 and 1"
            )

        self._minimum_confidence = value

    def evaluate(
        self,
        score: ScoreResult,
    ) -> DecisionResult | None:
        """
        Evaluates confidence threshold.
        """

        if score is None:
            raise TypeError(
                "score cannot be None"
            )

        if not isinstance(score, ScoreResult):
            raise TypeError(
                "score must be ScoreResult"
            )

        confidence = score.confidence

        if isinstance(confidence, bool):
            raise TypeError(
                "confidence cannot be boolean"
            )

        if not isinstance(
            confidence,
            (int, float),
        ):
            raise TypeError(
                "confidence must be numeric"
            )

        confidence_value = float(confidence)

        if not math.isfinite(confidence_value):
            raise ValueError(
                "confidence must be finite"
            )

        if confidence_value >= self._minimum_confidence:
            return DecisionResult(
                signal=SignalType.BUY,
                score=score.score,
                confidence=confidence_value,
                approved=True,
                reason="Confidence threshold reached.",
            )

        return DecisionResult(
            signal=SignalType.NEUTRAL,
            score=score.score,
            confidence=confidence_value,
            approved=False,
            reason="Confidence below minimum threshold.",
        )