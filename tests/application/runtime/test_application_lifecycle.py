"""
PocketBot Enterprise X

Application lifecycle integration tests.
"""

from __future__ import annotations

from pocketbot.application.runtime.application_runtime import (
    ApplicationRuntime,
)
from pocketbot.bootstrap import build_application
from pocketbot.events.event import Event
from pocketbot.events.event_bus import EventBus
from pocketbot.infrastructure.audit import AuditRegistry
from pocketbot.infrastructure.metrics import MetricsRegistry
from pocketbot.infrastructure.observability import (
    RuntimeObservabilityHandler,
)
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


def test_application_registers_runtime_observability_handler() -> None:
    """
    Validates runtime observability integration through application bootstrap.
    """

    provider = build_application()

    event_bus = provider.get_service(
        EventBus,
    )

    handler = provider.get_service(
        RuntimeObservabilityHandler,
    )

    metrics = provider.get_service(
        MetricsRegistry,
    )

    audit = provider.get_service(
        AuditRegistry,
    )

    assert event_bus is not None
    assert handler is not None

    event_name = "application.test.event"

    event_bus.publish(
        Event(
            name=event_name,
            payload={
                "source": "integration-test",
            },
        )
    )

    metric = metrics.get(
        event_name,
    )

    assert metric is not None
    assert metric.value == 1

    events = audit.query(
        event_name=event_name,
        source="runtime",
    )

    assert len(events) == 1