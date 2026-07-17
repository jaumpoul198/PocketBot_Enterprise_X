from pocketbot.enterprise.cognitive.autonomy import AutonomyFeedback


def test_register_feedback():

    feedback = AutonomyFeedback()

    result = feedback.register_feedback(
        {
            "action": "optimize"
        },
        True,
        1.0
    )

    assert result["success"] is True
    assert result["reward"] == 1.0


def test_success_rate():

    feedback = AutonomyFeedback()

    feedback.register_feedback(
        {
            "action": "a"
        },
        True,
        1
    )

    feedback.register_feedback(
        {
            "action": "b"
        },
        False,
        0
    )

    assert feedback.success_rate() == 0.5


def test_feedback_history():

    feedback = AutonomyFeedback()

    feedback.register_feedback(
        {
            "action": "learn"
        },
        True,
        1
    )

    assert len(
        feedback.get_history()
    ) == 1
