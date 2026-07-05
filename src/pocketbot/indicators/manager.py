"""
PocketBot Enterprise X

Indicator manager.
"""

from __future__ import annotations

from collections.abc import Sequence

from pocketbot.domain.candle import Candle
from pocketbot.indicators.base.result import IndicatorResult
from pocketbot.indicators.engine import IndicatorEngine


class IndicatorManager:
    """
    Gerencia a execução de indicadores.
    """

    def __init__(
        self,
        engine: IndicatorEngine,
    ) -> None:
        self._engine = engine

    def run(
        self,
        indicators: Sequence[str],
        candles: Sequence[Candle],
    ) -> list[IndicatorResult]:

        results: list[IndicatorResult] = []

        for indicator in indicators:
            results.append(
                self._engine.execute(
                    indicator,
                    candles,
                )
            )

        return results
