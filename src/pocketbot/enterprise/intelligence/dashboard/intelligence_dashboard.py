"""Enterprise Intelligence Dashboard."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Mapping


@dataclass(frozen=True, slots=True)
class IntelligenceDashboardSnapshot:
    """Immutable dashboard snapshot."""

    title: str
    generated_at: str
    widgets: dict[str, Any]

    def to_dict(self) -> dict[str, Any]:
        return {
            "title": self.title,
            "generated_at": self.generated_at,
            "widgets": dict(self.widgets),
        }


class IntelligenceDashboard:
    """Builds enterprise intelligence dashboard snapshots."""

    def build_snapshot(
        self,
        *,
        title: str,
        generated_at: str,
        widgets: Mapping[str, Any] | None = None,
    ) -> IntelligenceDashboardSnapshot:
        return IntelligenceDashboardSnapshot(
            title=title,
            generated_at=generated_at,
            widgets=dict(widgets or {}),
        )

    def from_mapping(
        self,
        data: Mapping[str, Any],
    ) -> IntelligenceDashboardSnapshot:
        return self.build_snapshot(
            title=str(data.get("title", "")),
            generated_at=str(data.get("generated_at", "")),
            widgets=data.get("widgets", {}),
        )
