"""
PocketBot Enterprise X

Simple Moving Average Indicator.
"""

from __future__ import annotations

from collections.abc import Sequence

from pocketbot.domain.candle import Candle
from pocketbot.domain.enums import SignalType
from pocketbot.indicators.base.indicator import Indicator
from pocketbot.indicators.base.result import IndicatorResult
from pocketbot.indicators.math.moving_average import (
    simple_moving_average,
)


class SMAIndicator(Indicator):
    """
    Simple Moving Average indicator.
    """

    def __init__(
        self,
        period: int = 20,
    ) -> None:
        self._period = period

    @property
    def name(self) -> str:
        return "SMA"

    def calculate(
        self,
        candles: Sequence[Candle],
    ) -> IndicatorResult:

        if len(candles) < self._period:
            raise ValueError(
                "Insufficient candles for SMA calculation."
            )

        closes = [
            float(candle.close)
            for candle in candles
        ]

        value = simple_moving_average(
            values=closes,
            period=self._period,
        )

        last_price = closes[-1]

        if last_price > value:
            signal = SignalType.BUY
        elif last_price < value:
            signal = SignalType.SELL
        else:
            signal = SignalType.NEUTRAL

        return IndicatorResult(
            name=self.name,
            value=value,
            signal=signal,
            strength=0.70,
            confidence=0.70,
            weight=1.0,
        )