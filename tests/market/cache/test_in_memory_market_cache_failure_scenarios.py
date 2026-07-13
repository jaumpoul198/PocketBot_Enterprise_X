"""
PocketBot Enterprise X

Market cache failure scenario tests.
"""

from __future__ import annotations

import pytest

from pocketbot.market.cache.in_memory_market_cache import (
    InMemoryMarketCache,
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
            "ETH",
        ],  # type: ignore[list-item]
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
    assert eth == [
        "ETH",
    ]


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
            "OLD",
        ],  # type: ignore[list-item]
    )

    cache.save(
        "BTCUSDT",
        60,
        [
            "NEW",
        ],  # type: ignore[list-item]
    )

    result = cache.load(
        "BTCUSDT",
        60,
    )

    assert result == [
        "NEW",
    ]


def test_cache_rejects_invalid_internal_operations() -> None:
    cache = InMemoryMarketCache()

    with pytest.raises(
        TypeError,
    ):
        cache.save(
            None,  # type: ignore[arg-type]
            60,
            [],
        )
