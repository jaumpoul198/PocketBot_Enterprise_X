from pocketbot.enterprise.intelligence.context.context_runtime import (
    ContextRuntime,
)


def test_context_runtime_execute():

    runtime = ContextRuntime()

    result = runtime.execute_decision(
        decision_id="runtime-001",
        score=0.93,
        input_context={
            "asset": "XAUUSD",
        },
        feedback={
            "success": True,
        },
    )

    assert result["decision_id"] == "runtime-001"
    assert result["score"] == 0.93


def test_context_runtime_history():

    runtime = ContextRuntime()

    runtime.execute_decision(
        decision_id="runtime-002",
        score=0.85,
    )

    history = runtime.get_context_history()

    assert len(history) == 1


def test_context_runtime_recall():

    runtime = ContextRuntime()

    runtime.execute_decision(
        decision_id="runtime-003",
        score=0.75,
    )

    result = runtime.recall_decision(
        "runtime-003"
    )

    assert len(result) == 1
