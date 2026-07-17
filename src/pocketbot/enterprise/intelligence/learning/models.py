from __future__ import annotations

from dataclasses import dataclass, asdict
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

    def to_dict(self):
        data = asdict(self)
        data["timestamp"] = self.timestamp.isoformat()
        data["improvement"] = self.improvement
        return data

    @classmethod
    def from_mapping(cls, data=None):
        data = data or {}

        timestamp = data.get(
            "timestamp",
            datetime.now(timezone.utc),
        )

        if isinstance(timestamp, str):
            timestamp = datetime.fromisoformat(timestamp)

        return cls(
            decision=data.get("decision", ""),
            score_before=data.get("score_before", 0.0),
            score_after=data.get("score_after", 0.0),
            feedback=data.get("feedback", 0.0),
            timestamp=timestamp,
        )


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

    def to_dict(self):
        data = asdict(self)
        data["last_update"] = self.last_update.isoformat()
        return data

    @classmethod
    def from_mapping(cls, data=None):
        data = data or {}

        last_update = data.get(
            "last_update",
            datetime.now(timezone.utc),
        )

        if isinstance(last_update, str):
            last_update = datetime.fromisoformat(last_update)

        return cls(
            total_records=data.get("total_records", 0),
            average_feedback=data.get("average_feedback", 0.0),
            adaptation_level=data.get("adaptation_level", 0.0),
            last_update=last_update,
        )
