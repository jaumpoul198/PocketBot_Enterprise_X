"""
PocketBot Enterprise X

Risk service interface.
"""

from __future__ import annotations

from abc import ABC, abstractmethod

from pocketbot.risk.models.risk_assessment import (
    RiskAssessment,
)


class RiskService(ABC):
    """
    Defines the contract for risk evaluation.
    """

    @abstractmethod
    def evaluate(
        self,
        *,
        position_size: float,
        current_exposure: float,
    ) -> RiskAssessment:
        """
        Evaluate whether a trading operation is allowed.

        Parameters:
            position_size:
                Size of the new position.

            current_exposure:
                Current portfolio exposure.

        Returns:
            RiskAssessment with approval or rejection.
        """
        raise NotImplementedError
