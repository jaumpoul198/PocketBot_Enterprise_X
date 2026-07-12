from __future__ import annotations

from datetime import UTC, datetime

from pocketbot.domain.candle import Candle
from pocketbot.market.cache.in_memory_market_cache import (
    InMemoryMarketCache,
)


def create_candle() -> Candle:
    return Candle(
        symbol="BTC",
        timeframe=1,
        timestamp=datetime.now(UTC),
        open=100.0,
        high=110.0,
        low=90.0,
        close=105.0,
        volume=10.0,
    )


def test_saved_candles_are_isolated_from_external_mutation() -> None:
    cache = InMemoryMarketCache()

    candles = [
        create_candle(),
    ]

    cache.save(
        "BTC",
        1,
        candles,
    )

    candles.clear()

    stored = cache.load(
        "BTC",
        1,
    )

    assert len(stored) == 1


def test_loaded_candles_are_isolated_from_cache_state() -> None:
    cache = InMemoryMarketCache()

    cache.save(
        "BTC",
        1,
        [
            create_candle(),
        ],
    )

    loaded = cache.load(
        "BTC",
        1,
    )

    loaded.clear()

    again = cache.load(
        "BTC",
        1,
    )

    assert len(again) == 1
