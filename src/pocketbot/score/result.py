"""
PocketBot Enterprise X

Score result model.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import UTC, datetime
from typing import Any


@dataclass(frozen=True, slots=True)
class ScoreResult:
    """
    Result produced by the Score Engine.

    This object contains only score metrics.

    The Decision Engine is responsible for converting this
    information into BUY, SELL or WAIT.
    """

    score: float

    confidence: float

    strength: float

    weight_sum: float

    indicators: int

    metadata: dict[str, Any] = field(default_factory=dict)

    timestamp: datetime = field(default_factory=lambda: datetime.now(UTC))

    def __post_init__(self) -> None:
        if not 0.0 <= self.score <= 100.0:
            raise ValueError("score must be between 0 and 100.")

        if not 0.0 <= self.confidence <= 1.0:
            raise ValueError("confidence must be between 0 and 1.")

        if not 0.0 <= self.strength <= 1.0:
            raise ValueError("strength must be between 0 and 1.")

        if self.weight_sum < 0:
            raise ValueError("weight_sum cannot be negative.")

        if self.indicators < 0:
            raise ValueError("indicators cannot be negative.")