from pocketbot.enterprise.cognitive.evolution.cognitive_evolution import (
    CognitiveEvolution,
)


def test_cognitive_evolution():

    evolution = CognitiveEvolution()

    metric = evolution.evaluate(
        memory_count=10,
        learning_score=0.9,
    )

    assert metric.score > 0
    assert metric.maturity == "ADVANCED"
    assert evolution.latest() == metric
