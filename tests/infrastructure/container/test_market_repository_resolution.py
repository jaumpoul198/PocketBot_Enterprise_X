from pocketbot.infrastructure.container.service_collection import (
    ServiceCollection,
)
from pocketbot.market.interfaces import (
    MarketRepository,
)
from pocketbot.market.repositories.in_memory_market_repository import (
    InMemoryMarketRepository,
)


def test_market_repository_resolution() -> None:
    services = ServiceCollection()

    services.add_singleton(
        MarketRepository,
        InMemoryMarketRepository,
    )

    provider = services.build_provider()

    repository = provider.get_service(
        MarketRepository,
    )

    assert isinstance(
        repository,
        InMemoryMarketRepository,
    )
