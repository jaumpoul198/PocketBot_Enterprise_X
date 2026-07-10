"""
PocketBot Enterprise X

Trading Application Flow.

Application use case responsible for executing
the trading analysis workflow.
"""

from __future__ import annotations

from pocketbot.application.pipeline.models import (
    TradingRequest,
    TradingResult,
)
from pocketbot.application.pipeline.protocols import (
    TradingPipelineProtocol,
)


class TradingApplicationFlow:
    """
    Application use case for trading execution.
    """

    def __init__(
        self,
        pipeline: TradingPipelineProtocol,
    ) -> None:

        self._pipeline = pipeline

    def execute(
        self,
        request: TradingRequest,
    ) -> TradingResult:
        """
        Executes the trading application flow.
        """

        return self._pipeline.execute(
            request,
        )
