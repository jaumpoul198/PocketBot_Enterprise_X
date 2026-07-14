"""
PocketBot Enterprise X

Score decision filter.
"""

from __future__ import annotations

from pocketbot.decision.filter import DecisionFilter
from pocketbot.decision.result import DecisionResult
from pocketbot.domain.enums import SignalType
from pocketbot.score.result import ScoreResult


class ScoreFilter(DecisionFilter):
    """
    Validates whether the score is sufficient.
    """

    def __init__(
        self,
        minimum_buy: float = 80.0,
        maximum_sell: float = 20.0,
    ) -> None:

        if isinstance(minimum_buy, bool):
            raise TypeError(
                "minimum_buy cannot be boolean"
            )

        if isinstance(maximum_sell, bool):
            raise TypeError(
                "maximum_sell cannot be boolean"
            )

        if not isinstance(
            minimum_buy,
            (int, float),
        ):
            raise TypeError(
                "minimum_buy must be numeric"
            )

        if not isinstance(
            maximum_sell,
            (int, float),
        ):
            raise TypeError(
                "maximum_sell must be numeric"
            )

        if minimum_buy <= 0:
            raise ValueError(
                "minimum_buy must be greater than zero"
            )

        if maximum_sell < 0:
            raise ValueError(
                "maximum_sell cannot be negative"
            )

        self._minimum_buy = float(minimum_buy)
        self._maximum_sell = float(maximum_sell)

    def evaluate(
        self,
        score: ScoreResult,
    ) -> DecisionResult | None:
        """
        Evaluates the score.
        """

        if score is None:
            raise TypeError(
                "score cannot be None"
            )

        if not isinstance(
            score,
            ScoreResult,
        ):
            raise TypeError(
                "score must be ScoreResult"
            )

        if score.score >= self._minimum_buy:
            return DecisionResult(
                signal=SignalType.BUY,
                score=score.score,
                confidence=score.confidence,
                approved=True,
                reason="BUY score threshold reached.",
            )

        if score.score <= self._maximum_sell:
            return DecisionResult(
                signal=SignalType.SELL,
                score=score.score,
                confidence=score.confidence,
                approved=True,
                reason="SELL score threshold reached.",
            )

        return None