"""
PocketBot Enterprise X

Infrastructure Metric Model.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import UTC, datetime


@dataclass(slots=True)
class Metric:
    """
    Represents an operational metric.
    """

    name: str
    value: int

    created_at: datetime = field(
        default_factory=lambda: datetime.now(UTC),
    )
