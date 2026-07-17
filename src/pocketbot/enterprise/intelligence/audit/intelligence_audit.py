"""Enterprise Intelligence Audit."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Mapping


@dataclass(frozen=True, slots=True)
class IntelligenceAuditRecord:
    """Immutable audit record."""

    event: str
    actor: str
    success: bool
    metadata: dict[str, Any]

    def to_dict(self) -> dict[str, Any]:
        return {
            "event": self.event,
            "actor": self.actor,
            "success": self.success,
            "metadata": dict(self.metadata),
        }


class IntelligenceAudit:
    """Manages enterprise intelligence audit records."""

    def record(
        self,
        *,
        event: str,
        actor: str,
        success: bool,
        metadata: Mapping[str, Any] | None = None,
    ) -> IntelligenceAuditRecord:
        return IntelligenceAuditRecord(
            event=event,
            actor=actor,
            success=success,
            metadata=dict(metadata or {}),
        )

    def from_mapping(
        self,
        data: Mapping[str, Any],
    ) -> IntelligenceAuditRecord:
        return self.record(
            event=str(data.get("event", "")),
            actor=str(data.get("actor", "")),
            success=bool(data.get("success", False)),
            metadata=data.get("metadata", {}),
        )
