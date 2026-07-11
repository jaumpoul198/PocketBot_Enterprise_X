"""
PocketBot Enterprise X

MACD Indicator.
"""

from __future__ import annotations

from collections.abc import Sequence

from pocketbot.domain.candle import Candle
from pocketbot.domain.enums import SignalType
from pocketbot.indicators.base.indicator import Indicator
from pocketbot.indicators.base.result import IndicatorResult
from pocketbot.indicators.math.moving_average import (
    exponential_moving_average,
)


class MACDIndicator(Indicator):
    """
    Moving Average Convergence Divergence.
    """

    def __init__(
        self,
        fast_period: int = 12,
        slow_period: int = 26,
    ) -> None:
        self._fast = fast_period
        self._slow = slow_period

    @property
    def name(self) -> str:
        return "MACD"

    def calculate(
        self,
        candles: Sequence[Candle],
    ) -> IndicatorResult:

        if len(candles) < self._slow:
            raise ValueError("Insufficient candles for MACD calculation.")

        closes = [float(c.close) for c in candles]

        fast = exponential_moving_average(
            closes,
            self._fast,
        )

        slow = exponential_moving_average(
            closes,
            self._slow,
        )

        value = fast - slow

        if value > 0:
            signal = SignalType.BUY
        elif value < 0:
            signal = SignalType.SELL
        else:
            signal = SignalType.NEUTRAL

        return IndicatorResult(
            name=self.name,
            value=value,
            signal=signal,
            strength=0.75,
            confidence=0.75,
            weight=1.10,
        )
