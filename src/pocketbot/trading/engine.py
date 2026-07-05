"""
PocketBot Enterprise X

Trade Engine.
"""

from __future__ import annotations

from pocketbot.decision.engine import DecisionEngine
from pocketbot.execution.engine import ExecutionEngine
from pocketbot.risk.engine import RiskEngine
from pocketbot.score.result import ScoreResult
from pocketbot.trading.result import TradeResult


class TradeEngine:
    """
    Executes the complete trading cycle.
    """

    def __init__(
        self,
        decision: DecisionEngine,
        risk: RiskEngine,
        execution: ExecutionEngine,
    ) -> None:

        self._decision = decision
        self._risk = risk
        self._execution = execution

    def process(
        self,
        asset: str,
        timeframe: int,
        score: ScoreResult,
    ) -> TradeResult:

        decision = self._decision.decide(score)

        risk = self._risk.evaluate(decision)

        execution = self._execution.execute(
            asset=asset,
            timeframe=timeframe,
            decision=decision,
            risk=risk,
        )

        return TradeResult(
            score=score,
            decision=decision,
            risk=risk,
            execution=execution,
        )