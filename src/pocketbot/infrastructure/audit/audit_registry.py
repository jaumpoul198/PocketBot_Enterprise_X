"""
PocketBot Enterprise X

Infrastructure Audit Registry.
"""

from __future__ import annotations

from copy import deepcopy

from pocketbot.infrastructure.audit.audit_event import (
    AuditEvent,
)


class AuditRegistry:
    """
    Registry for operational audit events.
    """

    def __init__(self) -> None:
        self._events: list[AuditEvent] = []

    def record(
        self,
        event: AuditEvent,
    ) -> None:
        """
        Record an audit event.

        The registry stores an isolated copy to prevent
        external mutation of internal state.
        """

        self._events.append(
            deepcopy(event),
        )

    def all(self) -> list[AuditEvent]:
        """
        Return all audit events.

        Returned events are isolated copies to prevent
        callers from mutating registry state.
        """

        return deepcopy(
            self._events,
        )

    def query(
        self,
        *,
        event_name: str | None = None,
        source: str | None = None,
    ) -> list[AuditEvent]:
        """
        Query audit events by filters.

        Returned events are isolated copies.
        """

        events = self._events

        if event_name is not None:
            events = [
                event
                for event in events
                if event.event_name == event_name
            ]

        if source is not None:
            events = [
                event
                for event in events
                if event.source == source
            ]

        return deepcopy(
            events,
        )
