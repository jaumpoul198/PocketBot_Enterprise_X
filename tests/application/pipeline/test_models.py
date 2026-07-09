from pocketbot.application.pipeline.models import (
    TradingRequest,
)


def test_trading_request_creation() -> None:
    request = TradingRequest(
        asset="BTCUSDT",
        timeframe=15,
    )

    assert request.asset == "BTCUSDT"
    assert request.timeframe == 15
