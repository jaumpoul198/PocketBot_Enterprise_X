"""
PocketBot Enterprise X

Trading application flow failure scenarios.
"""

from __future__ import annotations

from datetime import UTC, datetime
from unittest.mock import Mock

import pytest

from pocketbot.application.flows.trading_flow import (
    TradingApplicationFlow,
)
from pocketbot.application.requests import (
    TradingRequest,
)


class FailingRecorder:
    """
    Recorder that simulates persistence failure.
    """

    def record(
        self,
        *_args: object,
        **_kwargs: object,
    ) -> None:
        raise RuntimeError(
            "recorder unavailable",
        )


def test_trading_flow_propagates_recorder_failure() -> None:
    """
    Recorder failures must propagate.
    """

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
            timestamp=datetime.now(UTC),
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