"""
PocketBot Enterprise X
Market Analysis Service
"""

from __future__ import annotations

from dataclasses import dataclass

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
        if analytics_service is None:
            raise ValueError(
                "analytics_service cannot be None",
            )

        if not hasattr(
            analytics_service,
            "analyze",
        ):
            raise TypeError(
                "analytics_service must provide analyze",
            )

        self._analytics_service = analytics_service

    def analyze(
        self,
        candles: list[Candle],
    ) -> MarketAnalysisResult:
        """
        Executa a análise completa do mercado.
        """

        if candles is None:
            raise ValueError(
                "candles cannot be None",
            )

        if not isinstance(
            candles,
            list,
        ):
            raise TypeError(
                "candles must be a list",
            )

        analytics = self._analytics_service.analyze(
            candles,
        )

        if not isinstance(
            analytics,
            AnalyticsSnapshot,
        ):
            raise TypeError(
                "analytics result must be AnalyticsSnapshot",
            )

        return MarketAnalysisResult(
            analytics=analytics,
        )
