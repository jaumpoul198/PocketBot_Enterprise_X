from pocketbot.enterprise.intelligence import IntelligenceEngine


def test_intelligence_engine_normal():

    engine = IntelligenceEngine()

    decision = engine.analyze(95)

    assert decision.action == "maintain"
    assert decision.confidence > 0.9
    assert engine.learning.state().total_records == 1


def test_intelligence_engine_monitor():

    engine = IntelligenceEngine()

    decision = engine.analyze(75)

    assert decision.action == "monitor"
    assert engine.learning.state().total_records == 1


def test_intelligence_engine_risk():

    engine = IntelligenceEngine()

    decision = engine.analyze(40)

    assert decision.action == "intervene"
    assert engine.learning.state().total_records == 1


def test_intelligence_engine_multiple_analysis():

    engine = IntelligenceEngine()

    engine.analyze(95)
    engine.analyze(80)
    engine.analyze(45)

    state = engine.learning.state()

    assert state.total_records == 3
    assert state.adaptation_level > 0
