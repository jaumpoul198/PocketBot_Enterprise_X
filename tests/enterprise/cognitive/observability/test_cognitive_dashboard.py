from pocketbot.enterprise.cognitive.observability.cognitive_monitor import (
    CognitiveMonitor,
)

from pocketbot.enterprise.cognitive.observability.cognitive_dashboard import (
    CognitiveDashboard,
)


def test_dashboard_summary():
    monitor = CognitiveMonitor()

    dashboard = CognitiveDashboard(
        monitor,
    )

    monitor.record_metric(
        name="score",
        value=0.8,
        component="planner",
    )

    summary = dashboard.summary()

    assert summary["metrics"] == 1


def test_dashboard_metrics_events_traces():
    monitor = CognitiveMonitor()

    dashboard = CognitiveDashboard(
        monitor,
    )

    monitor.record_metric(
        name="accuracy",
        value=0.9,
        component="decision",
    )

    monitor.emit_event(
        event_type="decision",
        source="runtime",
    )

    monitor.start_trace(
        operation="cycle",
    )

    assert len(dashboard.metrics()) == 1
    assert len(dashboard.events()) == 1
    assert len(dashboard.traces()) == 1
