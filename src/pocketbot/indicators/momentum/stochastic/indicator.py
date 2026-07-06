"""
PocketBot Enterprise X

Stochastic Oscillator Indicator.
"""

from __future__ import annotations

from collections.abc import Sequence

from pocketbot.domain.candle import Candle
from pocketbot.domain.enums import SignalType
from pocketbot.indicators.base.indicator import Indicator
from pocketbot.indicators.base.result import IndicatorResult


class StochasticIndicator(Indicator):
    """
    Stochastic Oscillator.
    """

    def __init__(
        self,
        period: int = 14,
        overbought: float = 80.0,
        oversold: float = 20.0,
    ) -> None:
        self._period = period
        self._overbought = overbought
        self._oversold = oversold

    @property
    def name(self) -> str:
        return "STOCHASTIC"

    def calculate(
        self,
        candles: Sequence[Candle],
    ) -> IndicatorResult:

        if len(candles) < self._period:
            raise ValueError(
                "Insufficient candles for Stochastic calculation."
            )

        window = candles[-self._period:]

        highest = max(float(c.high) for c in window)
        lowest = min(float(c.low) for c in window)
        close = float(window[-1].close)

        if highest == lowest:
            value = 50.0
        else:
            value = ((close - lowest) / (highest - lowest)) * 100

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
            strength=0.72,
            confidence=0.72,
            weight=1.0,
            metadata={
                "highest": highest,
                "lowest": lowest,
                "overbought": self._overbought,
                "oversold": self._oversold,
            },
        )