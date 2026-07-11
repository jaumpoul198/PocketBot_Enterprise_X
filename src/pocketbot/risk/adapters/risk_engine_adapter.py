"""
PocketBot Enterprise X

Risk service adapter.
"""

from __future__ import annotations

from pocketbot.decision.result import DecisionResult
from pocketbot.risk.interfaces.risk_service import RiskService
from pocketbot.risk.result import RiskResult
from pocketbot.risk.models.risk_assessment import (
    RiskStatus,
)


class RiskEngineAdapter:
    """
    Adapts RiskService to the legacy RiskEngine contract.
    """

    def __init__(
        self,
        risk_service: RiskService,
    ) -> None:

        self._risk_service = risk_service

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

        assessment = self._risk_service.evaluate(
            position_size=1.0,
            current_exposure=0.0,
        )

        approved = (
            assessment.status
            is RiskStatus.APPROVED
        )

        return RiskResult(
            approved=approved,
            risk_level=0.20 if approved else 1.0,
            position_size=1.0 if approved else 0.0,
            max_loss=1.0 if approved else 0.0,
            reason=assessment.reason,
        )
