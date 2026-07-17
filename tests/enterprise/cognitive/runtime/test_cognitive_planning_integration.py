from pocketbot.enterprise.cognitive.runtime import CognitiveRuntime


def test_runtime_planning_integration():

    runtime = CognitiveRuntime()

    runtime.execute()

    status = runtime.status()

    assert status["last_plan"] is not None
    assert status["planning"]["plans"] == 1
