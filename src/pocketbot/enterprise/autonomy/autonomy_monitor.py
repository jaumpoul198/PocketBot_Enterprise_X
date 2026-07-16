"""Enterprise autonomy monitoring primitives."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import UTC, datetime
from typing import Any


@dataclass(frozen=True)
class AutonomySnapshot:
    """Immutable snapshot representing autonomy runtime status."""

    timestamp: datetime
    healthy: bool
    active: bool
    metrics: dict[str, Any]

    @classmethod
    def create(
        cls,
        *,
        healthy: bool = True,
        active: bool = False,
        metrics: dict[str, Any] | None = None,
    ) -> AutonomySnapshot:
        """Create a runtime snapshot."""

        return cls(
            timestamp=datetime.now(UTC),
            healthy=healthy,
            active=active,
            metrics=metrics or {},
        )


class AutonomyMonitor:
    """Enterprise autonomy runtime monitor.

    Responsible for collecting and exposing the current
    autonomy execution state.
    """

    def __init__(self) -> None:
        self._healthy = True
        self._active = False
        self._metrics: dict[str, Any] = {}

    def start(self) -> None:
        """Activate autonomy monitoring."""

        self._active = True

    def stop(self) -> None:
        """Deactivate autonomy monitoring."""

        self._active = False

    def update_health(self, healthy: bool) -> None:
        """Update runtime health state."""

        self._healthy = healthy

    def update_metric(
        self,
        name: str,
        value: Any,
    ) -> None:
        """Register or update a runtime metric."""

        self._metrics[name] = value

    def snapshot(self) -> AutonomySnapshot:
        """Return current autonomy snapshot."""

        return AutonomySnapshot.create(
            healthy=self._healthy,
            active=self._active,
            metrics=dict(self._metrics),
        )

    @property
    def healthy(self) -> bool:
        """Current health status."""

        return self._healthy

    @property
    def active(self) -> bool:
        """Current activation status."""

        return self._active
