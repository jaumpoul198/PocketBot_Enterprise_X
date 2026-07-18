from pocketbot.enterprise.cognitive.runtime import CognitiveRuntime


def test_runtime_has_cognitive_goal_manager():

    runtime = CognitiveRuntime()

    assert runtime.goals is not None


def test_runtime_goal_creation():

    runtime = CognitiveRuntime()

    goal = runtime.goals.create_goal(
        name="autonomous_cycle",
        objective="Execute cognitive autonomous cycle",
    )

    runtime.last_goal = goal

    assert runtime.last_goal == goal
