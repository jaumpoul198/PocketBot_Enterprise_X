from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime


@dataclass
class DecisionFeedback:
    """
    Result feedback from an intelligence decision.
    """

    decision: str
    expected_score: float
    actual_score: float
    success: bool
    timestamp: datetime

    @property
    def accuracy(self) -> float:
        difference = abs(
            self.expected_score - self.actual_score
        )

        return max(
            0.0,
            1.0 - difference / 100,
        )
