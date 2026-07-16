from __future__ import annotations

import time
from dataclasses import dataclass, field
from threading import Lock


@dataclass
class RuntimeMetrics:
    """
    Enterprise runtime metrics collector.
    """

    startup_count: int = 0
    shutdown_count: int = 0
    recovery_count: int = 0
    failure_count: int = 0

    started_at: float | None = None
    last_shutdown_at: float | None = None

    state: str = "stopped"

    _lock: Lock = field(default_factory=Lock, repr=False)

    def startup(self) -> None:
        with self._lock:
            self.startup_count += 1
            self.started_at = time.time()
            self.state = "running"

    def shutdown(self) -> None:
        with self._lock:
            self.shutdown_count += 1
            self.last_shutdown_at = time.time()
            self.state = "stopped"

    def recovery(self) -> None:
        with self._lock:
            self.recovery_count += 1

    def failure(self) -> None:
        with self._lock:
            self.failure_count += 1
            self.state = "failed"

    def uptime_seconds(self) -> float:
        with self._lock:
            if self.started_at is None:
                return 0.0

            return max(
                0.0,
                time.time() - self.started_at
            )

    def snapshot(self) -> dict:
        with self._lock:
            return {
                "startup_count": self.startup_count,
                "shutdown_count": self.shutdown_count,
                "recovery_count": self.recovery_count,
                "failure_count": self.failure_count,
                "uptime_seconds": self.uptime_seconds(),
                "state": self.state,
            }
