from datetime import UTC, datetime

from pocketbot.domain.candle import Candle
from pocketbot.domain.value_objects.price import Price
from pocketbot.market.intelligence.market_history_service import (
    MarketHistoryService,
)
from pocketbot.market.models.market_snapshot import MarketSnapshot
from pocketbot.market.repositories.in_memory_market_repository import (
    InMemoryMarketRepository,
)


def create_snapshot(
    asset: str = "BTCUSDT",
) -> MarketSnapshot:
    return MarketSnapshot(
        asset=asset,
        timeframe=60,
        candles=[
            Candle(
                symbol=asset,
                timeframe="60",
                open=Price(100),
                high=Price(110),
                low=Price(90),
                close=Price(105),
                volume=1000,
                timestamp=datetime.now(UTC),
            )
        ],
    )


def test_market_history_returns_last_n_snapshots() -> None:
    repository = InMemoryMarketRepository()

    repository.save(create_snapshot())

    service = MarketHistoryService(repository)

    result = service.get_last_n(
        "BTCUSDT",
        60,
        1,
    )

    assert len(result) == 1


def test_market_history_returns_snapshots_between_dates() -> None:
    repository = InMemoryMarketRepository()

    snapshot = create_snapshot()

    repository.save(snapshot)

    service = MarketHistoryService(repository)

    result = service.get_between(
        "BTCUSDT",
        60,
        snapshot.timestamp,
        snapshot.timestamp,
    )

    assert len(result) == 1
