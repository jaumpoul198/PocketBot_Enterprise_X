from pocketbot.enterprise.cognitive.goals import CognitiveGoalManager


def test_goal_manager_runtime_isolation():

    manager_one = CognitiveGoalManager()
    manager_two = CognitiveGoalManager()

    goal = manager_one.create_goal(
        name="autonomous_learning",
        objective="Improve learning cycle",
    )

    assert len(manager_one.goals) == 1
    assert len(manager_two.goals) == 0
    assert goal in manager_one.goals
