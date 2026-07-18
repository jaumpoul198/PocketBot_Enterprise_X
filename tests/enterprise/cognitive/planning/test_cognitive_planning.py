from pocketbot.enterprise.cognitive.planning import (
    CognitivePlanning,
)


def test_planning():

    planning = CognitivePlanning()

    result = planning.plan(
        learning_score=0.8,
        evolution_score=0.6,
    )

    assert result.objective == "continuous_improvement"
    assert result.strategy == "OPTIMIZE"


def test_planning_status():

    planning = CognitivePlanning()

    planning.plan(
        learning_score=1.0,
        evolution_score=1.0,
    )

    status = planning.status()

    assert status["plans"] == 1
    assert status["latest"] is not None
