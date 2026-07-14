"""
PocketBot Enterprise X

Trading orchestrator failure scenario tests.
"""

from __future__ import annotations

import pytest

from pocketbot.application.orchestrator.trading_orchestrator import (
    TradingOrchestrator,
)
from pocketbot.application.pipeline.models import (
    TradingRequest,
)


class FailingTradingFlow:
    def execute(
        self,
        request: TradingRequest,
    ):
        raise RuntimeError(
            "Trading flow execution failed."
        )


class TrackingTradingFlow:
    def __init__(self) -> None:
        self.request = None

    def execute(
        self,
        request: TradingRequest,
    ):
        self.request = request

        return None


def test_orchestrator_propagates_flow_exception() -> None:

    orchestrator = TradingOrchestrator(
        FailingTradingFlow(),
    )

    request = TradingRequest(
        asset="BTCUSDT",
        timeframe=60,
    )

    with pytest.raises(
        RuntimeError,
        match="Trading flow execution failed.",
    ):
        orchestrator.execute(
            request,
        )


def test_orchestrator_forwards_request_to_flow() -> None:

    flow = TrackingTradingFlow()

    orchestrator = TradingOrchestrator(
        flow,
    )

    request = TradingRequest(
        asset="ETHUSDT",
        timeframe=15,
    )

    result = orchestrator.execute(
        request,
    )

    assert result is None
    assert flow.request == request
