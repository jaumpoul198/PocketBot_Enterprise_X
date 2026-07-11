"""
PocketBot Enterprise X

Risk assessment models.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum


class RiskStatus(str, Enum):
    """
    Risk evaluation result.
    """

    APPROVED = "approved"
    REJECTED = "rejected"


@dataclass(frozen=True)
class RiskAssessment:
    """
    Represents the result of a risk evaluation.
    """

    status: RiskStatus
    reason: str

    @property
    def approved(self) -> bool:
        """
        Indicates whether the operation was approved.
        """

        return self.status is RiskStatus.APPROVED
