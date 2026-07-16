from pocketbot.enterprise.intelligence.learning import (
    LearningEngine,
)


def test_learning_record():

    engine = LearningEngine()

    record = engine.learn(
        decision="increase_confidence",
        score_before=50,
        score_after=70,
        feedback=1.0,
    )

    assert record.improvement == 20


def test_learning_state():

    engine = LearningEngine()

    engine.learn(
        decision="optimize",
        score_before=40,
        score_after=60,
        feedback=1.0,
    )

    state = engine.state()

    assert state.total_records == 1
    assert state.adaptation_level > 0
