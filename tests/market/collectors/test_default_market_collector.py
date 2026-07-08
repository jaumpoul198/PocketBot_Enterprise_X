"""
PocketBot Enterprise X

Default Market Collector.
"""

from __future__ import annotations

from pocketbot.domain.candle import Candle
from pocketbot.market.interfaces.market_collector import (
    MarketCollector,
)
from pocketbot.market.interfaces.market_provider import (
    MarketProvider,
)
from pocketbot.market.collectors.default_market_collector import (
    DefaultMarketCollector,
)
from pocketbot.market.providers.default_provider import (
    DefaultMarketProvider,
)


def test_market_collector_collects_candles() -> None:
    provider = DefaultMarketProvider()

    collector = DefaultMarketCollector(
        provider,
    )

    candles = collector.collect(
        "BTCUSDT",
        60,
        10,
    )

    assert isinstance(
        candles,
        list,
    )

class DefaultMarketCollector(MarketCollector):
    """
    Default implementation of market data collector.
    """

    def __init__(
        self,
        provider: MarketProvider,
    ) -> None:
        self._provider = provider

    def collect(
        self,
        asset: str,
        timeframe: int,
        count: int,
    ) -> list[Candle]:
        """
        Collects market candles from provider.
        """

        return self._provider.get_candles(
            asset,
            timeframe,
            count,
        )