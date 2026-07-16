from __future__ import annotations

from datetime import datetime, timezone

from .memory_store import IntelligenceMemoryStore
from .models import LearningRecord, LearningState


class LearningEngine:
    """
    Adaptive learning controller.
    """

    def __init__(
        self,
        memory: IntelligenceMemoryStore | None = None,
    ) -> None:
        self.memory = memory or IntelligenceMemoryStore()

    def learn(
        self,
        decision: str,
        score_before: float,
        score_after: float,
        feedback: float,
    ) -> LearningRecord:

        record = LearningRecord(
            decision=decision,
            score_before=score_before,
            score_after=score_after,
            feedback=feedback,
            timestamp=datetime.now(timezone.utc),
        )

        self.memory.add(record)

        return record

    def state(self) -> LearningState:

        total = self.memory.count()

        feedback = (
            self.memory.average_feedback()
        )

        adaptation = min(
            100.0,
            total * 5 + feedback * 10,
        )

        return LearningState(
            total_records=total,
            average_feedback=feedback,
            adaptation_level=adaptation,
            last_update=self.memory.last_update(),
        )
