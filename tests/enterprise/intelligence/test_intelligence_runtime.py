from pocketbot.enterprise.intelligence import IntelligenceRuntime


def test_runtime_evaluation():

    runtime = IntelligenceRuntime()

    decision = runtime.evaluate(95)

    assert decision.action == "maintain"


def test_runtime_status():

    runtime = IntelligenceRuntime()

    runtime.evaluate(40)

    status = runtime.status()

    assert status["last_decision"].action == "intervene"
