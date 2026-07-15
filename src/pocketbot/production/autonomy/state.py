from __future__ import annotations

from dataclasses import dataclass


@dataclass
class AutonomyState:
    """
    Runtime autonomy state.
    """

    healthy: bool = True
    recovery_attempts: int = 0
    last_action: str = "initialized"

    def record_recovery(self) -> None:
        self.recovery_attempts += 1
        self.last_action = "recovery"

    def mark_healthy(self) -> None:
        self.healthy = True
        self.last_action = "healthy"

    def mark_unhealthy(self) -> None:
        self.healthy = False
        self.last_action = "unhealthy"
