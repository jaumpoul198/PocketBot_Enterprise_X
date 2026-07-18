from pocketbot.enterprise.cognitive.autonomy import AutonomyEvolutionBridge


def test_positive_evolution_signal():

    bridge = AutonomyEvolutionBridge()

    result = bridge.process_feedback(
        {
            "reward": 0.9
        }
    )

    assert result["signal"] == "reinforce"


def test_adjust_evolution_signal():

    bridge = AutonomyEvolutionBridge()

    result = bridge.process_feedback(
        {
            "reward": 0.5
        }
    )

    assert result["signal"] == "adjust"


def test_discard_evolution_signal():

    bridge = AutonomyEvolutionBridge()

    result = bridge.process_feedback(
        {
            "reward": 0.1
        }
    )

    assert result["signal"] == "discard"


def test_event_history():

    bridge = AutonomyEvolutionBridge()

    bridge.process_feedback(
        {
            "reward": 1
        }
    )

    assert len(
        bridge.get_events()
    ) == 1
