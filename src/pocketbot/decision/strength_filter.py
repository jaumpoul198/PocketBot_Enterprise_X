"""
PocketBot Enterprise X

Strength decision filter.
"""

from __future__ import annotations

import math

from pocketbot.decision.filter import DecisionFilter
from pocketbot.decision.result import DecisionResult
from pocketbot.domain.enums import SignalType
from pocketbot.score.result import ScoreResult


class StrengthFilter(DecisionFilter):
    """
    Validates whether the strength level is sufficient.
    """

    def __init__(
        self,
        minimum_strength: float = 0.60,
    ) -> None:
        if isinstance(minimum_strength, bool):
            raise TypeError(
                "minimum_strength cannot be boolean"
            )

        if not isinstance(
            minimum_strength,
            (int, float),
        ):
            raise TypeError(
                "minimum_strength must be numeric"
            )

        value = float(minimum_strength)

        if not math.isfinite(value):
            raise ValueError(
                "minimum_strength must be finite"
            )

        if not 0 < value <= 1:
            raise ValueError(
                "minimum_strength must be between 0 and 1"
            )

        self._minimum_strength = value

    def evaluate(
        self,
        score: ScoreResult,
    ) -> DecisionResult | None:
        """
        Evaluates strength threshold.
        """

        if score is None:
            raise TypeError(
                "score cannot be None"
            )

        if not isinstance(score, ScoreResult):
            raise TypeError(
                "score must be ScoreResult"
            )

        strength = score.strength

        if isinstance(strength, bool):
            raise TypeError(
                "strength cannot be boolean"
            )

        if not isinstance(
            strength,
            (int, float),
        ):
            raise TypeError(
                "strength must be numeric"
            )

        strength_value = float(strength)

        if not math.isfinite(strength_value):
            raise ValueError(
                "strength must be finite"
            )

        if strength_value >= self._minimum_strength:
            return DecisionResult(
                signal=SignalType.BUY,
                score=score.score,
                confidence=score.confidence,
                approved=True,
                reason="Strength threshold reached.",
            )

        return DecisionResult(
            signal=SignalType.NEUTRAL,
            score=score.score,
            confidence=score.confidence,
            approved=False,
            reason="Strength below minimum threshold.",
        )