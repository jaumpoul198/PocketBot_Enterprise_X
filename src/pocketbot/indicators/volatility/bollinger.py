"""
PocketBot Enterprise X

Bollinger Bands Indicator.
"""

from __future__ import annotations

from collections.abc import Sequence
from math import sqrt

from pocketbot.domain.candle import Candle
from pocketbot.domain.enums import SignalType
from pocketbot.indicators.base.indicator import Indicator
from pocketbot.indicators.base.result import IndicatorResult
from pocketbot.indicators.math.moving_average import simple_moving_average


class BollingerIndicator(Indicator):
    """
    Bollinger Bands indicator.
    """

    def __init__(
        self,
        period: int = 20,
        deviation: float = 2.0,
    ) -> None:
        self._period = period
        self._deviation = deviation

    @property
    def name(self) -> str:
        return "BOLLINGER"

    def calculate(
        self,
        candles: Sequence[Candle],
    ) -> IndicatorResult:

        if len(candles) < self._period:
            raise ValueError("Insufficient candles for Bollinger calculation.")

        closes = [float(c.close) for c in candles]

        sma = simple_moving_average(
            closes,
            self._period,
        )

        window = closes[-self._period :]

        variance = sum((price - sma) ** 2 for price in window) / self._period

        std = sqrt(variance)

        upper = sma + (std * self._deviation)
        lower = sma - (std * self._deviation)

        last = closes[-1]

        if last > upper:
            signal = SignalType.SELL

        elif last < lower:
            signal = SignalType.BUY

        else:
            signal = SignalType.NEUTRAL

        return IndicatorResult(
            name=self.name,
            value=sma,
            signal=signal,
            strength=0.70,
            confidence=0.70,
            weight=1.0,
            metadata={
                "upper": upper,
                "middle": sma,
                "lower": lower,
            },
        )
