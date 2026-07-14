from unittest.mock import Mock

import pytest

from pocketbot.application.pipeline.exceptions import (
    TradingPipelineError,
)
from pocketbot.application.pipeline.models import (
    TradingRequest,
)
from pocketbot.application.pipeline.service import (
    TradingPipelineService,
)


def build_pipeline(
    market_service=None,
    indicator_pipeline=None,
    score_engine=None,
    strategy_service=None,
    decision_engine=None,
    risk_service=None,
) -> TradingPipelineService:

    return TradingPipelineService(
        market_service or Mock(),
        indicator_pipeline or Mock(),
        score_engine or Mock(),
        strategy_service or Mock(),
        decision_engine or Mock(),
        risk_service or Mock(),
    )


def test_pipeline_raises_error_when_market_snapshot_missing() -> None:
    market_service = Mock()

    market_service.get_latest_market.return_value = None

    pipeline = build_pipeline(
        market_service=market_service,
    )

    with pytest.raises(
        TradingPipelineError,
        match="Market snapshot not found",
    ):
        pipeline.execute(
            TradingRequest(
                asset="BTCUSDT",
                timeframe=15,
            )
        )


def test_pipeline_propagates_indicator_failure() -> None:
    market_service = Mock()
    indicator_pipeline = Mock()

    market_service.get_latest_market.return_value = Mock()

    indicator_pipeline.execute.side_effect = RuntimeError(
        "indicator unavailable",
    )

    pipeline = build_pipeline(
        market_service=market_service,
        indicator_pipeline=indicator_pipeline,
    )

    with pytest.raises(
        RuntimeError,
        match="indicator unavailable",
    ):
        pipeline.execute(
            TradingRequest(
                asset="BTCUSDT",
                timeframe=15,
            )
        )


def test_pipeline_propagates_score_failure() -> None:
    market_service = Mock()
    score_engine = Mock()

    market_service.get_latest_market.return_value = Mock()

    score_engine.calculate.side_effect = RuntimeError(
        "score unavailable",
    )

    pipeline = build_pipeline(
        market_service=market_service,
        score_engine=score_engine,
    )

    with pytest.raises(
        RuntimeError,
        match="score unavailable",
    ):
        pipeline.execute(
            TradingRequest(
                asset="BTCUSDT",
                timeframe=15,
            )
        )


def test_pipeline_propagates_strategy_failure() -> None:
    market_service = Mock()
    strategy_service = Mock()

    market_service.get_latest_market.return_value = Mock()

    strategy_service.analyze.side_effect = RuntimeError(
        "strategy unavailable",
    )

    pipeline = build_pipeline(
        market_service=market_service,
        strategy_service=strategy_service,
    )

    with pytest.raises(
        RuntimeError,
        match="strategy unavailable",
    ):
        pipeline.execute(
            TradingRequest(
                asset="BTCUSDT",
                timeframe=15,
            )
        )


def test_pipeline_propagates_decision_failure() -> None:
    market_service = Mock()
    strategy_service = Mock()
    decision_engine = Mock()

    market_service.get_latest_market.return_value = Mock()

    strategy_service.analyze.return_value = []

    decision_engine.decide.side_effect = RuntimeError(
        "decision unavailable",
    )

    pipeline = build_pipeline(
        market_service=market_service,
        strategy_service=strategy_service,
        decision_engine=decision_engine,
    )

    with pytest.raises(
        RuntimeError,
        match="decision unavailable",
    ):
        pipeline.execute(
            TradingRequest(
                asset="BTCUSDT",
                timeframe=15,
            )
        )


def test_pipeline_propagates_risk_failure() -> None:
    market_service = Mock()
    strategy_service = Mock()
    risk_service = Mock()

    market_service.get_latest_market.return_value = Mock()

    strategy_service.analyze.return_value = []

    risk_service.evaluate.side_effect = RuntimeError(
        "risk unavailable",
    )

    pipeline = build_pipeline(
        market_service=market_service,
        strategy_service=strategy_service,
        risk_service=risk_service,
    )

    with pytest.raises(
        RuntimeError,
        match="risk unavailable",
    ):
        pipeline.execute(
            TradingRequest(
                asset="BTCUSDT",
                timeframe=15,
            )
        )
