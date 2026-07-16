from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from datetime import datetime
from typing import Any


@dataclass(slots=True)
class Event:
    timestamp: datetime
    category: str
    name: str
    payload: dict[str, Any]


class IntelligenceEventBus:
    """
    Enterprise Intelligence Event Bus.
    """

    def __init__(self, limit: int = 1000) -> None:
        self._events: deque[Event] = deque(maxlen=limit)

    def publish(
        self,
        category: str,
        name: str,
        payload: dict[str, Any] | None = None,
    ) -> Event:
        event = Event(
            timestamp=datetime.now(),
            category=category,
            name=name,
            payload=payload or {},
        )

        self._events.append(event)

        return event

    def recent(self, limit: int = 20) -> list[Event]:
        return list(self._events)[-limit:]

    def all(self) -> list[Event]:
        return list(self._events)

    def clear(self) -> None:
        self._events.clear()

    def count(self) -> int:
        return len(self._events)

    def categories(self) -> list[str]:
        return sorted(
            {
                event.category
                for event in self._events
            }
        )
