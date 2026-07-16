from pocketbot.enterprise.intelligence import IntelligenceEngine


def test_intelligence_engine_normal():

    engine = IntelligenceEngine()

    decision = engine.analyze(95)

    assert decision.action == "maintain"
    assert decision.confidence > 0.9


def test_intelligence_engine_risk():

    engine = IntelligenceEngine()

    decision = engine.analyze(40)

    assert decision.action == "intervene"
