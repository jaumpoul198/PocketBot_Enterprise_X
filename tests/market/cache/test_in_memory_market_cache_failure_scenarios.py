"""
PocketBot Enterprise X

Market cache failure scenario tests.
"""

from __future__ import annotations

from datetime import UTC, datetime

import pytest

from pocketbot.domain.candle import Candle
from pocketbot.market.cache.in_memory_market_cache import (
    InMemoryMarketCache,
)


def create_candle(
    symbol: str = "BTC",
) -> Candle:
    return Candle(
        symbol=symbol,
        timeframe=60,
        timestamp=datetime.now(UTC),
        open=100.0,
        high=110.0,
        low=90.0,
        close=105.0,
        volume=10.0,
    )


def test_load_unknown_market_returns_empty_list() -> None:
    cache = InMemoryMarketCache()

    result = cache.load(
        "UNKNOWN",
        60,
    )

    assert result == []


def test_cache_supports_multiple_assets_without_collision() -> None:
    cache = InMemoryMarketCache()

    cache.save(
        "BTCUSDT",
        60,
        [],
    )

    cache.save(
        "ETHUSDT",
        60,
        [
            create_candle("ETH"),
        ],
    )

    btc = cache.load(
        "BTCUSDT",
        60,
    )

    eth = cache.load(
        "ETHUSDT",
        60,
    )

    assert btc == []
    assert len(eth) == 1
    assert eth[0].symbol == "ETH"


def test_cache_clear_removes_all_entries() -> None:
    cache = InMemoryMarketCache()

    cache.save(
        "BTCUSDT",
        60,
        [],
    )

    cache.clear()

    result = cache.load(
        "BTCUSDT",
        60,
    )

    assert result == []


def test_cache_save_overwrites_previous_value() -> None:
    cache = InMemoryMarketCache()

    cache.save(
        "BTCUSDT",
        60,
        [
            create_candle("OLD"),
        ],
    )

    cache.save(
        "BTCUSDT",
        60,
        [
            create_candle("NEW"),
        ],
    )

    result = cache.load(
        "BTCUSDT",
        60,
    )

    assert result[0].symbol == "NEW"


def test_cache_rejects_none_asset() -> None:
    cache = InMemoryMarketCache()

    with pytest.raises(
        ValueError,
        match="asset cannot be None",
    ):
        cache.save(
            None,  # type: ignore[arg-type]
            60,
            [],
        )


def test_cache_rejects_invalid_asset_type() -> None:
    cache = InMemoryMarketCache()

    with pytest.raises(
        TypeError,
        match="asset must be a string",
    ):
        cache.save(
            123,  # type: ignore[arg-type]
            60,
            [],
        )


def test_cache_rejects_none_timeframe() -> None:
    cache = InMemoryMarketCache()

    with pytest.raises(
        ValueError,
        match="timeframe cannot be None",
    ):
        cache.save(
            "BTCUSDT",
            None,  # type: ignore[arg-type]
            [],
        )


def test_cache_rejects_bool_timeframe() -> None:
    cache = InMemoryMarketCache()

    with pytest.raises(
        TypeError,
        match="timeframe must be an integer",
    ):
        cache.save(
            "BTCUSDT",
            True,
            [],
        )


def test_cache_rejects_invalid_timeframe_type() -> None:
    cache = InMemoryMarketCache()

    with pytest.raises(
        TypeError,
        match="timeframe must be an integer",
    ):
        cache.save(
            "BTCUSDT",
            "60",  # type: ignore[arg-type]
            [],
        )


def test_cache_rejects_none_candles() -> None:
    cache = InMemoryMarketCache()

    with pytest.raises(
        ValueError,
        match="candles cannot be None",
    ):
        cache.save(
            "BTCUSDT",
            60,
            None,  # type: ignore[arg-type]
        )


def test_cache_rejects_invalid_candles_type() -> None:
    cache = InMemoryMarketCache()

    with pytest.raises(
        TypeError,
        match="candles must be a list",
    ):
        cache.save(
            "BTCUSDT",
            60,
            "invalid",  # type: ignore[arg-type]
        )


def test_cache_rejects_invalid_candle_item() -> None:
    cache = InMemoryMarketCache()

    with pytest.raises(
        TypeError,
        match="candles must contain only Candle instances",
    ):
        cache.save(
            "BTCUSDT",
            60,
            [
                "INVALID",  # type: ignore[list-item]
            ],
        )