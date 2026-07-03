from __future__ import annotations

from collections import defaultdict

from .event import Event
from .handlers import EventHandler


class EventBus:
    """
    Barramento de eventos.
    """

    def __init__(self) -> None:
        self._handlers: dict[str, list[EventHandler]] = defaultdict(list)

    def subscribe(
        self,
        event_name: str,
        handler: EventHandler,
    ) -> None:
        self._handlers[event_name].append(handler)

    def publish(self, event: Event) -> None:
        handlers = self._handlers.get(event.name, [])

        for handler in handlers:
            handler.handle(event)
