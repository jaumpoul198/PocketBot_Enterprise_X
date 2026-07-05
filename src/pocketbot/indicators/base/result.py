"""
PocketBot Enterprise X

Indicator result model.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import UTC, datetime
from typing import Any

from pocketbot.domain.enums import SignalType


@dataclass(frozen=True, slots=True)
class IndicatorResult:
    """
    Standard result returned by every indicator.
    """

    name: str
    value: float | int | bool | None
    signal: SignalType

    strength: float
    confidence: float
    weight: float = 1.0

    metadata: dict[str, Any] = field(default_factory=dict)

    timestamp: datetime = field(default_factory=lambda: datetime.now(UTC))

    def __post_init__(self) -> None:
        """
        Validate object consistency.
        """

        if not 0.0 <= self.strength <= 1.0:
            raise ValueError("strength must be between 0 and 1.")

        if not 0.0 <= self.confidence <= 1.0:
            raise ValueError("confidence must be between 0 and 1.")

        if self.weight < 0:
            raise ValueError("weight cannot be negative.")
