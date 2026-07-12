
from pocketbot.events.event import Event
from pocketbot.infrastructure.audit.audit_registry import (
    AuditRegistry,
)
from pocketbot.infrastructure.metrics.metrics_registry import (
    MetricsRegistry,
)
from pocketbot.infrastructure.observability.runtime_observability_handler import (
    RuntimeObservabilityHandler,
)


def test_observability_handler_isolates_audit_metadata() -> None:
    metrics = MetricsRegistry()
    audit = AuditRegistry()

    handler = RuntimeObservabilityHandler(
        metrics,
        audit,
    )

    payload = {
        "service": "runtime",
        "state": "healthy",
    }

    event = Event(
        name="application.started",
        payload=payload,
    )

    handler.handle(event)

    payload["state"] = "broken"

    stored = audit.all()

    assert stored[0].metadata["state"] == "healthy"
