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

    def _validate_asset(
        self,
        asset: str,
    ) -> None:

        if asset is None:
            raise ValueError(
                "asset cannot be None",
            )

        if not isinstance(
            asset,
            str,
        ):
            raise TypeError(
                "asset must be a string",
            )

        if not asset:
            raise ValueError(
                "asset cannot be empty",
            )

    def _validate_timeframe(
        self,
        timeframe: int,
    ) -> None:

        if timeframe is None:
            raise ValueError(
                "timeframe cannot be None",
            )

        if (
            not isinstance(
                timeframe,
                int,
            )
            or isinstance(
                timeframe,
                bool,
            )
        ):
            raise TypeError(
                "timeframe must be an integer",
            )

    def _validate_candles(
        self,
        candles: list[Candle],
    ) -> None:

        if candles is None:
            raise ValueError(
                "candles cannot be None",
            )

        if not isinstance(
            candles,
            list,
        ):
            raise TypeError(
                "candles must be a list",
            )

        for candle in candles:
            if not isinstance(
                candle,
                Candle,
            ):
                raise TypeError(
                    "candles must contain only Candle instances",
                )

    def save(
        self,
        asset: str,
        timeframe: int,
        candles: list[Candle],
    ) -> None:
        """
        Stores candles in memory.
        """

        self._validate_asset(
            asset,
        )

        self._validate_timeframe(
            timeframe,
        )

        self._validate_candles(
            candles,
        )

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

        self._validate_asset(
            asset,
        )

        self._validate_timeframe(
            timeframe,
        )

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