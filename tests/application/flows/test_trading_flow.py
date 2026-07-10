"""
PocketBot Enterprise X

Trading application flow tests.
"""

from __future__ import annotations

from pocketbot.application.flows.trading_flow import (
    TradingApplicationFlow,
)
from pocketbot.application.pipeline.models import (
    TradingRequest,
    TradingResult,
)


class FakeTradingPipeline:

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


def test_trading_flow_executes_pipeline() -> None:

    pipeline = FakeTradingPipeline()

    flow = TradingApplicationFlow(
        pipeline,
    )

    request = TradingRequest(
        asset="BTCUSDT",
        timeframe=60,
        indicators=[
            "rsi",
            "ema",
            "macd",
        ],
    )

    result = flow.execute(
        request,
    )

    assert result is not None
    assert pipeline.called is True
    assert pipeline.request == request
