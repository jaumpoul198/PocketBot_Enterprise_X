from pocketbot.enterprise.cognitive.runtime.cognitive_runtime import (
    CognitiveRuntime,
)


def test_cognitive_runtime_integrates_with_intelligence():

    runtime = CognitiveRuntime()

    decision = runtime.execute(
        health_score=0.95
    )

    status = runtime.status()

    assert decision.action == "PERCEIVE"

    assert status["last_decision"] is not None

    assert status["last_intelligence_decision"] is not None

    assert "intelligence" in status
