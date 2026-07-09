"""
PocketBot Enterprise X
MACD Indicator
"""

from __future__ import annotations

from dataclasses import dataclass

from pocketbot.domain.candle import Candle
from pocketbot.market.analytics.indicators.base_indicator import (
    BaseIndicator,
)


@dataclass(slots=True, frozen=True)
class MACDIndicator(BaseIndicator):
    """
    Moving Average Convergence Divergence.

    MACD = EMA rápida - EMA lenta
    """

    fast_period: int
    slow_period: int

    def __post_init__(self) -> None:
        if self.fast_period <= 0:
            raise ValueError(
                "Fast period must be greater than zero"
            )

        if self.slow_period <= 0:
            raise ValueError(
                "Slow period must be greater than zero"
            )

        if self.fast_period >= self.slow_period:
            raise ValueError(
                "Fast period must be smaller than slow period"
            )

    def calculate(
        self,
        candles: list[Candle],
    ) -> float | None:

        if len(candles) < self.slow_period:
            return None

        fast_prices = [
            float(candle.close)
            for candle in candles[-self.fast_period:]
        ]

        slow_prices = [
            float(candle.close)
            for candle in candles[-self.slow_period:]
        ]

        fast_average = (
            sum(fast_prices)
            / self.fast_period
        )

        slow_average = (
            sum(slow_prices)
            / self.slow_period
        )

        return fast_average - slow_average
