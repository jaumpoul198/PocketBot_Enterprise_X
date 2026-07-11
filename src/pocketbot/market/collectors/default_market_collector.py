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
from pocketbot.market.interfaces.market_repository import (
    MarketRepository,
)
from pocketbot.market.interfaces.market_validator import (
    MarketValidator,
)
from pocketbot.market.models.market_snapshot import (
    MarketSnapshot,
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
        repository: MarketRepository,
    ) -> None:
        self._provider = provider
        self._validator = validator
        self._cache = cache
        self._repository = repository

    def collect(
        self,
        asset: str,
        timeframe: int,
        count: int,
    ) -> list[Candle]:
        """
        Collects, validates, caches and persists market candles.
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

        snapshot = MarketSnapshot(
            asset=asset,
            timeframe=timeframe,
            candles=candles,
        )

        self._repository.save(
            snapshot,
        )

        return candles
