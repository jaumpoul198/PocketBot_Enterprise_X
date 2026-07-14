"""
PocketBot Enterprise X

Market Analytics Service.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from pocketbot.domain.candle import Candle
from pocketbot.market.analytics.indicators.base_indicator import (
    BaseIndicator,
)


@dataclass(frozen=True)
class AnalyticsSnapshot:
    """
    Resultado consolidado da análise de mercado.
    """

    values: dict[str, Any]


class AnalyticsService:
    """
    Serviço responsável pela execução dos indicadores técnicos.
    """

    def __init__(
        self,
        indicators: list[BaseIndicator[Any]],
    ) -> None:
        self._indicators = indicators

    def analyze(
        self,
        candles: list[Candle],
    ) -> AnalyticsSnapshot:
        """
        Executa todos os indicadores registrados
        sobre uma sequência de candles.
        """

        results: dict[str, Any] = {}

        for indicator in self._indicators:
            indicator_name = (
                indicator.__class__.__name__
            )

            results[indicator_name] = (
                indicator.calculate(
                    candles,
                )
            )

        return AnalyticsSnapshot(
            values=results,
        )
