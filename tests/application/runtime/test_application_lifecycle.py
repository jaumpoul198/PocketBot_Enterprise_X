"""
PocketBot Enterprise X

Application lifecycle integration tests.
"""

from __future__ import annotations

from pocketbot.application.runtime.application_runtime import (
    ApplicationRuntime,
)
from pocketbot.bootstrap import build_application
from pocketbot.market.interfaces import MarketProvider


def test_application_runtime_lifecycle() -> None:
    """
    Validates complete application startup and shutdown lifecycle.
    """

    provider = build_application()

    runtime = provider.get_service(
        ApplicationRuntime,
    )

    market = provider.get_service(
        MarketProvider,
    )

    assert not market.is_connected()

    runtime.start()

    assert runtime.is_running
    assert market.is_connected()

    runtime.stop()

    assert not runtime.is_running
    assert not market.is_connected()

from pocketbot.application.orchestrator.trading_orchestrator import (
    TradingOrchestrator,
)


def test_application_runtime_resolves_trading_orchestrator() -> None:
    """
    Validates trading orchestrator availability during application runtime.
    """

    provider = build_application()

    runtime = provider.get_service(
        ApplicationRuntime,
    )

    assert runtime is not None

    orchestrator = provider.get_service(
        TradingOrchestrator,
    )

    assert orchestrator is not None
