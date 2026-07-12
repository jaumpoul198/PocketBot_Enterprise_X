"""
PocketBot Enterprise X

In Memory Market Cache.
"""

from __future__ import annotations

from copy import deepcopy

from pocketbot.domain.candle import Candle
from pocketbot.market.interfaces.market_cache import (
    MarketCache,
)


class InMemoryMarketCache(MarketCache):
    """
    In-memory implementation of market cache.

    Cache state is isolated from external references.
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
        ] = deepcopy(candles)

    def load(
        self,
        asset: str,
        timeframe: int,
    ) -> list[Candle]:
        """
        Loads candles from memory.
        """

        return deepcopy(
            self._cache.get(
                (asset, timeframe),
                [],
            )
        )

    def clear(self) -> None:
        """
        Clears cached market data.
        """

        self._cache.clear()
