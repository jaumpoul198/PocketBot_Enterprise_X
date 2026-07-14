from __future__ import annotations

import math

from dataclasses import dataclass
from enum import Enum


class StrategySignal(Enum):
    BUY = "BUY"
    SELL = "SELL"
    HOLD = "HOLD"


@dataclass(frozen=True)
class StrategyResult:
    signal: StrategySignal
    confidence: float
    reason: str

    def __post_init__(self) -> None:
        if not isinstance(
            self.signal,
            StrategySignal,
        ):
            raise TypeError(
                "signal must be a StrategySignal"
            )

        if not isinstance(
            self.confidence,
            (int, float),
        ) or isinstance(
            self.confidence,
            bool,
        ):
            raise TypeError(
                "confidence must be numeric"
            )

        if not math.isfinite(
            float(self.confidence),
        ):
            raise ValueError(
                "confidence must be finite"
            )

        if not 0.0 <= self.confidence <= 1.0:
            raise ValueError(
                "confidence must be between 0 and 1"
            )

        if not isinstance(
            self.reason,
            str,
        ):
            raise TypeError(
                "reason must be a string"
            )

        if not self.reason.strip():
            raise ValueError(
                "reason cannot be empty"
            )
