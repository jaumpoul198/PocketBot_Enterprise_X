from __future__ import annotations

from pocketbot.infrastructure.audit.audit_event import (
    AuditEvent,
    AuditSeverity,
)
from pocketbot.infrastructure.audit.audit_registry import (
    AuditRegistry,
)


def create_event() -> AuditEvent:
    return AuditEvent(
        event_name="trade.executed",
        source="engine",
        severity=AuditSeverity.INFO,
        metadata={
            "asset": "BTC",
            "price": 100,
        },
    )


def test_query_results_are_isolated_from_registry_state() -> None:
    registry = AuditRegistry()

    registry.record(create_event())

    events = registry.query(
        event_name="trade.executed",
    )

    events[0].metadata["price"] = 999

    stored = registry.query(
        event_name="trade.executed",
    )

    assert stored[0].metadata["price"] == 100
