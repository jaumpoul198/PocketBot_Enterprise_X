"""
PocketBot Enterprise X

Trading application flow tests.
"""

from __future__ import annotations

from datetime import UTC, datetime

from pocketbot.application.flows.trading_flow import (
    TradingApplicationFlow,
)
from pocketbot.application.pipeline.models import (
    TradingRequest,
    TradingResult,
)
from pocketbot.risk.models.risk_assessment import (
    RiskAssessment,
    RiskStatus,
)
from pocketbot.decision.result import DecisionResult
from pocketbot.domain.enums import SignalType
from pocketbot.market.models.market_snapshot import MarketSnapshot
from pocketbot.score.result import ScoreResult
from pocketbot.market.strategy.models import (
    StrategyResult,
    StrategySignal,
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
            market=MarketSnapshot(
                asset="BTCUSDT",
                timeframe=60,
            ),
            indicators=[],
            score=ScoreResult(
                score=80.0,
                confidence=0.9,
                strength=0.8,
                weight_sum=1.0,
                indicators=3,
            ),
            strategy=StrategyResult(
                signal=StrategySignal.BUY,
                confidence=0.8,
                reason="test",
            ),
            decision=DecisionResult(
                signal=SignalType.BUY,
                score=80.0,
                confidence=0.9,
                approved=True,
                reason="test",
            ),   
             risk=RiskAssessment(
                status=RiskStatus.APPROVED,
                reason="test",
            ),
        )


class FakeTradingDecisionRecorder:

    def __init__(self) -> None:
        self.called = False
        self.result = None

    def record(
        self,
        decision,
    ) -> None:

        self.called = True
        self.result = decision


def test_trading_flow_executes_pipeline() -> None:

    pipeline = FakeTradingPipeline()

    recorder = FakeTradingDecisionRecorder()

    flow = TradingApplicationFlow(
        pipeline,
        recorder,
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
    assert recorder.called is True
