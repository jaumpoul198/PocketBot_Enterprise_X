"""
PocketBot Enterprise X
Relative Strength Index Indicator
"""

from __future__ import annotations

from dataclasses import dataclass

from pocketbot.domain.candle import Candle
from pocketbot.market.analytics.indicators.base_indicator import (
    BaseIndicator,
)


@dataclass(slots=True, frozen=True)
class RSIIndicator(BaseIndicator):
    """
    Calcula o Relative Strength Index.
    """

    period: int

    def __post_init__(self) -> None:
        if self.period <= 0:
            raise ValueError(
                "RSI period must be greater than zero"
            )

    def calculate(
        self,
        candles: list[Candle],
    ) -> float | None:

        if len(candles) <= self.period:
            return None

        closes = [
            float(candle.close)
            for candle in candles
        ]

        gains: list[float] = []
        losses: list[float] = []

        for index in range(1, len(closes)):
            change = closes[index] - closes[index - 1]

            if change > 0:
                gains.append(change)
                losses.append(0)

            else:
                gains.append(0)
                losses.append(abs(change))

        avg_gain = sum(
            gains[-self.period:]
        ) / self.period

        avg_loss = sum(
            losses[-self.period:]
        ) / self.period

        if avg_loss == 0:
            return 100.0

        rs = avg_gain / avg_loss

        return 100 - (
            100 / (1 + rs)
        )
