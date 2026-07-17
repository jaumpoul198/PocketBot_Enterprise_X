from datetime import datetime, timezone

from pocketbot.enterprise.intelligence.feedback.feedback_models import (
    DecisionFeedback,
)

from pocketbot.enterprise.intelligence.feedback import (
    FeedbackEngine,
)


def test_feedback_success():

    engine = FeedbackEngine()

    feedback = engine.evaluate(
        decision="buy",
        expected_score=80,
        actual_score=85,
        success=True,
    )

    assert feedback.success is True
    assert feedback.accuracy > 0


def test_feedback_learning_signal():

    engine = FeedbackEngine()

    feedback = engine.evaluate(
        decision="sell",
        expected_score=70,
        actual_score=40,
        success=False,
    )

    signal = engine.learning_signal(
        feedback
    )

    assert signal >= 0
    assert engine.count() == 1

def test_feedback_to_dict():

    feedback = DecisionFeedback(
        decision="buy",
        expected_score=90,
        actual_score=95,
        success=True,
        timestamp=datetime.now(timezone.utc),
    )

    data = feedback.to_dict()

    assert data["decision"] == "buy"
    assert data["accuracy"] > 0


def test_feedback_from_mapping():

    feedback = DecisionFeedback.from_mapping(
        {
            "decision": "sell",
            "expected_score": 70,
            "actual_score": 65,
            "success": False,
        }
    )

    assert feedback.decision == "sell"
    assert feedback.success is False
