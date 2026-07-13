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
) -> TradingPipelineService:

    return TradingPipelineService(
        market_service or Mock(),
        indicator_pipeline or Mock(),
        Mock(),
        Mock(),
        Mock(),
        Mock(),
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
