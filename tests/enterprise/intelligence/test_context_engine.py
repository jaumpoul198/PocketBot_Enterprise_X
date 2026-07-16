from pocketbot.enterprise.intelligence.context.context_engine import ContextEngine


def test_context_engine_register_decision():

    engine = ContextEngine()

    context = engine.register_decision(
        decision_id="decision-001",
        score=0.85,
        input_context={
            "market": "XAUUSD"
        },
        feedback={
            "success": True
        }
    )

    assert context.decision_id == "decision-001"
    assert context.score == 0.85


def test_context_history():

    engine = ContextEngine()

    engine.register_decision(
        decision_id="decision-002",
        score=0.70
    )

    history = engine.get_context_history()

    assert len(history) == 1
