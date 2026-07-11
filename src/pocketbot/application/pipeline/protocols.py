"""
PocketBot Enterprise X

Trading Pipeline protocols.
"""

from __future__ import annotations

from typing import Protocol

from pocketbot.application.pipeline.models import (
    TradingRequest,
    TradingResult,
)


class TradingPipelineProtocol(Protocol):
    """
    Contract for trading pipeline execution.
    """

    def execute(
        self,
        request: TradingRequest,
    ) -> TradingResult:
        """
        Execute complete trading analysis pipeline.
        """
        ...
