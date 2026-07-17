"""Enterprise Intelligence Compliance."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Mapping


@dataclass(frozen=True, slots=True)
class IntelligenceComplianceCheck:
    """Immutable compliance validation result."""

    name: str
    compliant: bool
    severity: str
    details: dict[str, Any]

    def to_dict(self) -> dict[str, Any]:
        return {
            "name": self.name,
            "compliant": self.compliant,
            "severity": self.severity,
            "details": dict(self.details),
        }


class IntelligenceCompliance:
    """Manages enterprise intelligence compliance checks."""

    def check(
        self,
        *,
        name: str,
        compliant: bool,
        severity: str,
        details: Mapping[str, Any] | None = None,
    ) -> IntelligenceComplianceCheck:
        return IntelligenceComplianceCheck(
            name=name,
            compliant=compliant,
            severity=severity,
            details=dict(details or {}),
        )

    def from_mapping(
        self,
        data: Mapping[str, Any],
    ) -> IntelligenceComplianceCheck:
        return self.check(
            name=str(data.get("name", "")),
            compliant=bool(data.get("compliant", False)),
            severity=str(data.get("severity", "")),
            details=data.get("details", {}),
        )
