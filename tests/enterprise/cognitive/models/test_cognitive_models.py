from datetime import datetime, UTC

from pocketbot.enterprise.cognitive.models.cognitive_models import (
    CognitiveDecision,
    CognitiveSignal,
    CognitiveStateModel,
)


def test_cognitive_signal_creation():

    signal = CognitiveSignal(
        name="health",
        value=1.0,
        source="runtime",
        timestamp=datetime.now(UTC),
    )

    assert signal.name == "health"
    assert signal.value == 1.0


def test_cognitive_state_creation():

    state = CognitiveStateModel(
        state="IDLE",
        confidence=1.0,
        timestamp=datetime.now(UTC),
    )

    assert state.state == "IDLE"


def test_cognitive_decision_creation():

    decision = CognitiveDecision(
        action="PROCESS",
        confidence=1.0,
        reasoning="test",
        timestamp=datetime.now(UTC),
    )

    assert decision.action == "PROCESS"
