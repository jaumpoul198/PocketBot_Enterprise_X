from __future__ import annotations

from pocketbot.infrastructure.audit.audit_event import (
    AuditEvent,
)


def test_audit_event_metadata_isolated_from_input() -> None:
    metadata = {
        "service": {
            "status": "healthy",
        },
    }

    event = AuditEvent(
        event_name="startup",
        source="runtime",
        metadata=metadata,
    )

    metadata["service"]["status"] = "broken"

    assert event.metadata["service"]["status"] == "healthy"


def test_audit_event_metadata_mutation_does_not_affect_source() -> None:
    metadata = {
        "attempt": 1,
    }

    event = AuditEvent(
        event_name="failure",
        source="runtime",
        metadata=metadata,
    )

    event.metadata["attempt"] = 99

    assert metadata["attempt"] == 1
