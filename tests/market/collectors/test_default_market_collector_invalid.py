from pocketbot.market.repositories.in_memory_market_repository import (
    InMemoryMarketRepository,
)
from pocketbot.market.cache.in_memory_market_cache import (
    InMemoryMarketCache,
)
from pocketbot.market.collectors.default_market_collector import (
    DefaultMarketCollector,
)
from pocketbot.market.interfaces import (
    MarketProvider,
)
from pocketbot.market.validators.default_market_validator import (
    DefaultMarketValidator,
)


class InvalidMarketProvider(MarketProvider):
    def connect(self) -> None:
        pass

    def disconnect(self) -> None:
        pass

    def is_connected(self) -> bool:
        return True

    def get_candles(
        self,
        asset: str,
        timeframe: int,
        count: int,
    ) -> list:
        return []


def test_market_collector_rejects_invalid_candles() -> None:
    provider = InvalidMarketProvider()
    validator = DefaultMarketValidator()
    cache = InMemoryMarketCache()
    repository = InMemoryMarketRepository()

    collector = DefaultMarketCollector(
        provider,
        validator,
        cache,
        repository,
    )

    candles = collector.collect(
        "BTCUSDT",
        60,
        10,
    )

    assert candles == []

    cached = cache.load(
        "BTCUSDT",
        60,
    )

    assert cached == []