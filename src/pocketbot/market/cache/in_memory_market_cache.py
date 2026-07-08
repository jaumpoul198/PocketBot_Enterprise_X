"""
PocketBot Enterprise X

In Memory Market Cache.
"""

from __future__ import annotations

from pocketbot.domain.candle import Candle
from pocketbot.market.interfaces.market_cache import (
    MarketCache,
)


class InMemoryMarketCache(MarketCache):
    """
    In-memory implementation of market cache.
    """

    def __init__(self) -> None:
        self._cache: dict[
            tuple[str, int],
            list[Candle],
        ] = {}

    def save(
        self,
        asset: str,
        timeframe: int,
        candles: list[Candle],
    ) -> None:
        """
        Stores candles in memory.
        """

        self._cache[
            (asset, timeframe)
        ] = candles

    def load(
        self,
        asset: str,
        timeframe: int,
    ) -> list[Candle]:
        """
        Loads candles from memory.
        """

        return self._cache.get(
            (asset, timeframe),
            [],
        )

    def clear(self) -> None:
        """
        Clears cached market data.
        """

        self._cache.clear()