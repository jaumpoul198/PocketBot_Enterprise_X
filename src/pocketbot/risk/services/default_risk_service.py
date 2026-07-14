"""
PocketBot Enterprise X

Default risk service implementation.
"""

from __future__ import annotations

import math

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

        self._validate_numeric(
            "position_size",
            position_size,
        )

        self._validate_numeric(
            "current_exposure",
            current_exposure,
        )

        if position_size <= 0:
            raise ValueError(
                "position_size must be greater than zero"
            )

        if current_exposure < 0:
            raise ValueError(
                "current_exposure cannot be negative"
            )

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

    @staticmethod
    def _validate_numeric(
        name: str,
        value: float,
    ) -> None:

        if isinstance(value, bool):
            raise TypeError(
                f"{name} cannot be boolean"
            )

        if not isinstance(value, (int, float)):
            raise TypeError(
                f"{name} must be numeric"
            )

        if not math.isfinite(float(value)):
            raise ValueError(
                f"{name} must be finite"
            )