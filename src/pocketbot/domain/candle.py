from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime

from pocketbot.domain.value_objects.price import Price


@dataclass(slots=True, frozen=True)
class Candle:
    """
    Representa um candle do mercado.
    """

    symbol: str

    timeframe: str

    open: Price

    high: Price

    low: Price

    close: Price

    volume: float

    timestamp: datetime

    @property
    def body(self) -> float:
        return abs(float(self.close) - float(self.open))

    @property
    def range(self) -> float:
        return float(self.high) - float(self.low)

    @property
    def bullish(self) -> bool:
        return float(self.close) > float(self.open)

    @property
    def bearish(self) -> bool:
        return float(self.close) < float(self.open)

    @property
    def doji(self) -> bool:
        if self.range == 0:
            return True

        return self.body <= self.range * 0.05
