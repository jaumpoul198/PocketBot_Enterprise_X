"""
PocketBot Enterprise X
Simple Moving Average Indicator
"""

from __future__ import annotations

from pocketbot.domain.candle import Candle
from pocketbot.market.analytics.indicators.base_indicator import (
    BaseIndicator,
)


class SMAIndicator(BaseIndicator[float]):
    """
    Simple Moving Average (SMA).

    Calcula a média simples dos últimos candles.
    """

    def __init__(
        self,
        period: int,
    ) -> None:

        if period <= 0:
            raise ValueError(
                "Period must be positive."
            )

        self.period = period

    def calculate(
        self,
        candles: list[Candle],
    ) -> float | None:

        if len(candles) < self.period:
            return None

        selected_candles = candles[
            -self.period:
        ]

        total = sum(
            candle.close.value
            for candle in selected_candles
        )

        return total / self.period
