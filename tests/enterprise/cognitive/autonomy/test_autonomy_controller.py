from pocketbot.enterprise.cognitive.autonomy import AutonomyController


def test_controller_start():

    controller = AutonomyController()

    result = controller.start()

    assert result["status"] == "started"
    assert controller.active is True


def test_controller_process_action():

    controller = AutonomyController()

    result = controller.process_action(
        {
            "type": "optimize"
        },
        0.95
    )

    assert result["autonomous"] is True
    assert result["cycle"] == 1


def test_controller_metrics():

    controller = AutonomyController()

    controller.process_action(
        {
            "type": "learn"
        },
        0.7
    )

    metrics = controller.get_metrics()

    assert metrics["cycles"] == 1
    assert metrics["actions"] == 1
