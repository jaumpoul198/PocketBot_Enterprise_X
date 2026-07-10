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
from pocketbot.trading.models.trade_decision import (
    TradeDecision,
)
from pocketbot.trading.services.trading_decision_recorder import (
    TradingDecisionRecorder,
)


class TradingApplicationFlow:
    """
    Application use case for trading execution.
    """

    def __init__(
        self,
        pipeline: TradingPipelineProtocol,
        recorder: TradingDecisionRecorder,
    ) -> None:

        self._pipeline = pipeline
        self._recorder = recorder

    def execute(
        self,
        request: TradingRequest,
    ) -> TradingResult:
        """
        Executes the trading application flow.
        """

        result = self._pipeline.execute(
            request,
        )

        decision = TradeDecision(
            asset=result.market.asset,
            decision=result.decision.signal.value,
            strategy=(
                result.strategy.signal.value
                if result.strategy is not None
                else None
            ),
            score=result.score.score,
            timestamp=result.score.timestamp,
        )

        self._recorder.record(
            decision,
        )

        return result
