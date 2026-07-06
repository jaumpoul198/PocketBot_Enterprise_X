"""
PocketBot Enterprise X

RSI Indicator.
"""

from __future__ import annotations

from collections.abc import Sequence

from pocketbot.domain.candle import Candle
from pocketbot.domain.enums import SignalType
from pocketbot.indicators.base.indicator import Indicator
from pocketbot.indicators.base.result import IndicatorResult


class RSIIndicator(Indicator):
    """
    Relative Strength Index.
    """

    def __init__(
        self,
        period: int = 14,
        overbought: float = 70.0,
        oversold: float = 30.0,
    ) -> None:
        self._period = period
        self._overbought = overbought
        self._oversold = oversold

    @property
    def name(self) -> str:
        return "RSI"

    def calculate(
        self,
        candles: Sequence[Candle],
    ) -> IndicatorResult:

        if len(candles) < self._period + 1:
            raise ValueError(
                "Insufficient candles for RSI calculation."
            )

        closes = [float(c.close) for c in candles]

        gains: list[float] = []
        losses: list[float] = []

        for i in range(1, len(closes)):
            change = closes[i] - closes[i - 1]

            if change >= 0:
                gains.append(change)
                losses.append(0.0)
            else:
                gains.append(0.0)
                losses.append(abs(change))

        avg_gain = sum(gains[-self._period:]) / self._period
        avg_loss = sum(losses[-self._period:]) / self._period

        if avg_loss == 0:
            value = 100.0
        else:
            rs = avg_gain / avg_loss
            value = 100 - (100 / (1 + rs))

        if value >= self._overbought:
            signal = SignalType.SELL
        elif value <= self._oversold:
            signal = SignalType.BUY
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