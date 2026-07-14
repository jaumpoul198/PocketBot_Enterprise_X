"""
PocketBot Enterprise X

Trade Decision Model.
"""

from __future__ import annotations

import math
from dataclasses import dataclass
from datetime import datetime


@dataclass(slots=True, frozen=True)
class TradeDecision:
    """
    Represents a generated trading decision.
    """

    asset: str

    decision: str

    strategy: str | None

    score: float

    timestamp: datetime

    def __post_init__(self) -> None:
        if not isinstance(self.asset, str):
            raise TypeError(
                "asset must be a string",
            )

        if not self.asset.strip():
            raise ValueError(
                "asset cannot be empty",
            )

        if not isinstance(self.decision, str):
            raise TypeError(
                "decision must be a string",
            )

        if not self.decision.strip():
            raise ValueError(
                "decision cannot be empty",
            )

        if self.strategy is not None:
            if not isinstance(self.strategy, str):
                raise TypeError(
                    "strategy must be a string or None",
                )

            if not self.strategy.strip():
                raise ValueError(
                    "strategy cannot be empty",
                )

        if isinstance(self.score, bool):
            raise TypeError(
                "score cannot be boolean",
            )

        if not isinstance(self.score, (int, float)):
            raise TypeError(
                "score must be numeric",
            )

        if not math.isfinite(float(self.score)):
            raise ValueError(
                "score must be finite",
            )

        if not isinstance(self.timestamp, datetime):
            raise TypeError(
                "timestamp must be datetime",
            )