from datetime import UTC, datetime, timedelta

from pocketbot.market.models.market_snapshot import MarketSnapshot
from pocketbot.market.repositories.in_memory_market_repository import (
    InMemoryMarketRepository,
)


def create_snapshot() -> MarketSnapshot:
    return MarketSnapshot(
        asset="BTCUSDT",
        timeframe=5,
        timestamp=datetime.now(UTC),
        provider="test",
        connected=True,
    )


def test_get_latest_returns_none_when_repository_is_empty() -> None:
    repository = InMemoryMarketRepository()

    result = repository.get_latest(
        asset="BTCUSDT",
        timeframe=5,
    )

    assert result is None


def test_get_latest_returns_none_for_unknown_asset() -> None:
    repository = InMemoryMarketRepository()

    repository.save(
        create_snapshot(),
    )

    result = repository.get_latest(
        asset="UNKNOWN",
        timeframe=5,
    )

    assert result is None


def test_get_last_n_returns_empty_list_when_no_history_exists() -> None:
    repository = InMemoryMarketRepository()

    result = repository.get_last_n(
        asset="BTCUSDT",
        timeframe=5,
        limit=10,
    )

    assert result == []


def test_get_last_n_with_zero_limit_returns_empty_list() -> None:
    repository = InMemoryMarketRepository()

    repository.save(
        create_snapshot(),
    )

    result = repository.get_last_n(
        asset="BTCUSDT",
        timeframe=5,
        limit=0,
    )

    assert result == []


def test_get_between_returns_empty_list_when_range_has_no_snapshots() -> None:
    repository = InMemoryMarketRepository()

    repository.save(
        create_snapshot(),
    )

    start = datetime.now(UTC) + timedelta(days=1)
    end = start + timedelta(hours=1)

    result = repository.get_between(
        asset="BTCUSDT",
        timeframe=5,
        start=start,
        end=end,
    )

    assert result == []


def test_clear_removes_all_repository_state() -> None:
    repository = InMemoryMarketRepository()

    repository.save(
        create_snapshot(),
    )

    repository.clear()

    latest = repository.get_latest(
        asset="BTCUSDT",
        timeframe=5,
    )

    history = repository.get_last_n(
        asset="BTCUSDT",
        timeframe=5,
        limit=10,
    )

    assert latest is None
    assert history == []
