"""
PocketBot Enterprise X

Trading orchestrator.

Application component responsible for coordinating
trading execution flows.
"""

from __future__ import annotations

from pocketbot.application.orchestrator.interfaces import (
    TradingFlowProtocol,
)
from pocketbot.application.pipeline.models import (
    TradingRequest,
    TradingResult,
)


class TradingOrchestrator:
    """
    Coordinates trading application execution.
    """

    def __init__(
        self,
        flow: TradingFlowProtocol,
    ) -> None:

        self._flow = flow

    def execute(
        self,
        request: TradingRequest,
    ) -> TradingResult:
        """
        Execute trading workflow.
        """

        return self._flow.execute(
            request,
        )
