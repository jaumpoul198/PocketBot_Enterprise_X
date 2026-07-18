from pocketbot.enterprise.cognitive.goals.goal_models import CognitiveGoal
from pocketbot.enterprise.cognitive.goals.goal_optimizer import GoalOptimizer
from pocketbot.enterprise.cognitive.goals.goal_priority import GoalPriorityEngine



def test_goal_priority_engine():

    engine = GoalPriorityEngine()

    result = engine.calculate(
        priority=8,
        urgency=0.9,
        impact=0.8,
    )

    assert result.score > 0.5



def test_goal_optimizer():

    optimizer = GoalOptimizer()

    goals = [
        CognitiveGoal(
            name="A",
            objective="Improve system",
            priority=8,
        ),
        CognitiveGoal(
            name="B",
            objective="Minor task",
            priority=2,
        ),
    ]


    result = optimizer.optimize(
        goals
    )


    assert len(result) == 2

    assert result[0]["goal"].name == "A"
