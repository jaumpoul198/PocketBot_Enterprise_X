from pocketbot.production.autonomy.controller import (
    AutonomyController,
)
from pocketbot.production.autonomy.recovery import (
    AutonomyRecoveryManager,
)
from pocketbot.production.autonomy.state import (
    AutonomyState,
)


def test_autonomy_controller() -> None:
    state = AutonomyState()

    controller = AutonomyController(
        state,
        AutonomyRecoveryManager(state),
    )

    assert controller.healthy() is True

    assert controller.mark_unhealthy() is True
    assert state.healthy is False

    assert controller.recover() is True
    assert state.recovery_attempts == 1

    assert controller.mark_healthy() is True
    assert state.healthy is True
