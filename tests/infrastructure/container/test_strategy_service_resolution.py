from pocketbot.bootstrap.service_registration import (
    register_services,
)
from pocketbot.infrastructure.container.service_collection import (
    ServiceCollection,
)
from pocketbot.market.strategy.service import StrategyService


def test_strategy_service_is_resolvable_from_container():

    services = ServiceCollection()

    register_services(services)

    provider = services.build_provider()

    strategy_service = provider.get_service(
        StrategyService,
    )

    assert isinstance(
        strategy_service,
        StrategyService,
    )
