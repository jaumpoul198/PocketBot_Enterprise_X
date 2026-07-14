"""
PocketBot Enterprise X

Application service pipeline unavailable scenarios.
"""

from __future__ import annotations

import pytest

from pocketbot.application.services.application_service import (
    ApplicationService,
)
from pocketbot.application.pipeline.models import (
    TradingRequest,
)


class StubMarket:
    pass


class StubIndicatorPipeline:
    pass


class StubConfluence:
    pass


class StubScoreEngine:
    pass


class StubTradeEngine:
    pass


def test_application_service_pipeline_unavailable() -> None:

    service = ApplicationService(
        market=StubMarket(),
        pipeline=StubIndicatorPipeline(),
        confluence=StubConfluence(),
        score_engine=StubScoreEngine(),
        trade_engine=StubTradeEngine(),
        trading_pipeline=None,
    )

    request = TradingRequest(
        asset="BTCUSDT",
        timeframe=60,
        indicators=[
            "rsi",
        ],
    )

    with pytest.raises(
        RuntimeError,
        match="Trading pipeline is not available.",
    ):
        service.execute_pipeline(
            request,
        )
