from pocketbot.enterprise.cognitive.runtime.cognitive_runtime import (
    CognitiveRuntime,
)


def test_runtime_generates_final_decision():

    runtime = CognitiveRuntime()

    decision = runtime.execute()

    status = runtime.status()

    assert decision.action == "PERCEIVE"

    assert status["last_final_decision"] is not None

    assert (
        status["last_final_decision"].action
        == "PERCEIVE"
    )
