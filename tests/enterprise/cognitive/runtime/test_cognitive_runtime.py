from pocketbot.enterprise.cognitive.runtime.cognitive_runtime import (
    CognitiveRuntime,
)


def test_runtime_execution():

    runtime = CognitiveRuntime()

    decision = runtime.execute()

    assert decision.action == "PERCEIVE"


def test_runtime_status():

    runtime = CognitiveRuntime()

    runtime.execute()

    status = runtime.status()

    assert "started_at" in status
    assert "last_decision" in status
    assert "engine" in status
