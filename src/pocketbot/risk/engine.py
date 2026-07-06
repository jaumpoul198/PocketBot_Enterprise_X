"""
PocketBot Enterprise X

Risk Engine.
"""

from __future__ import annotations

from pocketbot.decision.result import DecisionResult
from pocketbot.risk.result import RiskResult


class RiskEngine:
    """
    Evaluates whether a decision can be executed.
    """

    def evaluate(
        self,
        decision: DecisionResult,
    ) -> RiskResult:

        if not decision.approved:

            return RiskResult(
                approved=False,
                risk_level=1.0,
                position_size=0.0,
                max_loss=0.0,
                reason="Decision not approved.",
            )

        return RiskResult(
            approved=True,
            risk_level=0.20,
            position_size=1.0,
            max_loss=1.0,
            reason="Risk approved.",
        )
