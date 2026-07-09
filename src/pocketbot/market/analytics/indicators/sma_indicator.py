"""
PocketBot Enterprise X
Simple Moving Average Indicator
"""

from __future__ import annotations

from dataclasses import dataclass

from pocketbot.domain.candle import Candle


@dataclass(slots=True, frozen=True)
class SMAIndicator:
    """
    Calcula a média móvel simples baseada no preço de fechamento
    dos candles.
    """

    period: int

    def __post_init__(self) -> None:
        if self.period <= 0:
            raise ValueError(
                "SMA period must be greater than zero"
            )

    def calculate(
        self,
        candles: list[Candle],
    ) -> float | None:
        """
        Calcula a média móvel simples.

        Retorna None quando não existem candles suficientes.
        """

        if len(candles) < self.period:
            return None

        selected = candles[-self.period:]

        total = sum(
            float(candle.close)
            for candle in selected
        )

        return total / self.period
