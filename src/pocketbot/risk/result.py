"""
PocketBot Enterprise X

Risk evaluation result.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import UTC, datetime
from typing import Any


@dataclass(frozen=True, slots=True)
class RiskResult:
    """
    Result produced by the Risk Engine.
    """

    approved: bool

    risk_level: float

    position_size: float

    max_loss: float

    reason: str = ""

    metadata: dict[str, Any] = field(default_factory=dict)

    timestamp: datetime = field(
        default_factory=lambda: datetime.now(UTC),
    )

    def __post_init__(self) -> None:

        if not 0.0 <= self.risk_level <= 1.0:
            raise ValueError("risk_level must be between 0 and 1.")

        if self.position_size < 0:
            raise ValueError("position_size cannot be negative.")

        if self.max_loss < 0:
            raise ValueError("max_loss cannot be negative.")
