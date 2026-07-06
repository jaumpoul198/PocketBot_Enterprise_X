"""
PocketBot Enterprise X

ATR Indicator.
"""

from __future__ import annotations

from collections.abc import Sequence

from pocketbot.domain.candle import Candle
from pocketbot.domain.enums import SignalType
from pocketbot.indicators.base.indicator import Indicator
from pocketbot.indicators.base.result import IndicatorResult


class ATRIndicator(Indicator):
    """
    Average True Range indicator.
    """

    def __init__(
        self,
        period: int = 14,
    ) -> None:
        self._period = period

    @property
    def name(self) -> str:
        return "ATR"

    def calculate(
        self,
        candles: Sequence[Candle],
    ) -> IndicatorResult:

        if len(candles) < self._period + 1:
            raise ValueError(
                "Insufficient candles for ATR calculation."
            )

        true_ranges: list[float] = []

        previous_close = float(candles[0].close)

        for candle in candles[1:]:

            high = float(candle.high)
            low = float(candle.low)

            tr = max(
                high - low,
                abs(high - previous_close),
                abs(low - previous_close),
            )

            true_ranges.append(tr)

            previous_close = float(candle.close)

        value = sum(true_ranges[-self._period:]) / self._period

        return IndicatorResult(
            name=self.name,
            value=value,
            signal=SignalType.NEUTRAL,
            strength=0.60,
            confidence=0.60,
            weight=0.80,
        )