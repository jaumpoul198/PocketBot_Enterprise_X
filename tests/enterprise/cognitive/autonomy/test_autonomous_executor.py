from pocketbot.enterprise.cognitive.autonomy import AutonomousExecutor


def test_executor_approves_high_confidence():

    executor = AutonomousExecutor()

    result = executor.execute(
        {
            "action": "adapt_strategy",
            "confidence": 0.95
        }
    )

    assert result["approved"] is True


def test_executor_blocks_low_confidence():

    executor = AutonomousExecutor()

    result = executor.execute(
        {
            "action": "unknown_action",
            "confidence": 0.3
        }
    )

    assert result["approved"] is False


def test_execution_history():

    executor = AutonomousExecutor()

    executor.execute(
        {
            "action": "learn",
            "confidence": 0.9
        }
    )

    assert executor.get_execution_count() == 1
