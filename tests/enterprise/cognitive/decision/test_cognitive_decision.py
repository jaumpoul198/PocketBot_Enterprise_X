from pocketbot.enterprise.cognitive.decision.cognitive_decision import (
    CognitiveDecision,
)


def test_cognitive_decision_generation():

    decision_engine = CognitiveDecision()

    result = decision_engine.decide(
        cognitive_state="PERCEIVE",
        memory_score=1.0,
        learning_score=1.0,
    )

    assert result.action == "PERCEIVE"
    assert result.confidence == 1.0


def test_cognitive_decision_status():

    decision_engine = CognitiveDecision()

    decision_engine.decide(
        cognitive_state="ACT",
        memory_score=0.8,
        learning_score=0.9,
    )

    status = decision_engine.status()

    assert status["last_decision"] is not None
