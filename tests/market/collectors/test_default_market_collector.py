from pocketbot.market.cache.in_memory_market_cache import (
    InMemoryMarketCache,
)
from pocketbot.market.collectors.default_market_collector import (
    DefaultMarketCollector,
)
from pocketbot.market.providers.default_provider import (
    DefaultMarketProvider,
)
from pocketbot.market.validators.default_market_validator import (
    DefaultMarketValidator,
)


def test_market_collector_collects_and_caches_candles() -> None:
    provider = DefaultMarketProvider()
    validator = DefaultMarketValidator()
    cache = InMemoryMarketCache()

    collector = DefaultMarketCollector(
        provider,
        validator,
        cache,
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

    cached = cache.load(
        "BTCUSDT",
        60,
    )

    assert cached == candles

