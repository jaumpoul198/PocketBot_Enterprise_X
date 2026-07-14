"""
PocketBot Enterprise X

Trading session manager.
"""

from __future__ import annotations

from uuid import uuid4

from pocketbot.application.orchestrator.trading_orchestrator import (
    TradingOrchestrator,
)
from pocketbot.application.pipeline.models import (
    TradingRequest,
    TradingResult,
)
from pocketbot.application.session.exceptions import (
    InvalidTradingSessionError,
)
from pocketbot.application.session.models import (
    TradingSession,
    TradingSessionStatus,
)


class TradingSessionManager:
    """
    Coordinates operational trading sessions.

    This component manages session lifecycle and delegates
    execution to the trading orchestrator.
    """

    def __init__(
        self,
        orchestrator: TradingOrchestrator,
    ) -> None:
        self._orchestrator = orchestrator

    def create_session(
        self,
        request: TradingRequest,
    ) -> TradingSession:
        """
        Create a new trading session.
        """

        return TradingSession(
            session_id=str(uuid4()),
            request=request,
        )

    def execute(
        self,
        session: TradingSession,
    ) -> TradingResult:
        """
        Execute a trading session.
        """

        if session.status is not TradingSessionStatus.CREATED:
            raise InvalidTradingSessionError(
                "Trading session cannot be executed."
            )

        session.status = TradingSessionStatus.RUNNING

        try:
            result = self._orchestrator.execute(
                session.request,
            )

            session.result = result
            session.status = TradingSessionStatus.COMPLETED

            return result

        except Exception:
            # Session lifecycle requires failure state transition.
            # Original exception is intentionally preserved.
            session.status = TradingSessionStatus.FAILED
            raise

    def close(
        self,
        session: TradingSession,
    ) -> None:
        """
        Close a completed or failed trading session.
        """

        if session.status is TradingSessionStatus.RUNNING:
            raise InvalidTradingSessionError(
                "Cannot close a running session."
            )

        if session.status is TradingSessionStatus.CLOSED:
            raise InvalidTradingSessionError(
                "Session already closed."
            )

        session.status = TradingSessionStatus.CLOSED