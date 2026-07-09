from unittest.mock import Mock

from pocketbot.application.pipeline.models import (
    TradingRequest,
)
from pocketbot.application.pipeline.service import (
    TradingPipelineService,
)
from pocketbot.decision.result import DecisionResult
from pocketbot.domain.enums import SignalType
from pocketbot.market.models.market_snapshot import (
    MarketSnapshot,
)
from pocketbot.market.strategy.models import (
    StrategyResult,
    StrategySignal,
)
from pocketbot.score.result import ScoreResult


def test_trading_pipeline_executes_complete_flow():

    market_service = Mock()
    indicator_pipeline = Mock()
    score_engine = Mock()
    strategy_service = Mock()
    decision_engine = Mock()

    snapshot = MarketSnapshot(
        asset="BTCUSDT",
        timeframe=15,
    )

    market_service.get_latest_market.return_value = snapshot

    indicator_pipeline.execute.return_value = []

    score_engine.calculate.return_value = ScoreResult(
        score=90.0,
        confidence=0.9,
        strength=0.8,
        weight_sum=1.0,
        indicators=1,
    )

    strategy_service.analyze.return_value = [
        StrategyResult(
            signal=StrategySignal.BUY,
            confidence=0.9,
            reason="Momentum confirmed",
        )
    ]

    decision_engine.decide.return_value = DecisionResult(
        signal=SignalType.BUY,
        score=90.0,
        confidence=0.9,
        approved=True,
        reason="Approved",
    )

    pipeline = TradingPipelineService(
        market_service,
        indicator_pipeline,
        score_engine,
        strategy_service,
        decision_engine,
    )

    result = pipeline.execute(
        TradingRequest(
            asset="BTCUSDT",
            timeframe=15,
        )
    )

    assert result.market == snapshot
    assert result.decision.approved is True
    assert result.decision.signal is SignalType.BUY

    market_service.get_latest_market.assert_called_once_with(
        "BTCUSDT",
        15,
    )
