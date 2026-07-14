"""
PocketBot Enterprise X

Decision result model.
"""

from __future__ import annotations

import math
from dataclasses import dataclass, field
from typing import Any

from pocketbot.domain.enums import SignalType


@dataclass(slots=True, frozen=True)
class DecisionResult:
    """
    Represents the final trading decision produced by
    the Decision Engine.
    """

    signal: SignalType

    score: float

    confidence: float

    approved: bool

    reason: str

    metadata: dict[str, Any] = field(
        default_factory=dict,
    )

    def __post_init__(self) -> None:

        if not isinstance(
            self.signal,
            SignalType,
        ):
            raise TypeError(
                "signal must be a SignalType"
            )

        if isinstance(
            self.score,
            bool,
        ):
            raise TypeError(
                "score cannot be boolean"
            )

        if not isinstance(
            self.score,
            (int, float),
        ):
            raise TypeError(
                "score must be numeric"
            )

        score = float(self.score)

        if not math.isfinite(score):
            raise ValueError(
                "score must be finite"
            )

        if isinstance(
            self.confidence,
            bool,
        ):
            raise TypeError(
                "confidence cannot be boolean"
            )

        if not isinstance(
            self.confidence,
            (int, float),
        ):
            raise TypeError(
                "confidence must be numeric"
            )

        confidence = float(self.confidence)

        if not math.isfinite(confidence):
            raise ValueError(
                "confidence must be finite"
            )

        if not 0 <= confidence <= 1:
            raise ValueError(
                "confidence must be between 0 and 1"
            )

        if not isinstance(
            self.approved,
            bool,
        ):
            raise TypeError(
                "approved must be boolean"
            )

        if not isinstance(
            self.reason,
            str,
        ):
            raise TypeError(
                "reason must be string"
            )

        if not self.reason.strip():
            raise ValueError(
                "reason cannot be empty"
            )