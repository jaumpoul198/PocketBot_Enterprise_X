"""
Tests for Market Analysis Service
"""

from pocketbot.market.analytics.analytics_service import (
    AnalyticsSnapshot,
)

from pocketbot.market.intelligence.market_analysis_service import (
    MarketAnalysisService,
)


class FakeAnalyticsService:

    def analyze(self, candles):

        return AnalyticsSnapshot(
            values={
                "SMAIndicator": 100
            }
        )


def test_market_analysis_service_returns_analysis():

    service = MarketAnalysisService(
        analytics_service=FakeAnalyticsService()
    )

    result = service.analyze(
        candles=[]
    )

    assert (
        result.analytics.values["SMAIndicator"]
        == 100
    )
