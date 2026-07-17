"""Enterprise Intelligence Reporting."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Mapping


@dataclass(frozen=True, slots=True)
class IntelligenceReport:
    """Immutable enterprise intelligence report."""

    title: str
    generated_at: str
    metrics: dict[str, Any]

    def to_dict(self) -> dict[str, Any]:
        return {
            "title": self.title,
            "generated_at": self.generated_at,
            "metrics": dict(self.metrics),
        }


class IntelligenceReporting:
    """Creates enterprise intelligence reports."""

    def build_report(
        self,
        *,
        title: str,
        generated_at: str,
        metrics: Mapping[str, Any] | None = None,
    ) -> IntelligenceReport:
        return IntelligenceReport(
            title=title,
            generated_at=generated_at,
            metrics=dict(metrics or {}),
        )

    def from_mapping(
        self,
        data: Mapping[str, Any],
    ) -> IntelligenceReport:
        return self.build_report(
            title=str(data.get("title", "")),
            generated_at=str(data.get("generated_at", "")),
            metrics=data.get("metrics", {}),
        )
