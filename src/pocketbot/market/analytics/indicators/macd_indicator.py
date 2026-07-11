"""
PocketBot Enterprise X
Moving Average Convergence Divergence Indicator
"""

from __future__ import annotations

from pocketbot.domain.candle import Candle
from pocketbot.market.analytics.indicators.base_indicator import (
    BaseIndicator,
)


class MACDIndicator(BaseIndicator[float]):
    """
    MACD simplificado.

    MACD = média rápida - média lenta
    """

    def __init__(
        self,
        fast_period: int = 12,
        slow_period: int = 26,
    ) -> None:

        if fast_period <= 0:
            raise ValueError(
                "Fast period must be positive."
            )

        if slow_period <= 0:
            raise ValueError(
                "Slow period must be positive."
            )

        if fast_period >= slow_period:
            raise ValueError(
                "Fast period must be lower than slow period."
            )

        self.fast_period = fast_period
        self.slow_period = slow_period

    def calculate(
        self,
        candles: list[Candle],
    ) -> float | None:

        if len(candles) < self.slow_period:
            return None

        closes = [
            candle.close.value
            for candle in candles
        ]

        fast_average = sum(
            closes[-self.fast_period:]
        ) / self.fast_period

        slow_average = sum(
            closes[-self.slow_period:]
        ) / self.slow_period

        return fast_average - slow_average
