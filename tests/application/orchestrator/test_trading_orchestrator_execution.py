"""
PocketBot Enterprise X

Trading orchestrator execution integration tests.
"""

from __future__ import annotations

from datetime import UTC, datetime

from pocketbot.application.orchestrator.trading_orchestrator import (
    TradingOrchestrator,
)
from pocketbot.application.pipeline.models import (
    TradingRequest,
)
from pocketbot.bootstrap import build_application
from pocketbot.domain.candle import Candle
from pocketbot.domain.value_objects.price import Price
from pocketbot.market.interfaces import (
    MarketRepository,
)
from pocketbot.market.models.market_snapshot import (
    MarketSnapshot,
)
from pocketbot.trading.interfaces.trade_decision_repository import (
    TradeDecisionRepository,
)


def test_trading_orchestrator_executes_complete_flow() -> None:
    """
    Validates complete application trading execution flow.
    """

    provider = build_application()

    market_repository = provider.get_service(
        MarketRepository,
    )

    market_repository.save(
        MarketSnapshot(
            asset="BTCUSDT",
            timeframe=60,
            candles=[
                Candle(
                    symbol="BTCUSDT",
                    timeframe="60",
                    open=Price(100),
                    high=Price(110),
                    low=Price(95),
                    close=Price(108),
                    volume=1000,
                    timestamp=datetime.now(UTC),
                ),
            ],
            provider="test",
            connected=True,
        )
    )

    orchestrator = provider.get_service(
        TradingOrchestrator,
    )

    result = orchestrator.execute(
        TradingRequest(
            asset="BTCUSDT",
            timeframe=60,
        )
    )

    assert result.market.asset == "BTCUSDT"
    assert result.decision is not None

    decision_repository = provider.get_service(
        TradeDecisionRepository,
    )

    decision = decision_repository.get_latest(
        "BTCUSDT",
    )

    assert decision is not None
    assert decision.asset == "BTCUSDT"
