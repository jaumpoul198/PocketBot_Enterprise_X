from __future__ import annotations

from dataclasses import dataclass
from math import sqrt

from pocketbot.domain.candle import Candle

from pocketbot.market.analytics.indicators.base_indicator import (
    BaseIndicator,
)


@dataclass(frozen=True, slots=True)
class BollingerBandsResult:
    """
    Resultado do cálculo Bollinger Bands.
    """

    middle: float

    upper: float

    lower: float


class BollingerBandsIndicator(BaseIndicator):
    """
    Indicador Bollinger Bands.

    Calcula:
    - Média móvel simples
    - Banda superior
    - Banda inferior
    """

    def __init__(
        self,
        period: int,
        multiplier: float,
    ) -> None:

        if period <= 0:
            raise ValueError(
                "Period must be positive"
            )

        if multiplier <= 0:
            raise ValueError(
                "Multiplier must be positive"
            )

        self.period = period
        self.multiplier = multiplier


    def calculate(
        self,
        candles: list[Candle],
    ) -> BollingerBandsResult | None:

        if len(candles) < self.period:
            return None

        selected = candles[-self.period:]

        prices = [
            float(candle.close.value)
            for candle in selected
        ]

        middle = (
            sum(prices)
            /
            len(prices)
        )

        variance = (
            sum(
                (price - middle) ** 2
                for price in prices
            )
            /
            len(prices)
        )

        deviation = sqrt(
            variance
        )

        return BollingerBandsResult(
            middle=middle,
            upper=middle + (
                deviation * self.multiplier
            ),
            lower=middle - (
                deviation * self.multiplier
            ),
        )
