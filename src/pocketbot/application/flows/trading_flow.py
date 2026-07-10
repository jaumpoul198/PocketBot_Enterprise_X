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
from pocketbot.application.services.application_service import (
    ApplicationService,
)


class TradingApplicationFlow:
    """
    Application use case for trading execution.
    """

    def __init__(
        self,
        application_service: ApplicationService,
    ) -> None:

        self._application_service = (
            application_service
        )

    def execute(
        self,
        request: TradingRequest,
    ) -> TradingResult:
        """
        Executes the trading application flow.
        """

        return self._application_service.execute_pipeline(
            request,
        )
