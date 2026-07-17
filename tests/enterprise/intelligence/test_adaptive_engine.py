from pocketbot.enterprise.intelligence.adaptive import (
    AdaptiveEngine,
    AdaptiveDecision,
)

def test_high_autonomy():

    engine = AdaptiveEngine()

    result = engine.evaluate(95.0)

    assert result.mode == "autonomous"
    assert result.threshold == 0.90


def test_medium_autonomy():

    engine = AdaptiveEngine()

    result = engine.evaluate(75.0)

    assert result.mode == "assisted"


def test_low_autonomy():

    engine = AdaptiveEngine()

    result = engine.evaluate(40.0)

    assert result.mode == "supervised"

def test_adaptive_decision_to_dict():

    engine = AdaptiveEngine()

    result = engine.evaluate(95.0)

    data = result.to_dict()

    assert data["mode"] == "autonomous"
    assert data["threshold"] == 0.90


def test_adaptive_decision_from_mapping():

    data = {
        "threshold": 0.70,
        "mode": "assisted",
        "confidence_floor": 0.80,
    }

    result = AdaptiveDecision.from_mapping(data)

    assert result.mode == "assisted"
    assert result.confidence_floor == 0.80
