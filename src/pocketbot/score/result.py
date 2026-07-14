"""
PocketBot Enterprise X

Score result model.
"""

from __future__ import annotations

import math

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

    timestamp: datetime = field(
        default_factory=lambda: datetime.now(UTC),
    )

    def __post_init__(self) -> None:
        """
        Validate score result contracts.
        """

        numeric_fields = (
            ("score", self.score),
            ("confidence", self.confidence),
            ("strength", self.strength),
            ("weight_sum", self.weight_sum),
        )

        for name, value in numeric_fields:
            if isinstance(value, bool):
                raise TypeError(
                    f"{name} cannot be boolean"
                )

            if not isinstance(
                value,
                (int, float),
            ):
                raise TypeError(
                    f"{name} must be numeric"
                )

            if not math.isfinite(float(value)):
                raise ValueError(
                    f"{name} must be finite"
                )

        if not 0.0 <= float(self.score) <= 100.0:
            raise ValueError(
                "score must be between 0 and 100."
            )

        if not 0.0 <= float(self.confidence) <= 1.0:
            raise ValueError(
                "confidence must be between 0 and 1."
            )

        if not 0.0 <= float(self.strength) <= 1.0:
            raise ValueError(
                "strength must be between 0 and 1."
            )

        if float(self.weight_sum) < 0:
            raise ValueError(
                "weight_sum cannot be negative."
            )

        if isinstance(self.indicators, bool):
            raise TypeError(
                "indicators cannot be boolean"
            )

        if not isinstance(
            self.indicators,
            int,
        ):
            raise TypeError(
                "indicators must be int"
            )

        if self.indicators < 0:
            raise ValueError(
                "indicators cannot be negative."
            )

        if not isinstance(
            self.metadata,
            dict,
        ):
            raise TypeError(
                "metadata must be a dictionary"
            )

        if not isinstance(
            self.timestamp,
            datetime,
        ):
            raise TypeError(
                "timestamp must be datetime"
            )