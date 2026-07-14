"""
PocketBot Enterprise X

Trading decision recorder tests.
"""

from __future__ import annotations

from datetime import UTC, datetime

import pytest

from pocketbot.trading.models.trade_decision import (
    TradeDecision,
)
from pocketbot.trading.services.trading_decision_recorder import (
    TradingDecisionRecorder,
)
from pocketbot.trading.repositories.in_memory_trade_decision_repository import (
    InMemoryTradeDecisionRepository,
)


def create_decision() -> TradeDecision:
    return TradeDecision(
        asset="BTCUSDT",
        decision="BUY",
        strategy="momentum",
        score=0.90,
        timestamp=datetime.now(UTC),
    )


def test_recorder_persists_trade_decision() -> None:

    repository = InMemoryTradeDecisionRepository()

    recorder = TradingDecisionRecorder(
        repository,
    )

    recorder.record(
        create_decision(),
    )

    result = repository.get_latest(
        "BTCUSDT",
    )

    assert result is not None
    assert result.asset == "BTCUSDT"
    assert result.decision == "BUY"


def test_recorder_rejects_none_decision() -> None:

    repository = InMemoryTradeDecisionRepository()

    recorder = TradingDecisionRecorder(
        repository,
    )

    with pytest.raises(
        TypeError,
        match="trade decision cannot be None",
    ):
        recorder.record(None)  # type: ignore[arg-type]


def test_recorder_rejects_none_repository() -> None:

    with pytest.raises(
        TypeError,
        match="repository cannot be None",
    ):
        TradingDecisionRecorder(None)  # type: ignore[arg-type]