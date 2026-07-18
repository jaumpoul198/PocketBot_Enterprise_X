from pocketbot.enterprise.cognitive.runtime.cognitive_runtime import (
    CognitiveRuntime,
)


def test_cognitive_runtime_stores_memory():

    runtime = CognitiveRuntime()

    decision = runtime.execute()

    status = runtime.status()

    assert decision.action == "PERCEIVE"

    assert status["last_memory_entry"] is not None

    assert len(status["memory"]) == 1

    assert status["memory"][0].action == decision.action
