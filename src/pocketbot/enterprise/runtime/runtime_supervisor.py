"""
PocketBot Enterprise X

Enterprise Runtime Supervisor.
"""

from __future__ import annotations

from pocketbot.enterprise.runtime.runtime_health import RuntimeHealth
from pocketbot.enterprise.runtime.runtime_recovery import (
    RuntimeRecoveryPolicy,
)


class RuntimeSupervisor:
    """
    Coordinates runtime health and recovery policy.
    """

    def __init__(
        self,
        health: RuntimeHealth,
        recovery: RuntimeRecoveryPolicy,
    ) -> None:
        self._health = health
        self._recovery = recovery

    @property
    def health(self) -> RuntimeHealth:
        return self._health

    @property
    def recovery(self) -> RuntimeRecoveryPolicy:
        return self._recovery

    def evaluate(self) -> bool:
        """
        Evaluates runtime state.
        """

        if self._health.healthy:
            return True

        result = self._recovery.recover()

        return result.recovered
