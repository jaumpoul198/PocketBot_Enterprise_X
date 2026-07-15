from __future__ import annotations

from pocketbot.production.autonomy.state import (
    AutonomyState,
)


class AutonomyRecoveryManager:
    """
    Handles production runtime recovery actions.
    """

    def __init__(
        self,
        state: AutonomyState,
    ) -> None:
        self._state = state

    def recover(self) -> bool:
        self._state.record_recovery()
        return True

    def is_available(self) -> bool:
        return self._state.recovery_attempts >= 0
