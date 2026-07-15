from pocketbot.production.autonomy.recovery import (
    AutonomyRecoveryManager,
)
from pocketbot.production.autonomy.state import (
    AutonomyState,
)


def test_recovery_manager_recovers() -> None:
    state = AutonomyState()
    manager = AutonomyRecoveryManager(state)

    assert manager.recover() is True
    assert state.recovery_attempts == 1
    assert state.last_action == "recovery"


def test_recovery_manager_available() -> None:
    state = AutonomyState()
    manager = AutonomyRecoveryManager(state)

    assert manager.is_available() is True
