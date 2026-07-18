from pocketbot.enterprise.cognitive.observability.cognitive_events import (
    CognitiveEvents,
)


def test_emit_event():
    events = CognitiveEvents()

    event = events.emit(
        event_type="cycle_started",
        source="runtime",
    )

    assert event.event_type == "cycle_started"
    assert event.source == "runtime"
    assert events.count() == 1


def test_get_all_events():
    events = CognitiveEvents()

    events.emit(
        event_type="decision",
        source="planner",
    )

    result = events.get_all()

    assert len(result) == 1
    assert result[0].event_type == "decision"


def test_get_by_type():
    events = CognitiveEvents()

    events.emit(
        event_type="success",
        source="runtime",
    )

    events.emit(
        event_type="failure",
        source="runtime",
    )

    result = events.get_by_type("success")

    assert len(result) == 1
    assert result[0].event_type == "success"


def test_latest_event():
    events = CognitiveEvents()

    events.emit(
        event_type="update",
        source="memory",
    )

    events.emit(
        event_type="update",
        source="learning",
    )

    latest = events.latest("update")

    assert latest.source == "learning"
