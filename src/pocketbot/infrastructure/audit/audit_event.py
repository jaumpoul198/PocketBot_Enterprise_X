"""
PocketBot Enterprise X

Infrastructure Audit Event Model.
"""

from __future__ import annotations

from copy import deepcopy
from dataclasses import dataclass, field
from datetime import UTC, datetime
from enum import Enum
from typing import Any
from uuid import uuid4


class AuditSeverity(str, Enum):
    """
    Represents audit severity.
    """

    INFO = "info"
    WARNING = "warning"
    ERROR = "error"
    CRITICAL = "critical"


@dataclass(slots=True)
class AuditEvent:
    """
    Represents an operational audit event.
    """

    event_name: str
    source: str
    severity: AuditSeverity = AuditSeverity.INFO

    metadata: dict[str, Any] = field(
        default_factory=dict,
    )

    id: str = field(
        default_factory=lambda: str(uuid4()),
    )

    created_at: datetime = field(
        default_factory=lambda: datetime.now(UTC),
    )

    def __post_init__(self) -> None:
        self.metadata = deepcopy(
            self.metadata,
        )
