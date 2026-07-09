"""
PocketBot Enterprise X
Relative Strength Index Indicator
"""

from __future__ import annotations

from pocketbot.domain.candle import Candle
from pocketbot.market.analytics.indicators.base_indicator import (
    BaseIndicator,
)


class RSIIndicator(BaseIndicator[float]):
    """
    Relative Strength Index (RSI).

    Mede força relativa dos movimentos de preço.
    """

    def __init__(self, period: int) -> None:
        if period <= 0:
            raise ValueError("Period must be positive.")

        self.period = period

    def calculate(
        self,
        candles: list[Candle],
    ) -> float | None:

        if len(candles) <= self.period:
            return None

        closes = [
            candle.close.value
            for candle in candles
        ]

        gains: list[float] = []
        losses: list[float] = []

        for index in range(
            1,
            len(closes),
        ):
            change = closes[index] - closes[index - 1]

            if change > 0:
                gains.append(change)
                losses.append(0.0)
            else:
                gains.append(0.0)
                losses.append(abs(change))

        recent_gains = gains[-self.period:]
        recent_losses = losses[-self.period:]

        average_gain = (
            sum(recent_gains)
            / self.period
        )

        average_loss = (
            sum(recent_losses)
            / self.period
        )

        if average_loss == 0:
            return 100.0

        relative_strength = (
            average_gain
            / average_loss
        )

        return 100 - (
            100
            /
            (1 + relative_strength)
        )
