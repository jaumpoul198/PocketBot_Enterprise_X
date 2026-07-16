"""Enterprise autonomy monitoring primitives."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import UTC, datetime
from enum import Enum
from typing import Any


class AutonomyFailureState(str, Enum):
    """Autonomy failure lifecycle state."""

    HEALTHY = "healthy"
    WARNING = "warning"
    FAILED = "failed"
    RECOVERING = "recovering"
    RECOVERED = "recovered"


@dataclass(frozen=True)
class AutonomySnapshot:
    """Immutable snapshot representing autonomy runtime status."""

    timestamp: datetime
    healthy: bool
    active: bool
    failure_state: AutonomyFailureState
    metrics: dict[str, Any]

    @classmethod
    def create(
        cls,
        *,
        healthy: bool = True,
        active: bool = False,
        failure_state: AutonomyFailureState = AutonomyFailureState.HEALTHY,
        metrics: dict[str, Any] | None = None,
    ) -> AutonomySnapshot:
        """Create a runtime snapshot."""

        return cls(
            timestamp=datetime.now(UTC),
            healthy=healthy,
            active=active,
            failure_state=failure_state,
            metrics=metrics or {},
        )


class AutonomyMonitor:
    """Enterprise autonomy runtime monitor."""

    def __init__(self) -> None:
        self._healthy = True
        self._active = False
        self._failure_state = AutonomyFailureState.HEALTHY
        self._metrics: dict[str, Any] = {}

    def start(self) -> None:
        self._active = True

    def stop(self) -> None:
        self._active = False

    def update_health(
        self,
        healthy: bool,
    ) -> None:

        self._healthy = healthy

        if healthy:
            self._failure_state = AutonomyFailureState.HEALTHY
        else:
            self._failure_state = AutonomyFailureState.FAILED

    def mark_failure(self) -> None:
        self._healthy = False
        self._failure_state = AutonomyFailureState.FAILED

    def mark_recovering(self) -> None:
        self._failure_state = AutonomyFailureState.RECOVERING

    def mark_recovered(self) -> None:
        self._healthy = True
        self._failure_state = AutonomyFailureState.RECOVERED

    def update_metric(
        self,
        name: str,
        value: Any,
    ) -> None:

        self._metrics[name] = value

    def snapshot(self) -> AutonomySnapshot:

        return AutonomySnapshot.create(
            healthy=self._healthy,
            active=self._active,
            failure_state=self._failure_state,
            metrics=dict(self._metrics),
        )

    @property
    def healthy(self) -> bool:
        return self._healthy

    @property
    def active(self) -> bool:
        return self._active

    @property
    def failure_state(self) -> AutonomyFailureState:
        return self._failure_state
