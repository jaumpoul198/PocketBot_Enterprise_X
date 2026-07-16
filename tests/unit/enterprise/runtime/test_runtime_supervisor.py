from pocketbot.enterprise.runtime.runtime_health import (
    RuntimeHealth,
)
from pocketbot.enterprise.runtime.runtime_recovery import (
    RuntimeRecoveryPolicy,
)
from pocketbot.enterprise.runtime.runtime_supervisor import (
    RuntimeSupervisor,
)


def test_runtime_supervisor_returns_true_when_healthy():
    health = RuntimeHealth(
        healthy=True,
        runtime_running=True,
        autonomy_running=True,
    )

    recovery = RuntimeRecoveryPolicy()

    supervisor = RuntimeSupervisor(
        health=health,
        recovery=recovery,
    )

    assert supervisor.evaluate() is True


def test_runtime_supervisor_recovers_when_unhealthy():
    health = RuntimeHealth(
        healthy=False,
        runtime_running=False,
        autonomy_running=False,
    )

    recovery = RuntimeRecoveryPolicy()

    supervisor = RuntimeSupervisor(
        health=health,
        recovery=recovery,
    )

    assert supervisor.evaluate() is True
