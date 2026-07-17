from __future__ import annotations

from dataclasses import dataclass, asdict
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

    def to_dict(self):
        data = asdict(self)
        data["timestamp"] = self.timestamp.isoformat()
        data["accuracy"] = self.accuracy
        return data

    @classmethod
    def from_mapping(cls, data=None):
        data = data or {}

        timestamp = data.get(
            "timestamp",
            datetime.utcnow(),
        )

        if isinstance(timestamp, str):
            timestamp = datetime.fromisoformat(timestamp)

        return cls(
            decision=data.get(
                "decision",
                "",
            ),
            expected_score=data.get(
                "expected_score",
                0.0,
            ),
            actual_score=data.get(
                "actual_score",
                0.0,
            ),
            success=data.get(
                "success",
                False,
            ),
            timestamp=timestamp,
        )
