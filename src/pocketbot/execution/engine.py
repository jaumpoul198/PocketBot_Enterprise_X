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

        if not isinstance(asset, str):
            raise TypeError("asset must be a string")

        if not asset.strip():
            raise ValueError("asset cannot be empty")

        if isinstance(timeframe, bool):
            raise TypeError("timeframe cannot be boolean")

        if not isinstance(timeframe, int):
            raise TypeError("timeframe must be int")

        if timeframe <= 0:
            raise ValueError("timeframe must be greater than zero")

        if decision is None:
            raise TypeError("decision cannot be None")

        if risk is None:
            raise TypeError("risk cannot be None")

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