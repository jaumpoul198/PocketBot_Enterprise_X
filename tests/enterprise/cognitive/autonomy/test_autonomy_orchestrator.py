from pocketbot.enterprise.cognitive.autonomy import (
    CognitiveAutonomyOrchestrator,
)


def test_orchestrator_execution():

    orchestrator = CognitiveAutonomyOrchestrator()

    result = orchestrator.execute(
        {
            "type": "adapt_strategy"
        },
        0.9,
    )

    assert result["execution"]["approved"] is True
    assert result["feedback"]["reward"] == 0.9


def test_orchestrator_status():

    orchestrator = CognitiveAutonomyOrchestrator()

    orchestrator.execute(
        {
            "type": "learn"
        },
        0.8,
    )

    status = orchestrator.status()

    assert status["feedback"] == 1
    assert status["evolution_events"] == 1
