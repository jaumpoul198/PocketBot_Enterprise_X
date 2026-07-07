"""
PocketBot Enterprise X

Service Registration Bootstrap.
"""

from __future__ import annotations

from pocketbot.application.runtime.application_runtime import (
    ApplicationRuntime,
)

from pocketbot.application.services.application_service import (
    ApplicationService,
)

from pocketbot.application.runtime.application_runtime import (
    ApplicationRuntime,
)
from pocketbot.infrastructure.container.interfaces import (
    IServiceProvider,
)

from pocketbot.application.lifecycle.lifecycle_manager import (
    LifecycleManager,
)
from pocketbot.application.lifecycle.shutdown import (
    Shutdown,
)
from pocketbot.application.lifecycle.startup import (
    Startup,
)

from pocketbot.bootstrap.indicator_loader import load_indicators
from pocketbot.confluence.engine import ConfluenceEngine
from pocketbot.decision.engine import DecisionEngine
from pocketbot.execution.engine import ExecutionEngine
from pocketbot.indicators.engine import IndicatorEngine
from pocketbot.indicators.factory import IndicatorFactory
from pocketbot.indicators.manager import IndicatorManager
from pocketbot.indicators.pipeline import IndicatorPipeline
from pocketbot.indicators.registry import IndicatorRegistry
from pocketbot.infrastructure.container.service_collection import (
    ServiceCollection,
)
from pocketbot.market.interfaces import MarketProvider
from pocketbot.market.providers.default_provider import (
    DefaultMarketProvider,
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

    services.add_singleton(
        MarketProvider,
        DefaultMarketProvider,
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