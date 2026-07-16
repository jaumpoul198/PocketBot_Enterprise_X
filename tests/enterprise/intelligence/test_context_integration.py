from pocketbot.enterprise.intelligence.context.context_integration import (
    ContextIntegration,
)


def test_context_integration_process_decision():

    integration = ContextIntegration()

    result = integration.process_decision(
        decision_id="decision-100",
        score=0.92,
        input_context={
            "market": "XAUUSD",
            "timeframe": "M1",
        },
        feedback={
            "result": "success"
        },
    )

    assert result.decision_id == "decision-100"
    assert result.score == 0.92


def test_context_integration_history():

    integration = ContextIntegration()

    integration.process_decision(
        decision_id="decision-200",
        score=0.80,
    )

    history = integration.get_context()

    assert len(history) == 1
