from datetime import UTC, datetime

from pocketbot.market.models.market_snapshot import MarketSnapshot
from pocketbot.market.repositories.in_memory_market_repository import (
    InMemoryMarketRepository,
)


def test_save_and_get_latest_snapshot() -> None:
    repository = InMemoryMarketRepository()

    snapshot = MarketSnapshot(
        asset="BTCUSDT",
        timeframe=5,
        timestamp=datetime.now(UTC),
        provider="test",
        connected=True,
    )

    repository.save(snapshot)

    result = repository.get_latest(
        asset="BTCUSDT",
        timeframe=5,
    )

    assert result is not None
    assert result.asset == "BTCUSDT"
    assert result.timeframe == 5
    assert result.provider == "test"


def test_clear_repository() -> None:
    repository = InMemoryMarketRepository()

    snapshot = MarketSnapshot(
        asset="ETHUSDT",
        timeframe=15,
    )

    repository.save(snapshot)

    repository.clear()

    result = repository.get_latest(
        asset="ETHUSDT",
        timeframe=15,
    )

    assert result is None
