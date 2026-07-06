"""
PocketBot Enterprise X

Indicator Engine.
"""

from __future__ import annotations

from collections.abc import Sequence

from pocketbot.domain.candle import Candle
from pocketbot.indicators.base.result import IndicatorResult
from pocketbot.indicators.factory import IndicatorFactory


class IndicatorEngine:
    """
    Executa um único indicador.
    """

    def __init__(
        self,
        factory: IndicatorFactory,
    ) -> None:
        self._factory = factory

    def execute(
        self,
        indicator: str,
        candles: Sequence[Candle],
        **kwargs: object,
    ) -> IndicatorResult:

        instance = self._factory.create(
            indicator,
            **kwargs,
        )

        return instance.calculate(candles)
