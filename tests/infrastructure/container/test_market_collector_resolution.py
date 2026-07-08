from pocketbot.infrastructure.container.service_collection import (
    ServiceCollection,
)
from pocketbot.market.cache.in_memory_market_cache import (
    InMemoryMarketCache,
)
from pocketbot.market.collectors.default_market_collector import (
    DefaultMarketCollector,
)
from pocketbot.market.interfaces import (
    MarketCache,
    MarketCollector,
    MarketProvider,
    MarketValidator,
)
from pocketbot.market.providers.default_provider import (
    DefaultMarketProvider,
)
from pocketbot.market.validators.default_market_validator import (
    DefaultMarketValidator,
)


def test_market_collector_resolution() -> None:
    services = ServiceCollection()

    services.add_singleton(
        MarketProvider,
        DefaultMarketProvider,
    )

    services.add_singleton(
        MarketCache,
        InMemoryMarketCache,
    )

    services.add_singleton(
        MarketValidator,
        DefaultMarketValidator,
    )

    services.add_singleton(
        MarketCollector,
        DefaultMarketCollector,
    )

    provider = services.build_provider()

    collector = provider.get_service(
        MarketCollector,
    )

    assert isinstance(
        collector,
        DefaultMarketCollector,
    )
