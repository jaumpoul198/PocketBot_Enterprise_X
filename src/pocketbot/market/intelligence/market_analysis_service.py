"""
PocketBot Enterprise X
Market Analysis Service
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from pocketbot.domain.candle import Candle

from pocketbot.market.analytics.analytics_service import (
    AnalyticsService,
    AnalyticsSnapshot,
)


@dataclass(frozen=True)
class MarketAnalysisResult:
    """
    Resultado consolidado da análise de mercado.
    """

    analytics: AnalyticsSnapshot


class MarketAnalysisService:
    """
    Serviço responsável pela consolidação da análise de mercado.
    """

    def __init__(
        self,
        analytics_service: AnalyticsService,
    ) -> None:
        self._analytics_service = analytics_service

    def analyze(
        self,
        candles: list[Candle],
    ) -> MarketAnalysisResult:
        """
        Executa a análise completa do mercado.
        """

        analytics = self._analytics_service.analyze(
            candles
        )

        return MarketAnalysisResult(
            analytics=analytics
        )
