from pocketbot.enterprise.runtime.runtime_health import (
    RuntimeHealthSupervisor,
)


def test_runtime_health_healthy():

    supervisor = RuntimeHealthSupervisor()

    health = supervisor.evaluate(
        runtime_running=True,
        autonomy_running=True,
    )

    assert health.healthy is True


def test_runtime_health_unhealthy():

    supervisor = RuntimeHealthSupervisor()

    health = supervisor.evaluate(
        runtime_running=True,
        autonomy_running=False,
    )

    assert health.healthy is False
