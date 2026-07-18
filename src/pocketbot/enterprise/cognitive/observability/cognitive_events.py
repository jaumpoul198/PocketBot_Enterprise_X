"""
PocketBot Enterprise X
Cognitive Events Manager

Responsible for recording cognitive
system events and lifecycle signals.
"""

from typing import Any, Dict, List, Optional

from .observability_models import CognitiveEvent


class CognitiveEvents:
    """
    Stores cognitive events generated
    during execution.
    """

    def __init__(self):
        self._events: List[CognitiveEvent] = []

    def emit(
        self,
        event_type: str,
        source: str,
        payload: Optional[Dict[str, Any]] = None,
    ) -> CognitiveEvent:
        """
        Create and store a cognitive event.
        """

        event = CognitiveEvent(
            event_type=event_type,
            source=source,
            payload=payload or {},
        )

        self._events.append(event)

        return event

    def get_all(self) -> List[CognitiveEvent]:
        """
        Return all events.
        """

        return list(self._events)

    def get_by_type(
        self,
        event_type: str,
    ) -> List[CognitiveEvent]:
        """
        Filter events by type.
        """

        return [
            event
            for event in self._events
            if event.event_type == event_type
        ]

    def latest(
        self,
        event_type: str,
    ) -> Optional[CognitiveEvent]:
        """
        Return latest event of a type.
        """

        for event in reversed(self._events):
            if event.event_type == event_type:
                return event

        return None

    def count(self) -> int:
        """
        Return total events stored.
        """

        return len(self._events)
