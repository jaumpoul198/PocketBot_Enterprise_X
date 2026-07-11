"""
PocketBot Enterprise X

Runtime Observability Handler.
"""

from __future__ import annotations

from collections.abc import Callable

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

    def _safe_execute(
        self,
        operation: Callable[[], None],
        operation_name: str,
    ) -> None:
        """
        Executes observability operations without affecting runtime flow.
        """

        try:
            operation()

        except Exception:
            logger.exception(
                "Observability operation failed | operation=%s",
                operation_name,
            )

    def handle(
        self,
        event: Event,
    ) -> None:
        """
        Processes runtime lifecycle events.
        """

        severity = AuditSeverity.INFO

        if event.name == "application.startup.failed":
            severity = AuditSeverity.ERROR

        self._safe_execute(
            lambda: self._metrics.increment(
                event.name,
            ),
            "metrics",
        )

        self._safe_execute(
            lambda: logger.info(
                "Runtime event received | event=%s payload=%s",
                event.name,
                event.payload,
            ),
            "logging",
        )

        if severity == AuditSeverity.ERROR:
            self._safe_execute(
                lambda: logger.error(
                    "Runtime startup failed | payload=%s",
                    event.payload,
                ),
                "error_logging",
            )

        self._safe_execute(
            lambda: self._audit.record(
                AuditEvent(
                    event_name=event.name,
                    source="runtime",
                    severity=severity,
                    metadata=event.payload,
                )
            ),
            "audit",
        )