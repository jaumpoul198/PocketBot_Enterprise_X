"""
PocketBot Enterprise X

Indicator execution engine.
"""

from __future__ import annotations

from collections.abc import Sequence

from pocketbot.domain.candle import Candle
from pocketbot.indicators.base.result import IndicatorResult
from pocketbot.indicators.factory import IndicatorFactory


class IndicatorEngine:
    """
    Executa indicadores registrados.
    """

    def __init__(
        self,
        factory: IndicatorFactory,
    ) -> None:
        self._factory = factory

    def execute(
        self,
        name: str,
        candles: Sequence[Candle],
        **kwargs: object,
    ) -> IndicatorResult:
        """
        Executa um indicador.
        """

        indicator = self._factory.create(
            name=name,
            **kwargs,
        )

        return indicator.calculate(candles)
