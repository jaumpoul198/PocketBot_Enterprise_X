from pocketbot.enterprise.cognitive.goals import (
    CognitiveGoalManager,
    GoalStatus,
)


def test_create_cognitive_goal():

    manager = CognitiveGoalManager()

    goal = manager.create_goal(
        name="optimize_strategy",
        objective="Improve autonomous decision quality",
        priority=5,
    )

    assert goal.name == "optimize_strategy"
    assert goal.objective == "Improve autonomous decision quality"
    assert goal.priority == 5
    assert goal.status == GoalStatus.CREATED


def test_activate_cognitive_goal():

    manager = CognitiveGoalManager()

    goal = manager.create_goal(
        name="market_analysis",
        objective="Analyze market context",
    )

    goal.activate()

    assert goal.status == GoalStatus.ACTIVE


def test_complete_cognitive_goal():

    manager = CognitiveGoalManager()

    goal = manager.create_goal(
        name="execution_cycle",
        objective="Execute cognitive cycle",
    )

    manager.complete_goal(goal)

    assert goal.status == GoalStatus.COMPLETED
    assert goal.completed_at is not None
