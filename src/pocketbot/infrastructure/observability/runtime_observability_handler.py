"""
PocketBot Enterprise X

Runtime Observability Handler.
"""

from __future__ import annotations

from pocketbot.core.logger import get_logger
from pocketbot.events.event import Event
from pocketbot.events.handlers import EventHandler
from pocketbot.infrastructure.audit import (
    AuditEvent,
    AuditRegistry,
)
from pocketbot.infrastructure.audit.audit_event import (
    AuditSeverity,
)
from pocketbot.infrastructure.metrics import (
    MetricsRegistry,
)


logger = get_logger(__name__)


class RuntimeObservabilityHandler(EventHandler):
    """
    Handles runtime events for infrastructure observability.
    """

    def __init__(
        self,
        metrics: MetricsRegistry,
        audit: AuditRegistry,
    ) -> None:
        self._metrics = metrics
        self._audit = audit

    def handle(
        self,
        event: Event,
    ) -> None:
        """
        Processes runtime lifecycle events.
        """

        self._metrics.increment(
            event.name,
        )

        severity = AuditSeverity.INFO

        if event.name == "application.startup.failed":
            severity = AuditSeverity.ERROR

        logger.info(
            "Runtime event received | event=%s payload=%s",
            event.name,
            event.payload,
        )

        if severity == AuditSeverity.ERROR:
            logger.error(
                "Runtime startup failed | payload=%s",
                event.payload,
            )

        self._audit.record(
            AuditEvent(
                event_name=event.name,
                source="runtime",
                severity=severity,
                metadata=event.payload,
            )
        )
