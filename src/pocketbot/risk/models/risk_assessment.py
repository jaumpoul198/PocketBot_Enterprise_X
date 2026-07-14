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


@dataclass(frozen=True, slots=True)
class RiskAssessment:
    """
    Represents the result of a risk evaluation.
    """

    status: RiskStatus
    reason: str

    def __post_init__(self) -> None:
        if not isinstance(self.status, RiskStatus):
            raise TypeError("status must be a RiskStatus")

        if not isinstance(self.reason, str):
            raise TypeError("reason must be a string")

        if not self.reason.strip():
            raise ValueError("reason cannot be empty")

    @property
    def approved(self) -> bool:
        """
        Indicates whether the operation was approved.
        """

        return self.status is RiskStatus.APPROVED