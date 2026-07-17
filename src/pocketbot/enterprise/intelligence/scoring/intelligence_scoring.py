"""Enterprise Intelligence Scoring."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Mapping


@dataclass(frozen=True, slots=True)
class IntelligenceScore:
    """Immutable intelligence score result."""

    name: str
    value: float
    threshold: float
    passed: bool
    metadata: dict[str, Any]

    def to_dict(self) -> dict[str, Any]:
        return {
            "name": self.name,
            "value": self.value,
            "threshold": self.threshold,
            "passed": self.passed,
            "metadata": dict(self.metadata),
        }


class IntelligenceScoring:
    """Calculates enterprise intelligence scores."""

    def calculate(
        self,
        *,
        name: str,
        value: float,
        threshold: float,
        metadata: Mapping[str, Any] | None = None,
    ) -> IntelligenceScore:
        return IntelligenceScore(
            name=name,
            value=value,
            threshold=threshold,
            passed=value >= threshold,
            metadata=dict(metadata or {}),
        )

    def from_mapping(
        self,
        data: Mapping[str, Any],
    ) -> IntelligenceScore:
        return self.calculate(
            name=str(data.get("name", "")),
            value=float(data.get("value", 0.0)),
            threshold=float(data.get("threshold", 0.0)),
            metadata=data.get("metadata", {}),
        )
