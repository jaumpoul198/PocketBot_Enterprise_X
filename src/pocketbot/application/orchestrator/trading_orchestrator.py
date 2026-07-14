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

        if flow is None:
            raise TypeError(
                "flow cannot be None",
            )

        self._flow = flow

    def execute(
        self,
        request: TradingRequest,
    ) -> TradingResult:
        """
        Execute trading workflow.
        """

        if request is None:
            raise TypeError(
                "request cannot be None",
            )

        return self._flow.execute(
            request,
        )