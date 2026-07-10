"""
PocketBot Enterprise X

Service Registration Bootstrap.
"""

from __future__ import annotations

from pathlib import Path

from pocketbot.application.hosting.hosted_service_manager import (
    HostedServiceManager,
)
from pocketbot.application.pipeline.service import (
    TradingPipelineService,
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
from pocketbot.application.flows.trading_flow import (
    TradingApplicationFlow,
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
from pocketbot.application.pipeline.service import (
    TradingPipelineService,
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
from pocketbot.market.strategy.breakout import (
    BreakoutStrategy,
)
from pocketbot.market.strategy.mean_reversion import (
    MeanReversionStrategy,
)
from pocketbot.market.strategy.momentum import (
    MomentumStrategy,
)
from pocketbot.market.strategy.selector.selector import (
    StrategySelectorEngine,
)

from pocketbot.market.strategy.selector.ranking import (
    StrategyRankingEngine,
)
from pocketbot.market.strategy.service import (
    StrategyService,
)
from pocketbot.market.validators.default_market_validator import (
    DefaultMarketValidator,
)
from pocketbot.risk.engine import RiskEngine
from pocketbot.score.engine import ScoreEngine
from pocketbot.trading.engine import TradeEngine
from pocketbot.trading.interfaces.trade_decision_repository import (
    TradeDecisionRepository,
)
from pocketbot.trading.repositories.in_memory_trade_decision_repository import (
    InMemoryTradeDecisionRepository,
)
from pocketbot.trading.services.trading_decision_recorder import (
    TradingDecisionRecorder,
)

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
        TradingPipelineService,
    )

    services.add_singleton(
        MarketConnectionService,
    )
    # Strategy services

    services.add_singleton(
        MomentumStrategy,
    )

    services.add_singleton(
        MeanReversionStrategy,
    )

    services.add_singleton(
        BreakoutStrategy,
    )

    services.add_singleton(
        StrategyRankingEngine,
    )

    services.add_singleton(
        StrategySelectorEngine,
        factory=lambda provider: StrategySelectorEngine(
            ranking_engine=provider.get_service(
                StrategyRankingEngine,
            ),
        ),
    )
    services.add_singleton(
        StrategyService,
        factory=lambda provider: StrategyService(
            strategies=[
                provider.get_service(
                    MomentumStrategy,
                ),
                provider.get_service(
                    MeanReversionStrategy,
                ),
                provider.get_service(
                    BreakoutStrategy,
                ),
            ],
            selector=provider.get_service(
                StrategySelectorEngine,
            ),
        ),
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
        ApplicationService,
    )

    services.add_singleton(
        TradingApplicationFlow,
        factory=lambda provider: TradingApplicationFlow(
            pipeline=provider.get_service(
                TradingPipelineService,
        ),
            recorder=provider.get_service(
                TradingDecisionRecorder,
            ),
        ),
    )
    services.add_singleton(
        TradeDecisionRepository,
        InMemoryTradeDecisionRepository,
    )

    services.add_singleton(
        TradingDecisionRecorder,
    )

    services.add_singleton(
        IServiceProvider,
        factory=lambda provider: provider,
    )

    services.add_singleton(
        ApplicationRuntime,
    )
