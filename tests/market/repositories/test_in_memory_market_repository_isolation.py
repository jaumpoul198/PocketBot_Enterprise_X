from __future__ import annotations

from datetime import UTC, datetime

from pocketbot.market.models.market_snapshot import MarketSnapshot
from pocketbot.market.repositories.in_memory_market_repository import (
    InMemoryMarketRepository,
)


def create_snapshot() -> MarketSnapshot:
    return MarketSnapshot(
        asset="BTC",
        timeframe=1,
        timestamp=datetime.now(UTC),
    )


def test_saved_snapshot_is_isolated_from_external_mutation() -> None:
    repository = InMemoryMarketRepository()

    snapshot = create_snapshot()

    repository.save(snapshot)

    snapshot.asset = "ETH"

    stored = repository.get_latest(
        "BTC",
        1,
    )

    assert stored is not None
    assert stored.asset == "BTC"


def test_retrieved_snapshot_is_isolated_from_external_mutation() -> None:
    repository = InMemoryMarketRepository()

    repository.save(
        create_snapshot()
    )

    stored = repository.get_latest(
        "BTC",
        1,
    )

    assert stored is not None

    stored.asset = "ETH"

    again = repository.get_latest(
        "BTC",
        1,
    )

    assert again is not None
    assert again.asset == "BTC"
