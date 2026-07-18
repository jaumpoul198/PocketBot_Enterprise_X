from pocketbot.enterprise.cognitive.core.cognitive_engine import (
    CognitiveEngine,
)


def test_engine_process():

    engine = CognitiveEngine()

    decision = engine.process()

    assert decision.action == "PERCEIVE"
    assert decision.confidence == 1.0


def test_engine_status():

    engine = CognitiveEngine()

    engine.process()

    status = engine.status()

    assert "state" in status
    assert "cycle" in status
