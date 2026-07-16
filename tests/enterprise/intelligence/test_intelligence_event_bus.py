from pocketbot.enterprise.intelligence.observability.intelligence_event_bus import (
    IntelligenceEventBus,
)


def test_publish_event() -> None:
    bus = IntelligenceEventBus()

    event = bus.publish(
        category="runtime",
        name="startup",
    )

    assert event.category == "runtime"
    assert event.name == "startup"
    assert bus.count() == 1


def test_recent_events() -> None:
    bus = IntelligenceEventBus()

    for i in range(5):
        bus.publish(
            category="test",
            name=f"event_{i}",
        )

    recent = bus.recent(2)

    assert len(recent) == 2
    assert recent[-1].name == "event_4"


def test_clear_events() -> None:
    bus = IntelligenceEventBus()

    bus.publish(
        category="runtime",
        name="start",
    )

    bus.clear()

    assert bus.count() == 0


def test_categories() -> None:
    bus = IntelligenceEventBus()

    bus.publish("runtime", "a")
    bus.publish("context", "b")
    bus.publish("runtime", "c")

    assert sorted(bus.categories()) == [
        "context",
        "runtime",
    ]
