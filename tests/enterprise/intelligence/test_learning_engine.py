from datetime import datetime, timezone

from pocketbot.enterprise.intelligence.learning import (
    LearningEngine,
)
from pocketbot.enterprise.intelligence.learning.models import (
    LearningRecord,
    LearningState,
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


def test_learning_record_to_dict():

    record = LearningRecord(
        decision="optimize",
        score_before=60,
        score_after=80,
        feedback=0.9,
        timestamp=datetime.now(timezone.utc),
    )

    data = record.to_dict()

    assert data["decision"] == "optimize"
    assert data["improvement"] == 20
    assert "timestamp" in data


def test_learning_record_from_mapping():

    record = LearningRecord.from_mapping(
        {
            "decision": "train",
            "score_before": 10,
            "score_after": 30,
            "feedback": 0.5,
        }
    )

    assert record.decision == "train"
    assert record.improvement == 20


def test_learning_state_to_dict():

    state = LearningState.empty()

    data = state.to_dict()

    assert data["total_records"] == 0
    assert "last_update" in data


def test_learning_state_from_mapping():

    state = LearningState.from_mapping(
        {
            "total_records": 5,
            "average_feedback": 0.8,
            "adaptation_level": 25.0,
        }
    )

    assert state.total_records == 5
    assert state.average_feedback == 0.8
    assert state.adaptation_level == 25.0
