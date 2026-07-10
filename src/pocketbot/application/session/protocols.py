"""
PocketBot Enterprise X

Trading session protocols.
"""

from __future__ import annotations

from typing import Protocol

from pocketbot.application.pipeline.models import (
    TradingRequest,
    TradingResult,
)
from pocketbot.application.session.models import (
    TradingSession,
)


class TradingSessionManagerProtocol(Protocol):
    """
    Contract for trading session management.
    """

    def create_session(
        self,
        request: TradingRequest,
    ) -> TradingSession:
        """
        Create a trading session.
        """
        ...

    def execute(
        self,
        session: TradingSession,
    ) -> TradingResult:
        """
        Execute a trading session.
        """
        ...

    def close(
        self,
        session: TradingSession,
    ) -> None:
        """
        Close a trading session.
        """
        ...
