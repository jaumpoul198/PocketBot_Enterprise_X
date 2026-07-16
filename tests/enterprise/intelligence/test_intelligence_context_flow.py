from pocketbot.enterprise.intelligence.context.context_runtime import (
    ContextRuntime,
)

from pocketbot.enterprise.intelligence.context.context_metrics import (
    ContextMetrics,
)


def test_full_intelligence_context_flow():

    runtime = ContextRuntime()

    metrics = ContextMetrics()


    result = runtime.execute_decision(
        decision_id="full-flow-001",
        score=0.95,
        input_context={
            "asset": "XAUUSD",
            "timeframe": "M1",
            "strategy": "adaptive",
        },
        feedback={
            "success": True,
        },
    )


    metrics.record(
        score=result["score"],
        feedback={
            "success": True,
        },
    )


    assert result["decision_id"] == "full-flow-001"

    assert result["score"] == 0.95

    assert runtime.get_context_count() == 1

    assert metrics.total_decisions == 1

    assert metrics.success_rate() == 1
