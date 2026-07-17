from pocketbot.enterprise.cognitive.autonomy import EvolutionAdapter


def test_adapter_process_event():

    adapter = EvolutionAdapter()

    result = adapter.process_event(
        {
            "signal": "reinforce",
            "reward": 0.9,
        }
    )

    assert result["signal"] == "reinforce"
    assert result["metric"].maturity == "ADVANCED"


def test_adapter_latest():

    adapter = EvolutionAdapter()

    adapter.process_event(
        {
            "signal": "adjust",
            "reward": 0.5,
        }
    )

    metric = adapter.latest()

    assert metric is not None
