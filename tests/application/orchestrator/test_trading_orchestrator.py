"""
PocketBot Enterprise X

Trading orchestrator tests.
"""

from __future__ import annotations

from pocketbot.application.orchestrator.trading_orchestrator import (
    TradingOrchestrator,
)
from pocketbot.application.pipeline.models import (
    TradingRequest,
    TradingResult,
)
from pocketbot.decision.result import DecisionResult
from pocketbot.risk.models.risk_assessment import (
    RiskAssessment,
    RiskStatus,
)
from pocketbot.score.result import ScoreResult


class FakeTradingFlow:
    """
    Fake trading flow used for orchestrator testing.
    """

    def __init__(self) -> None:

        self.called = False

        self.request = None

    def execute(
        self,
        request: TradingRequest,
    ) -> TradingResult:

        self.called = True

        self.request = request

        return TradingResult(
            market=None,  # type: ignore[arg-type]
            indicators=[],
            score=None,  # type: ignore[arg-type]
            strategy=None,
            decision=None,  # type: ignore[arg-type]
            risk=RiskAssessment(
                status=RiskStatus.APPROVED,
                reason="test",
            ),
        )


def test_trading_orchestrator_executes_application_flow() -> None:

    flow = FakeTradingFlow()

    orchestrator = TradingOrchestrator(
        flow,
    )

    request = TradingRequest(
        asset="BTCUSDT",
        timeframe=60,
        indicators=[
            "rsi",
        ],
    )

    result = orchestrator.execute(
        request,
    )

    assert result is not None

    assert flow.called is True

    assert flow.request == request
