"""
PocketBot Enterprise X
Exponential Moving Average Indicator
"""

from __future__ import annotations

from dataclasses import dataclass

from pocketbot.domain.candle import Candle


@dataclass(slots=True, frozen=True)
class EMAIndicator:
    """
    Calcula a média móvel exponencial baseada no preço de fechamento
    dos candles.
    """

    period: int

    def __post_init__(self) -> None:
        if self.period <= 0:
            raise ValueError(
                "EMA period must be greater than zero"
            )

    def calculate(
        self,
        candles: list[Candle],
    ) -> float | None:
        """
        Calcula a média móvel exponencial.

        Retorna None quando não existem candles suficientes.
        """

        if len(candles) < self.period:
            return None

        prices = [
            float(candle.close)
            for candle in candles[-self.period:]
        ]

        multiplier = 2 / (self.period + 1)

        ema = prices[0]

        for price in prices[1:]:
            ema = (
                (price - ema) * multiplier
            ) + ema

        return ema
