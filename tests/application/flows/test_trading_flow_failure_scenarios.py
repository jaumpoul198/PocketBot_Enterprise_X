from unittest.mock import Mock

import pytest

from pocketbot.application.flows.trading_flow import (
    TradingApplicationFlow,
)
from pocketbot.application.pipeline.models import (
    TradingRequest,
)
from pocketbot.application.pipeline.exceptions import (
    TradingPipelineError,
)


class FailingPipeline:

    def execute(
        self,
        request: TradingRequest,
    ):
        raise TradingPipelineError(
            "pipeline unavailable",
        )


class FailingRecorder:

    def record(
        self,
        decision,
    ) -> None:
        raise RuntimeError(
            "recorder unavailable",
        )


def test_trading_flow_propagates_pipeline_failure() -> None:
    flow = TradingApplicationFlow(
        pipeline=FailingPipeline(),
        recorder=Mock(),
    )

    with pytest.raises(
        TradingPipelineError,
        match="pipeline unavailable",
    ):
        flow.execute(
            TradingRequest(
                asset="BTCUSDT",
                timeframe=60,
            )
        )


def test_trading_flow_propagates_recorder_failure() -> None:
    pipeline = Mock()

    pipeline.execute.return_value = Mock(
        market=Mock(
            asset="BTCUSDT",
        ),
        decision=Mock(
            signal=Mock(
                value="BUY",
            ),
        ),
        strategy=None,
        score=Mock(
            score=90.0,
            timestamp=None,
        ),
    )

    flow = TradingApplicationFlow(
        pipeline=pipeline,
        recorder=FailingRecorder(),
    )

    with pytest.raises(
        RuntimeError,
        match="recorder unavailable",
    ):
        flow.execute(
            TradingRequest(
                asset="BTCUSDT",
                timeframe=60,
            )
        )
