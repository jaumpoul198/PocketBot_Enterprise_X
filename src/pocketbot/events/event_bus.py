from __future__ import annotations

from collections import defaultdict
from copy import deepcopy

from pocketbot.core.logger import get_logger

from .event import Event
from .exceptions import EventHandlingError
from .handlers import EventHandler


logger = get_logger(__name__)


class EventBus:
    """
    Barramento central de eventos.
    """

    def __init__(self) -> None:
        self._handlers: dict[str, list[EventHandler]] = defaultdict(list)
        self._global_handlers: list[EventHandler] = []

    def subscribe(
        self,
        event_name: str,
        handler: EventHandler,
    ) -> None:
        self._handlers[event_name].append(handler)

    def add_global_handler(
        self,
        handler: EventHandler,
    ) -> None:
        """
        Register a handler that receives all events.
        """
        self._global_handlers.append(handler)

    def handlers(
        self,
    ) -> dict[str, list[EventHandler]]:
        return deepcopy(self._handlers)

    def global_handlers(
        self,
    ) -> list[EventHandler]:
        return deepcopy(self._global_handlers)

    def publish(
        self,
        event: Event,
    ) -> None:
        handlers = self._handlers.get(event.name, [])

        for handler in [
            *handlers,
            *self._global_handlers,
        ]:
            try:
                handler.handle(
                    deepcopy(event),
                )

            except Exception as exc:
                logger.exception(
                    "Event handler failed | event=%s handler=%s",
                    event.name,
                    handler.__class__.__name__,
                )

                raise EventHandlingError(
                    f"Failed handling event '{event.name}'"
                ) from exc
