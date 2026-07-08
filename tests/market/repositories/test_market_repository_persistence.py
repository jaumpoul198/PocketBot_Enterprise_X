from datetime import UTC, datetime

from pocketbot.market.models.market_snapshot import MarketSnapshot
from pocketbot.market.repositories.in_memory_market_repository import (
    InMemoryMarketRepository,
)


def create_snapshot(
    asset: str,
    timeframe: int,
    provider: str,
) -> MarketSnapshot:

    return MarketSnapshot(
        asset=asset,
        timeframe=timeframe,
        timestamp=datetime.now(UTC),
        provider=provider,
        connected=True,
    )


def test_repository_keeps_different_assets_separated() -> None:
    repository = InMemoryMarketRepository()

    btc = create_snapshot(
        "BTCUSDT",
        5,
        "btc-provider",
    )

    eth = create_snapshot(
        "ETHUSDT",
        5,
        "eth-provider",
    )

    repository.save(btc)
    repository.save(eth)

    btc_result = repository.get_latest(
        "BTCUSDT",
        5,
    )

    eth_result = repository.get_latest(
        "ETHUSDT",
        5,
    )

    assert btc_result is not None
    assert eth_result is not None

    assert btc_result.provider == "btc-provider"
    assert eth_result.provider == "eth-provider"


def test_repository_overwrites_same_asset_and_timeframe() -> None:
    repository = InMemoryMarketRepository()

    old_snapshot = create_snapshot(
        "BTCUSDT",
        5,
        "old",
    )

    new_snapshot = create_snapshot(
        "BTCUSDT",
        5,
        "new",
    )

    repository.save(old_snapshot)
    repository.save(new_snapshot)

    result = repository.get_latest(
        "BTCUSDT",
        5,
    )

    assert result is not None
    assert result.provider == "new"


def test_repository_returns_none_for_unknown_snapshot() -> None:
    repository = InMemoryMarketRepository()

    result = repository.get_latest(
        "UNKNOWN",
        5,
    )

    assert result is None