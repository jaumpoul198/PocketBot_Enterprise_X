from pocketbot.enterprise.intelligence.adaptive import AdaptiveEngine


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
