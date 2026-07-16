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
