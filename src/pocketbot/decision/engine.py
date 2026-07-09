"""
PocketBot Enterprise X

Decision Engine.
"""

from __future__ import annotations

from pocketbot.decision.filters import DecisionFilters
from pocketbot.decision.result import DecisionResult
from pocketbot.domain.enums import SignalType
from pocketbot.market.strategy.models import (
    StrategyResult,
    StrategySignal,
)
from pocketbot.score.result import ScoreResult


class DecisionEngine:
    """
    Orchestrates the trading decision process.
    """

    def __init__(self) -> None:
        self._filters = DecisionFilters()

    def decide(
        self,
        score: ScoreResult,
        strategy: StrategyResult | None = None,
    ) -> DecisionResult:
        """
        Executes all decision filters.
        """

        if not self._filters.score_ok(score):
            return DecisionResult(
                signal=SignalType.NEUTRAL,
                score=score.score,
                confidence=score.confidence,
                approved=False,
                reason="Score below minimum threshold.",
            )

        if not self._filters.confidence_ok(score):
            return DecisionResult(
                signal=SignalType.NEUTRAL,
                score=score.score,
                confidence=score.confidence,
                approved=False,
                reason="Confidence below minimum threshold.",
            )

        if not self._filters.strength_ok(score):
            return DecisionResult(
                signal=SignalType.NEUTRAL,
                score=score.score,
                confidence=score.confidence,
                approved=False,
                reason="Strength below minimum threshold.",
            )

        if strategy is not None:
            if strategy.signal is StrategySignal.HOLD:
                return DecisionResult(
                    signal=SignalType.NEUTRAL,
                    score=score.score,
                    confidence=score.confidence,
                    approved=False,
                    reason=strategy.reason,
                    metadata={
                        "strategy_signal": strategy.signal.value,
                    },
                )

            if strategy.signal is StrategySignal.SELL:
                return DecisionResult(
                    signal=SignalType.NEUTRAL,
                    score=score.score,
                    confidence=score.confidence,
                    approved=False,
                    reason=strategy.reason,
                    metadata={
                        "strategy_signal": strategy.signal.value,
                    },
                )

        return DecisionResult(
            signal=SignalType.BUY,
            score=score.score,
            confidence=score.confidence,
            approved=True,
            reason="All decision filters approved.",
            metadata=(
                {}
                if strategy is None
                else {
                    "strategy_signal": strategy.signal.value,
                }
            ),
        )
