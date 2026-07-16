from __future__ import annotations

from datetime import datetime, timezone

from .models import LearningRecord


class IntelligenceMemoryStore:
    """
    Stores intelligence learning experiences.
    """

    def __init__(self) -> None:
        self._records: list[LearningRecord] = []

    def add(
        self,
        record: LearningRecord,
    ) -> None:
        self._records.append(record)

    def all(
        self,
    ) -> list[LearningRecord]:
        return list(self._records)

    def count(self) -> int:
        return len(self._records)

    def average_feedback(self) -> float:
        if not self._records:
            return 0.0

        return sum(
            item.feedback
            for item in self._records
        ) / len(self._records)

    def last_update(self) -> datetime:
        if not self._records:
            return datetime.now(timezone.utc)

        return self._records[-1].timestamp
