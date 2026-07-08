from __future__ import annotations

from dataclasses import dataclass, field
from datetime import UTC, datetime
from typing import Any
from uuid import uuid4


@dataclass(slots=True)
class Event:
    """
    Evento base do sistema.
    """

    name: str

    payload: dict[str, Any]

    id: str = field(default_factory=lambda: str(uuid4()))

    created_at: datetime = field(default_factory=lambda: datetime.now(UTC))
