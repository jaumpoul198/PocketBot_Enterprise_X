from __future__ import annotations

from pocketbot.events.event import Event
from pocketbot.infrastructure.audit import (
    AuditRegistry,
)
from pocketbot.infrastructure.metrics import (
    MetricsRegistry,
)
from pocketbot.infrastructure.observability.runtime_observability_handler import (
    RuntimeObservabilityHandler,
)


class FailingAuditRegistry(AuditRegistry):
    def record(self, event) -> None:
        raise RuntimeError("audit failure")


def test_runtime_observability_records_metrics_and_audit() -> None:
    metrics = MetricsRegistry()
    audit = AuditRegistry()

    handler = RuntimeObservabilityHandler(
        metrics=metrics,
        audit=audit,
    )

    handler.handle(
        Event(
            name="application.started",
            payload={},
        )
    )

    metric = metrics.get(
        "application.started",
    )

    assert metric is not None
    assert metric.value == 1

    events = audit.query(
        event_name="application.started",
    )

    assert len(events) == 1
    assert events[0].source == "runtime"


def test_runtime_observability_marks_startup_failure_as_error() -> None:
    metrics = MetricsRegistry()
    audit = AuditRegistry()

    handler = RuntimeObservabilityHandler(
        metrics=metrics,
        audit=audit,
    )

    handler.handle(
        Event(
            name="application.startup.failed",
            payload={
                "error": "failure",
            },
        )
    )

    events = audit.query(
        event_name="application.startup.failed",
    )

    assert len(events) == 1
    assert events[0].severity.value == "error"


def test_runtime_observability_ignores_audit_failure() -> None:
    metrics = MetricsRegistry()
    audit = FailingAuditRegistry()

    handler = RuntimeObservabilityHandler(
        metrics=metrics,
        audit=audit,
    )

    handler.handle(
        Event(
            name="application.started",
            payload={},
        )
    )

    metric = metrics.get(
        "application.started",
    )

    assert metric is not None
    assert metric.value == 1
