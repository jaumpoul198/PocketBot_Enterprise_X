from __future__ import annotations

from dataclasses import asdict, dataclass


@dataclass(frozen=True)
class HealthResponse:
    """
    HTTP health response model.
    """

    status: str
    service: str
    healthy: bool
    ready: bool
    alive: bool
    uptime_seconds: float

    def to_dict(self) -> dict[str, object]:
        return asdict(self)
