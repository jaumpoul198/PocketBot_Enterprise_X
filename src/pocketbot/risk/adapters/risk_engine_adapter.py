"""
PocketBot Enterprise X

Risk service adapter.
"""

from __future__ import annotations

from pocketbot.decision.result import DecisionResult
from pocketbot.risk.interfaces.risk_service import RiskService
from pocketbot.risk.models.risk_assessment import RiskStatus
from pocketbot.risk.result import RiskResult


class RiskEngineAdapter:
    """
    Adapts RiskService to the legacy RiskEngine contract.
    """

    def __init__(
        self,
        risk_service: RiskService,
    ) -> None:

        if risk_service is None:
            raise TypeError(
                "risk_service cannot be None"
            )

        self._risk_service = risk_service

    def evaluate(
        self,
        decision: DecisionResult,
    ) -> RiskResult:

        if decision is None:
            raise TypeError(
                "decision cannot be None"
            )

        if not isinstance(
            decision,
            DecisionResult,
        ):
            raise TypeError(
                "decision must be DecisionResult"
            )

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