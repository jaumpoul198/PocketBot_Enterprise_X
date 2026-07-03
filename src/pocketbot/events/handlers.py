from __future__ import annotations

from abc import ABC, abstractmethod

from .event import Event


class EventHandler(ABC):
    """
    Interface para handlers de eventos.
    """

    @abstractmethod
    def handle(self, event: Event) -> None: ...
