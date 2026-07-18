from pocketbot.enterprise.cognitive.goals.runtime.goal_feedback import (
    GoalFeedback,
)


def test_goal_feedback_record():

    feedback = GoalFeedback()

    result = feedback.record(
        goal="test_goal",
        result="completed",
        score=1.0,
    )

    assert result["result"] == "completed"
    assert result["score"] == 1.0

    assert feedback.latest() == result
