from pocketbot.enterprise.cognitive.autonomy import AutonomyState


def test_state_initialization():

    state = AutonomyState()

    snapshot = state.snapshot()

    assert snapshot["executions"] == 0
    assert snapshot["feedback"] == 0
    assert snapshot["evolution_events"] == 0


def test_state_records():

    state = AutonomyState()

    state.add_execution(
        {
            "approved": True
        }
    )

    state.add_feedback(
        {
            "reward": 1
        }
    )

    state.add_evolution_event(
        {
            "signal": "reinforce"
        }
    )

    snapshot = state.snapshot()

    assert snapshot["executions"] == 1
    assert snapshot["feedback"] == 1
    assert snapshot["evolution_events"] == 1
