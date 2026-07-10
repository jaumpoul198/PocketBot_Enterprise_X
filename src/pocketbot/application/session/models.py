"""
PocketBot Enterprise X

Trading session models.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum

from pocketbot.application.pipeline.models import (
    TradingRequest,
    TradingResult,
)


class TradingSessionStatus(str, Enum):
    """
    Trading session lifecycle states.
    """

    CREATED = "created"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"


@dataclass
class TradingSession:
    """
    Represents an operational trading session.
    """

    session_id: str
    request: TradingRequest
    status: TradingSessionStatus = TradingSessionStatus.CREATED
    result: TradingResult | None = None
