"""
PocketBot Enterprise X

Trading orchestrator container tests.
"""

from __future__ import annotations

from pocketbot.application.flows.trading_flow import (
    TradingApplicationFlow,
)
from pocketbot.application.orchestrator.trading_orchestrator import (
    TradingOrchestrator,
)
from pocketbot.bootstrap.service_registration import (
    register_services,
)
from pocketbot.infrastructure.container.service_collection import (
    ServiceCollection,
)


def test_container_resolves_trading_orchestrator() -> None:

    services = ServiceCollection()

    register_services(
        services,
    )

    provider = services.build_provider()

    orchestrator = provider.get_service(
        TradingOrchestrator,
    )

    flow = provider.get_service(
        TradingApplicationFlow,
    )

    assert orchestrator is not None
    assert flow is not None
