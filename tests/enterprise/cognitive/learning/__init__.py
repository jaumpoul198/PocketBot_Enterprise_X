from pocketbot.enterprise.cognitive.learning.cognitive_learning import (
    CognitiveLearning
)


def test_learning_cycle():

    learning = CognitiveLearning()

    result = learning.learn(
        event="PERCEIVE",
        outcome="SUCCESS",
        score=1.0,
    )

    assert result.event == "PERCEIVE"
    assert learning.score() == 1.0
