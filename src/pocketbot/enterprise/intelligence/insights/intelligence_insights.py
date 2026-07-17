"""Enterprise Intelligence Insights."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Mapping


@dataclass(frozen=True, slots=True)
class IntelligenceInsight:
    """Immutable enterprise intelligence insight."""

    category: str
    summary: str
    confidence: float
    metadata: dict[str, Any]

    def to_dict(self) -> dict[str, Any]:
        return {
            "category": self.category,
            "summary": self.summary,
            "confidence": self.confidence,
            "metadata": dict(self.metadata),
        }


class IntelligenceInsights:
    """Creates enterprise intelligence insights."""

    def build_insight(
        self,
        *,
        category: str,
        summary: str,
        confidence: float,
        metadata: Mapping[str, Any] | None = None,
    ) -> IntelligenceInsight:
        return IntelligenceInsight(
            category=category,
            summary=summary,
            confidence=confidence,
            metadata=dict(metadata or {}),
        )

    def from_mapping(
        self,
        data: Mapping[str, Any],
    ) -> IntelligenceInsight:
        return self.build_insight(
            category=str(data.get("category", "")),
            summary=str(data.get("summary", "")),
            confidence=float(data.get("confidence", 0.0)),
            metadata=data.get("metadata", {}),
        )
