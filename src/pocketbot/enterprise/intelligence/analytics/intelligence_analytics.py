"""Enterprise Intelligence Analytics."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Mapping


@dataclass(frozen=True, slots=True)
class IntelligenceAnalyticsSnapshot:
    """Immutable analytics snapshot."""

    total_events: int
    total_contexts: int
    total_memories: int
    average_score: float

    def to_dict(self) -> dict[str, Any]:
        return {
            "total_events": self.total_events,
            "total_contexts": self.total_contexts,
            "total_memories": self.total_memories,
            "average_score": self.average_score,
        }


class IntelligenceAnalytics:
    """Aggregates enterprise intelligence metrics."""

    def build_snapshot(
        self,
        *,
        total_events: int = 0,
        total_contexts: int = 0,
        total_memories: int = 0,
        average_score: float = 0.0,
    ) -> IntelligenceAnalyticsSnapshot:
        return IntelligenceAnalyticsSnapshot(
            total_events=total_events,
            total_contexts=total_contexts,
            total_memories=total_memories,
            average_score=average_score,
        )

    def from_mapping(
        self,
        data: Mapping[str, Any],
    ) -> IntelligenceAnalyticsSnapshot:
        return self.build_snapshot(
            total_events=int(data.get("total_events", 0)),
            total_contexts=int(data.get("total_contexts", 0)),
            total_memories=int(data.get("total_memories", 0)),
            average_score=float(data.get("average_score", 0.0)),
        )
