from __future__ import annotations

from .event import Event
from .event_bus import EventBus


class EventPublisher:
    """
    Publicador de eventos.
    """

    def __init__(self, event_bus: EventBus) -> None:
        self._event_bus = event_bus

    def publish(
        self,
        name: str,
        payload: dict,
    ) -> None:
        self._event_bus.publish(
            Event(
                name=name,
                payload=payload,
            )
        )
