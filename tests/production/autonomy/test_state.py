from pocketbot.production.autonomy.state import (
    AutonomyState,
)


def test_autonomy_state_recovery() -> None:
    state = AutonomyState()

    assert state.healthy is True
    assert state.recovery_attempts == 0

    state.mark_unhealthy()
    state.record_recovery()

    assert state.healthy is False
    assert state.recovery_attempts == 1
    assert state.last_action == "recovery"


def test_autonomy_state_health() -> None:
    state = AutonomyState()

    state.mark_unhealthy()
    state.mark_healthy()

    assert state.healthy is True
    assert state.last_action == "healthy"
