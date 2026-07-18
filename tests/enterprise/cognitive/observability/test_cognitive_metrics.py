from pocketbot.enterprise.cognitive.observability.cognitive_metrics import (
    CognitiveMetrics,
)


def test_record_metric():
    metrics = CognitiveMetrics()

    metric = metrics.record(
        name="confidence",
        value=0.85,
        component="decision",
    )

    assert metric.name == "confidence"
    assert metric.value == 0.85
    assert metric.component == "decision"
    assert metrics.count() == 1


def test_get_all_metrics():
    metrics = CognitiveMetrics()

    metrics.record(
        name="latency",
        value=120,
        component="runtime",
    )

    result = metrics.get_all()

    assert len(result) == 1
    assert result[0].name == "latency"


def test_get_by_component():
    metrics = CognitiveMetrics()

    metrics.record(
        name="score",
        value=0.9,
        component="planner",
    )

    metrics.record(
        name="accuracy",
        value=0.8,
        component="decision",
    )

    result = metrics.get_by_component("planner")

    assert len(result) == 1
    assert result[0].component == "planner"


def test_latest_metric():
    metrics = CognitiveMetrics()

    metrics.record(
        name="confidence",
        value=0.5,
        component="decision",
    )

    metrics.record(
        name="confidence",
        value=0.9,
        component="decision",
    )

    latest = metrics.latest("confidence")

    assert latest.value == 0.9
