"""
PocketBot Enterprise X

Service Registration Bootstrap.
"""

from __future__ import annotations

from pathlib import Path

from pocketbot.application.hosting.hosted_service_manager import (
    HostedServiceManager,
)
from pocketbot.application.lifecycle.lifecycle_manager import (
    LifecycleManager,
)
from pocketbot.application.lifecycle.shutdown import Shutdown
from pocketbot.application.lifecycle.startup import Startup
from pocketbot.application.runtime.application_runtime import (
    ApplicationRuntime,
)
from pocketbot.application.services.application_service import (
    ApplicationService,
)
from pocketbot.application.services.market_query_service import (
    MarketQueryService,
)
from pocketbot.application.services.market_service import (
    MarketService,
)
from pocketbot.bootstrap.indicator_loader import load_indicators
from pocketbot.config.service import ConfigService
from pocketbot.confluence.engine import ConfluenceEngine
from pocketbot.decision.engine import DecisionEngine
from pocketbot.execution.engine import ExecutionEngine
from pocketbot.indicators.engine import IndicatorEngine
from pocketbot.indicators.factory import IndicatorFactory
from pocketbot.indicators.manager import IndicatorManager
from pocketbot.indicators.pipeline import IndicatorPipeline
from pocketbot.indicators.registry import IndicatorRegistry
from pocketbot.infrastructure.container.interfaces import (
    IServiceProvider,
)
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
    MarketRepository,
    MarketValidator,
)
from pocketbot.market.providers.default_provider import (
    DefaultMarketProvider,
)
from pocketbot.market.repositories.in_memory_market_repository import (
    InMemoryMarketRepository,
)
from pocketbot.market.services.market_connection_service import (
    MarketConnectionService,
)
from pocketbot.market.validators.default_market_validator import (
    DefaultMarketValidator,
)
from pocketbot.risk.engine import RiskEngine
from pocketbot.score.engine import ScoreEngine
from pocketbot.trading.engine import TradeEngine


def register_services(
    services: ServiceCollection,
) -> None:
    """
    Register application services.
    """

    indicator_registry = load_indicators()

    services.add_instance(
        IndicatorRegistry,
        indicator_registry,
    )

    services.add_singleton(
        ConfigService,
        factory=lambda _: ConfigService(
            Path("config"),
        ),
    )

    services.add_singleton(
        IndicatorFactory,
    )

    services.add_singleton(
        IndicatorEngine,
    )

    services.add_singleton(
        IndicatorManager,
    )

    services.add_singleton(
        IndicatorPipeline,
    )

    services.add_singleton(
        ConfluenceEngine,
    )

    services.add_singleton(
        ScoreEngine,
    )

    services.add_singleton(
        DecisionEngine,
    )

    services.add_singleton(
        RiskEngine,
    )

    services.add_singleton(
        ExecutionEngine,
    )

    services.add_singleton(
        TradeEngine,
    )

    # Market services

    services.add_singleton(
        MarketProvider,
        DefaultMarketProvider,
    )

    services.add_singleton(
        MarketCache,
        InMemoryMarketCache,
    )

    services.add_singleton(
        MarketRepository,
        InMemoryMarketRepository,
    )

    services.add_singleton(
        MarketValidator,
        DefaultMarketValidator,
    )

    services.add_singleton(
        MarketCollector,
        DefaultMarketCollector,
    )

    services.add_singleton(
        MarketService,
    )

    services.add_singleton(
        MarketQueryService,
    )

    services.add_singleton(
        MarketConnectionService,
    )

    services.add_singleton(
        HostedServiceManager,
        factory=lambda provider: HostedServiceManager(
            services=[
                provider.get_service(
                    MarketConnectionService,
                ),
            ],
        ),
    )

    services.add_singleton(
        Startup,
    )

    services.add_singleton(
        Shutdown,
    )

    services.add_singleton(
        LifecycleManager,
    )

    services.add_singleton(
        ApplicationService,
    )

    services.add_singleton(
        IServiceProvider,
        factory=lambda provider: provider,
    )

    services.add_singleton(
        ApplicationRuntime,
    )