from pocketbot.enterprise.intelligence.context.context_bridge import (
    ContextBridge,
)


def test_context_bridge_process():

    bridge = ContextBridge()

    result = bridge.process(
        decision_id="bridge-001",
        score=0.88,
        input_context={
            "asset": "XAUUSD",
            "timeframe": "M1",
        },
        feedback={
            "result": "success",
        },
    )

    assert result.decision_id == "bridge-001"
    assert result.score == 0.88


def test_context_bridge_recall():

    bridge = ContextBridge()

    bridge.process(
        decision_id="bridge-002",
        score=0.77,
    )

    result = bridge.recall(
        "bridge-002"
    )

    assert len(result) == 1


def test_context_bridge_history():

    bridge = ContextBridge()

    bridge.process(
        decision_id="bridge-003",
        score=0.66,
    )

    history = bridge.get_history()

    assert len(history) == 1
