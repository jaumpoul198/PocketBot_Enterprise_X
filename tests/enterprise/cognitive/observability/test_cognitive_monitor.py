from pocketbot.enterprise.cognitive.observability.cognitive_monitor import (
    CognitiveMonitor,
)


def test_monitor_record_metric():
    monitor = CognitiveMonitor()

    metric = monitor.record_metric(
        name="confidence",
        value=0.95,
        component="decision",
    )

    assert metric.name == "confidence"
    assert monitor.snapshot()["metrics"] == 1


def test_monitor_emit_event():
    monitor = CognitiveMonitor()

    event = monitor.emit_event(
        event_type="cycle_started",
        source="runtime",
    )

    assert event.event_type == "cycle_started"
    assert monitor.snapshot()["events"] == 1


def test_monitor_trace_flow():
    monitor = CognitiveMonitor()

    trace = monitor.start_trace(
        operation="planning",
    )

    monitor.add_trace_step(
        trace,
        "analyze",
    )

    monitor.finish_trace(trace)

    snapshot = monitor.snapshot()

    assert snapshot["traces"] == 1
    assert trace.finished_at is not None
