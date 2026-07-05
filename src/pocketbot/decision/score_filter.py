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
        self._minimum_buy = minimum_buy
        self._maximum_sell = maximum_sell

    def evaluate(
        self,
        score: ScoreResult,
    ) -> DecisionResult | None:
        """
        Evaluates the score.
        """

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