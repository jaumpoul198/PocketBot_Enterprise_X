from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class HealthStatus:
    healthy: bool
    service: str


def check_health(service_name: str = "pocketbot") -> HealthStatus:
    return HealthStatus(
        healthy=True,
        service=service_name,
    )
