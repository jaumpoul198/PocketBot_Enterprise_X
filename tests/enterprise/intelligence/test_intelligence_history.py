from pocketbot.enterprise.intelligence import IntelligenceHistory


def test_history_record():

    history = IntelligenceHistory()

    event = history.record(
        decision="maintain",
        confidence=0.95,
        health_score=100,
    )

    assert event["decision"] == "maintain"
    assert event["autonomy_score"] == 97.5


def test_history_autonomy_score():

    history = IntelligenceHistory()

    history.record(
        decision="monitor",
        confidence=0.80,
        health_score=80,
    )

    assert history.autonomy_score() == 80.0
