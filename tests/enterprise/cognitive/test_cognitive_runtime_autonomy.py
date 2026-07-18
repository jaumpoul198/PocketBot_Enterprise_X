from pocketbot.enterprise.cognitive.runtime import CognitiveRuntime


def test_runtime_autonomy_integration():

    runtime = CognitiveRuntime()

    runtime.execute()

    status = runtime.status()

    assert status["last_autonomy_result"] is not None
    assert status["last_feedback"] is not None


def test_runtime_feedback():

    runtime = CognitiveRuntime()

    runtime.execute()

    feedback = runtime.status()["last_feedback"]

    assert "reward" in feedback
    assert "success" in feedback
