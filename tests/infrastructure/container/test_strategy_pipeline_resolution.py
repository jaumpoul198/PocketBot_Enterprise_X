from pocketbot.infrastructure.container.service_collection import (
    ServiceCollection,
)
from pocketbot.bootstrap.service_registration import (
    register_services,
)
from pocketbot.market.strategy.service import (
    StrategyService,
)
from pocketbot.market.strategy.selector.selector import (
    StrategySelectorEngine,
)
from pocketbot.market.strategy.selector.ranking import (
    StrategyRankingEngine,
)
from pocketbot.market.strategy.momentum import (
    MomentumStrategy,
)
from pocketbot.market.strategy.mean_reversion import (
    MeanReversionStrategy,
)
from pocketbot.market.strategy.breakout import (
    BreakoutStrategy,
)


def test_strategy_pipeline_resolves_real_strategies():

    services = ServiceCollection()

    register_services(services)

    provider = services.build_provider()

    strategy_service = provider.get_service(
        StrategyService,
    )

    assert isinstance(
        strategy_service._strategies[0],
        MomentumStrategy,
    )

    assert any(
        isinstance(
            strategy,
            MeanReversionStrategy,
        )
        for strategy in strategy_service._strategies
    )

    assert any(
        isinstance(
            strategy,
            BreakoutStrategy,
        )
        for strategy in strategy_service._strategies
    )


def test_strategy_pipeline_resolves_selector_dependencies():

    services = ServiceCollection()

    register_services(services)

    provider = services.build_provider()

    selector = provider.get_service(
        StrategySelectorEngine,
    )

    assert selector is not None

    ranking = provider.get_service(
        StrategyRankingEngine,
    )

    assert ranking is not None
