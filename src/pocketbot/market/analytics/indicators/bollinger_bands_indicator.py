"""
PocketBot Enterprise X
Bollinger Bands Indicator
"""

from __future__ import annotations

from dataclasses import dataclass
import statistics

from pocketbot.domain.candle import Candle
from pocketbot.market.analytics.indicators.base_indicator import (
    BaseIndicator,
)


@dataclass(frozen=True, slots=True)
class BollingerBandsResult:
    """
    Resultado do indicador Bollinger Bands.
    """

    lower: float
    middle: float
    upper: float


class BollingerBandsIndicator(
    BaseIndicator[BollingerBandsResult]
):
    """
    Bollinger Bands.

    Calcula:
    - Banda inferior
    - Média móvel
    - Banda superior
    """

    def __init__(
        self,
        period: int,
        multiplier: float = 2.0,
    ) -> None:

        if period <= 2:
            raise ValueError(
                "Period must be at least 2."
            )

        if multiplier <= 0:
            raise ValueError(
                "Multiplier must be positive."
            )

        self.period = period
        self.multiplier = multiplier

    def calculate(
        self,
        candles: list[Candle],
    ) -> BollingerBandsResult | None:

        if len(candles) < self.period:
            return None

        closes = [
            candle.close.value
            for candle in candles[-self.period:]
        ]

        middle = (
            sum(closes)
            /
            self.period
        )

        deviation = statistics.stdev(
            closes
        )

        upper = (
            middle
            +
            self.multiplier * deviation
        )

        lower = (
            middle
            -
            self.multiplier * deviation
        )

        return BollingerBandsResult(
            lower=lower,
            middle=middle,
            upper=upper,
        )
