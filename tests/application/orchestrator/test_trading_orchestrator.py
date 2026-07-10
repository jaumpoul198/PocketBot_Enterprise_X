"""
PocketBot Enterprise X

Trading orchestrator tests.
"""

from __future__ import annotations

from pocketbot.application.pipeline.models import (
    TradingRequest,
    TradingResult,
)
from pocketbot.application.orchestrator.trading_orchestrator import (
    TradingOrchestrator,
)


class FakeTradingFlow:

    def __init__(self) -> None:
        self.called = False
        self.request: TradingRequest | None = None

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
