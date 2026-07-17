"""Enterprise Intelligence Recommendations."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Mapping


@dataclass(frozen=True, slots=True)
class IntelligenceRecommendation:
    """Immutable intelligence recommendation."""

    action: str
    reason: str
    priority: str
    confidence: float
    metadata: dict[str, Any]

    def to_dict(self) -> dict[str, Any]:
        return {
            "action": self.action,
            "reason": self.reason,
            "priority": self.priority,
            "confidence": self.confidence,
            "metadata": dict(self.metadata),
        }


class IntelligenceRecommendations:
    """Creates enterprise intelligence recommendations."""

    def build_recommendation(
        self,
        *,
        action: str,
        reason: str,
        priority: str,
        confidence: float,
        metadata: Mapping[str, Any] | None = None,
    ) -> IntelligenceRecommendation:
        return IntelligenceRecommendation(
            action=action,
            reason=reason,
            priority=priority,
            confidence=confidence,
            metadata=dict(metadata or {}),
        )

    def from_mapping(
        self,
        data: Mapping[str, Any],
    ) -> IntelligenceRecommendation:
        return self.build_recommendation(
            action=str(data.get("action", "")),
            reason=str(data.get("reason", "")),
            priority=str(data.get("priority", "")),
            confidence=float(data.get("confidence", 0.0)),
            metadata=data.get("metadata", {}),
        )
