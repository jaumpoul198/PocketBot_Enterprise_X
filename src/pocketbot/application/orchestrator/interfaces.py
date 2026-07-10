"""
PocketBot Enterprise X

Trading orchestrator interfaces.
"""

from __future__ import annotations

from typing import Protocol

from pocketbot.application.pipeline.models import (
    TradingRequest,
    TradingResult,
)


class TradingFlowProtocol(Protocol):
    """
    Contract for trading application flow.
    """

    def execute(
        self,
        request: TradingRequest,
    ) -> TradingResult:
        """
        Execute trading flow.
        """
        ...
