from __future__ import annotations

from pocketbot.events.event import Event
from pocketbot.events.event_bus import EventBus
from pocketbot.events.handlers import EventHandler


class DummyHandler(EventHandler):
    def handle(self, event: Event) -> None:
        pass


def test_handlers_snapshot_isolated_from_bus_state() -> None:
    bus = EventBus()

    handler = DummyHandler()

    bus.subscribe(
        "test",
        handler,
    )

    snapshot = bus.handlers()

    snapshot["test"].clear()

    assert len(bus.handlers()["test"]) == 1


def test_global_handlers_snapshot_isolated_from_bus_state() -> None:
    bus = EventBus()

    handler = DummyHandler()

    bus.add_global_handler(
        handler,
    )

    snapshot = bus.global_handlers()

    snapshot.clear()

    assert len(bus.global_handlers()) == 1
