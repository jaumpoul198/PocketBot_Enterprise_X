from __future__ import annotations

from pocketbot.production.autonomy.recovery import (
    AutonomyRecoveryManager,
)
from pocketbot.production.autonomy.state import (
    AutonomyState,
)


class AutonomyController:
    """
    Enterprise autonomy runtime controller.
    """

    def __init__(
        self,
        state: AutonomyState,
        recovery: AutonomyRecoveryManager,
    ) -> None:
        self._state = state
        self._recovery = recovery

    def healthy(self) -> bool:
        return self._state.healthy

    def mark_healthy(self) -> bool:
        self._state.mark_healthy()
        return self._state.healthy

    def mark_unhealthy(self) -> bool:
        self._state.mark_unhealthy()
        return not self._state.healthy

    def recover(self) -> bool:
        return self._recovery.recover()
