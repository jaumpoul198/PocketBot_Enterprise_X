from pocketbot.enterprise.cognitive.autonomy import CognitiveAutonomy


def test_autonomy_initial_state():
    autonomy = CognitiveAutonomy()

    status = autonomy.get_status()

    assert status["state"] == "initialized"
    assert status["cycles"] == 0


def test_autonomy_high_confidence():
    autonomy = CognitiveAutonomy()

    result = autonomy.evaluate_autonomy(
        {
            "confidence": 0.9
        }
    )

    assert result["status"] == "autonomous_ready"
    assert result["autonomy_score"] == 0.9


def test_autonomy_assisted_mode():
    autonomy = CognitiveAutonomy()

    result = autonomy.evaluate_autonomy(
        {
            "confidence": 0.6
        }
    )

    assert result["status"] == "assisted_autonomy"


def test_execute_autonomous_cycle():
    autonomy = CognitiveAutonomy()

    autonomy.evaluate_autonomy(
        {
            "confidence": 0.9
        }
    )

    result = autonomy.execute_cycle(
        {
            "action": "optimize_strategy"
        }
    )

    assert result["executed"] is True
    assert result["cycle"] == 1
