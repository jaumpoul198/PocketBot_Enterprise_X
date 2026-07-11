"""
PocketBot Enterprise X

Default risk service implementation.
"""

from __future__ import annotations

from pocketbot.risk.interfaces.risk_service import (
    RiskService,
)
from pocketbot.risk.models.risk_assessment import (
    RiskAssessment,
    RiskStatus,
)
from pocketbot.risk.models.risk_profile import (
    RiskProfile,
)


class DefaultRiskService(RiskService):
    """
    Default implementation of risk validation.
    """

    def __init__(
        self,
        profile: RiskProfile | None = None,
    ) -> None:
        self._profile = profile or RiskProfile(
            max_position_size=1.0,
            max_loss_percentage=2.0,
            max_exposure_percentage=50.0,
        )

    def evaluate(
        self,
        *,
        position_size: float,
        current_exposure: float,
    ) -> RiskAssessment:
        """
        Evaluate trading risk constraints.
        """

        if position_size > self._profile.max_position_size:
            return RiskAssessment(
                status=RiskStatus.REJECTED,
                reason="Position size exceeds maximum limit.",
            )

        if current_exposure > (
            self._profile.max_exposure_percentage
            / 100
        ):
            return RiskAssessment(
                status=RiskStatus.REJECTED,
                reason="Exposure exceeds maximum limit.",
            )

        return RiskAssessment(
            status=RiskStatus.APPROVED,
            reason="Risk approved.",
        )
