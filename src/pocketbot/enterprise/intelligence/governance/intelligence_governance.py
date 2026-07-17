"""Enterprise Intelligence Governance."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Mapping


@dataclass(frozen=True, slots=True)
class IntelligenceGovernancePolicy:
    """Immutable governance policy definition."""

    name: str
    level: str
    enabled: bool
    rules: dict[str, Any]

    def to_dict(self) -> dict[str, Any]:
        return {
            "name": self.name,
            "level": self.level,
            "enabled": self.enabled,
            "rules": dict(self.rules),
        }


class IntelligenceGovernance:
    """Manages enterprise intelligence governance policies."""

    def create_policy(
        self,
        *,
        name: str,
        level: str,
        enabled: bool,
        rules: Mapping[str, Any] | None = None,
    ) -> IntelligenceGovernancePolicy:
        return IntelligenceGovernancePolicy(
            name=name,
            level=level,
            enabled=enabled,
            rules=dict(rules or {}),
        )

    def from_mapping(
        self,
        data: Mapping[str, Any],
    ) -> IntelligenceGovernancePolicy:
        return self.create_policy(
            name=str(data.get("name", "")),
            level=str(data.get("level", "")),
            enabled=bool(data.get("enabled", False)),
            rules=data.get("rules", {}),
        )
