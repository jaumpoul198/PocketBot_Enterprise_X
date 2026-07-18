from pocketbot.enterprise.cognitive.core.cognitive_state import (
    CognitiveState,
)


def test_initial_state():

    state = CognitiveState()

    snapshot = state.snapshot()

    assert snapshot.state == "IDLE"


def test_state_update():

    state = CognitiveState()

    result = state.update(
        state="PROCESS",
        confidence=0.8,
    )

    assert result.state == "PROCESS"
    assert result.confidence == 0.8
