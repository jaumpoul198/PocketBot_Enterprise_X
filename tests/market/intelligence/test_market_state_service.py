from datetime import datetime, UTC

from pocketbot.market.intelligence.market_state_service import (
    MarketStateService,
)

from pocketbot.market.models.market_snapshot import (
    MarketSnapshot,
)

from pocketbot.market.repositories.in_memory_market_repository import (
    InMemoryMarketRepository,
)

from pocketbot.domain.candle import Candle
from pocketbot.domain.value_objects.price import Price



def create_snapshot(price: float) -> MarketSnapshot:

    candle = Candle(
        symbol="BTCUSDT",
        timeframe="60",
        open=Price(price),
        high=Price(price),
        low=Price(price),
        close=Price(price),
        volume=100,
        timestamp=datetime.now(UTC),
    )

    return MarketSnapshot(
        asset="BTCUSDT",
        timeframe=60,
        candles=[candle],
    )


def test_market_state_detects_uptrend():

    repository = InMemoryMarketRepository()

    repository.save(
        create_snapshot(100)
    )

    repository.save(
        create_snapshot(110)
    )

    service = MarketStateService(
        repository
    )

    result = service.get_current_state(
        "BTCUSDT",
        60,
    )

    assert result is not None
    assert result.trend == "UP"
    assert result.change_percent == 10


def test_market_state_returns_none_without_history():

    repository = InMemoryMarketRepository()

    repository.save(
        create_snapshot(100)
    )

    service = MarketStateService(
        repository
    )

    result = service.get_current_state(
        "BTCUSDT",
        60,
    )

    assert result is None
