"""
PocketBot Enterprise X

Default Market Collector.
"""

from __future__ import annotations

from pocketbot.domain.candle import Candle
from pocketbot.market.interfaces.market_cache import (
    MarketCache,
)
from pocketbot.market.interfaces.market_collector import (
    MarketCollector,
)
from pocketbot.market.interfaces.market_provider import (
    MarketProvider,
)
from pocketbot.market.interfaces.market_validator import (
    MarketValidator,
)


class DefaultMarketCollector(MarketCollector):
    """
    Default implementation of market data collector.
    """

    def __init__(
        self,
        provider: MarketProvider,
        validator: MarketValidator,
        cache: MarketCache,
    ) -> None:
        self._provider = provider
        self._validator = validator
        self._cache = cache

    def collect(
        self,
        asset: str,
        timeframe: int,
        count: int,
    ) -> list[Candle]:
        """
        Collects, validates and caches market candles.
        """

        candles = self._provider.get_candles(
            asset,
            timeframe,
            count,
        )

        if not self._validator.validate(
            candles,
        ):
            return []

        self._cache.save(
            asset,
            timeframe,
            candles,
        )

        return candles