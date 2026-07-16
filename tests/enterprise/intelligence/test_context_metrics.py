from pocketbot.enterprise.intelligence.context.context_metrics import (
    ContextMetrics,
)


def test_context_metrics_record():

    metrics = ContextMetrics()

    metrics.record(
        score=0.90,
        feedback={
            "success": True
        },
    )

    assert metrics.total_decisions == 1
    assert metrics.successful_feedbacks == 1


def test_context_metrics_average():

    metrics = ContextMetrics()

    metrics.record(score=0.80)
    metrics.record(score=1.00)

    assert metrics.average_score() == 0.90


def test_context_metrics_snapshot():

    metrics = ContextMetrics()

    metrics.record(
        score=0.75,
        feedback={
            "success": True
        },
    )

    result = metrics.snapshot()

    assert result["total_decisions"] == 1
    assert result["success_rate"] == 1
