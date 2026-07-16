from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone


@dataclass
class LearningRecord:
    """
    Represents an intelligence learning event.
    """

    decision: str
    score_before: float
    score_after: float
    feedback: float
    timestamp: datetime

    @property
    def improvement(self) -> float:
        return self.score_after - self.score_before


@dataclass
class LearningState:
    """
    Current adaptive learning state.
    """

    total_records: int
    average_feedback: float
    adaptation_level: float
    last_update: datetime

    @classmethod
    def empty(cls) -> "LearningState":
        return cls(
            total_records=0,
            average_feedback=0.0,
            adaptation_level=0.0,
            last_update=datetime.now(timezone.utc),
        )
