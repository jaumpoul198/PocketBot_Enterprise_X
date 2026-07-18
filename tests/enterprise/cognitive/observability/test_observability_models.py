from datetime import datetime, timezone

from pocketbot.enterprise.cognitive.observability.observability_models import (
    CognitiveMetric,
    CognitiveEvent,
    CognitiveTrace,
)


def test_cognitive_metric_creation():
    metric = CognitiveMetric(
        name="accuracy",
        value=0.95,
        component="decision",
    )

    assert metric.name == "accuracy"
    assert metric.value == 0.95
    assert metric.component == "decision"
    assert isinstance(metric.timestamp, datetime)
    assert metric.timestamp.tzinfo == timezone.utc


def test_cognitive_event_creation():
    event = CognitiveEvent(
        event_type="decision_created",
        source="runtime",
    )

    assert event.event_type == "decision_created"
    assert event.source == "runtime"
    assert event.event_id is not None


def test_cognitive_trace_steps_and_finish():
    trace = CognitiveTrace(
        operation="planning_cycle",
    )

    trace.add_step("analyze")
    trace.add_step("plan")

    assert trace.steps == [
        "analyze",
        "plan",
    ]

    assert trace.finished_at is None

    trace.finish()

    assert trace.finished_at is not None
