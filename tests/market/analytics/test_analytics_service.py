"""
Tests for Market Analytics Service
"""

from pocketbot.market.analytics.analytics_service import (
    AnalyticsService,
)


class FakeIndicator:
    def calculate(self, candles):
        return 123


def test_analytics_service_executes_indicators():

    service = AnalyticsService(
        indicators=[
            FakeIndicator()
        ]
    )

    result = service.analyze(
        candles=[]
    )

    assert result.values[
        "FakeIndicator"
    ] == 123
