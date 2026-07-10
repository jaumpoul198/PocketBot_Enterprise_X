"""
PocketBot Enterprise X

Trading pipeline risk integration tests.
"""

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
from pocketbot.risk.models.risk_assessment import (
    RiskAssessment,
    RiskStatus,
)
from pocketbot.risk.models.risk_profile import (
    RiskProfile,
)
from pocketbot.risk.services.default_risk_service import (
    DefaultRiskService,
)
from pocketbot.score.result import ScoreResult


def build_pipeline(
    risk_service,
) -> TradingPipelineService:

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

    return TradingPipelineService(
        market_service,
        indicator_pipeline,
        score_engine,
        strategy_service,
        decision_engine,
        risk_service,
    )


def test_pipeline_continues_when_risk_is_approved():

    risk_service = Mock()

    risk_service.evaluate.return_value = RiskAssessment(
        status=RiskStatus.APPROVED,
        reason="Risk approved.",
    )

    pipeline = build_pipeline(risk_service)

    result = pipeline.execute(
        TradingRequest(
            asset="BTCUSDT",
            timeframe=15,
        )
    )

    assert result.risk.approved is True
    assert result.decision.approved is True


def test_pipeline_records_rejected_risk():

    risk_service = Mock()

    risk_service.evaluate.return_value = RiskAssessment(
        status=RiskStatus.REJECTED,
        reason="Exposure exceeds limit.",
    )

    pipeline = build_pipeline(risk_service)

    result = pipeline.execute(
        TradingRequest(
            asset="BTCUSDT",
            timeframe=15,
        )
    )

    assert result.risk.status is RiskStatus.REJECTED
    assert result.risk.reason == "Exposure exceeds limit."


def test_default_risk_service_rejects_excessive_exposure():

    service = DefaultRiskService()

    result = service.evaluate(
        position_size=1.0,
        current_exposure=1.0,
    )

    assert result.status is RiskStatus.REJECTED


def test_invalid_risk_profile_is_rejected():

    try:
        RiskProfile(
            max_position_size=0,
            max_loss_percentage=2.0,
            max_exposure_percentage=50.0,
        )

        assert False

    except ValueError:
        assert True
