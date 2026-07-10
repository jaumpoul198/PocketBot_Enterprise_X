"""
PocketBot Enterprise X

Trading session manager container tests.
"""

from __future__ import annotations

from pocketbot.application.orchestrator.trading_orchestrator import (
    TradingOrchestrator,
)
from pocketbot.application.session.trading_session_manager import (
    TradingSessionManager,
)
from pocketbot.bootstrap.service_registration import (
    register_services,
)
from pocketbot.infrastructure.container.service_collection import (
    ServiceCollection,
)


def test_container_resolves_trading_session_manager() -> None:
    services = ServiceCollection()

    register_services(
        services,
    )

    provider = services.build_provider()

    session_manager = provider.get_service(
        TradingSessionManager,
    )

    orchestrator = provider.get_service(
        TradingOrchestrator,
    )

    assert session_manager is not None
    assert orchestrator is not None
