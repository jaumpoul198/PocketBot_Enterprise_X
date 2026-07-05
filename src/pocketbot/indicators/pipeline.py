"""
PocketBot Enterprise X

Indicator execution pipeline.
"""

from __future__ import annotations

from collections.abc import Sequence

from pocketbot.domain.candle import Candle
from pocketbot.indicators.base.result import IndicatorResult
from pocketbot.indicators.manager import IndicatorManager


class IndicatorPipeline:
    """
    Executa um pipeline completo de indicadores.
    """

    def __init__(
        self,
        manager: IndicatorManager,
    ) -> None:
        self._manager = manager

    def execute(
        self,
        indicators: Sequence[str],
        candles: Sequence[Candle],
    ) -> list[IndicatorResult]:
        return self._manager.run(
            indicators,
            candles,
        )
