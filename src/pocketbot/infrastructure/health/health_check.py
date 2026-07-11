"""
PocketBot Enterprise X

Infrastructure Health Check Model.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import UTC, datetime
from enum import Enum


class HealthStatus(str, Enum):
    """
    Represents health state of an infrastructure component.
    """

    HEALTHY = "healthy"
    DEGRADED = "degraded"
    UNHEALTHY = "unhealthy"


@dataclass(slots=True)
class HealthCheck:
    """
    Represents an operational health check result.
    """

    name: str
    status: HealthStatus
    message: str = ""

    metadata: dict[str, str] = field(
        default_factory=dict,
    )

    created_at: datetime = field(
        default_factory=lambda: datetime.now(UTC),
    )
