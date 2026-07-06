"""
PocketBot Enterprise X

Execution Engine.
"""

from __future__ import annotations

from pocketbot.decision.result import DecisionResult
from pocketbot.execution.order import ExecutionOrder
from pocketbot.execution.result import ExecutionResult
from pocketbot.risk.result import RiskResult


class ExecutionEngine:
    """
    Responsible for transforming an approved decision
    into an executable order.
    """

    def execute(
        self,
        asset: str,
        timeframe: int,
        decision: DecisionResult,
        risk: RiskResult,
    ) -> ExecutionResult:

        if not decision.approved:
            return ExecutionResult(
                decision=decision,
                risk=risk,
                order=None,
                executed=False,
                message="Decision rejected.",
            )

        if not risk.approved:
            return ExecutionResult(
                decision=decision,
                risk=risk,
                order=None,
                executed=False,
                message="Risk rejected.",
            )

        order = ExecutionOrder(
            asset=asset,
            signal=decision.signal,
            timeframe=timeframe,
            amount=risk.position_size,
            confidence=decision.confidence,
            expiration=timeframe,
        )

        return ExecutionResult(
            decision=decision,
            risk=risk,
            order=order,
            executed=True,
            message="Execution approved.",
        )
