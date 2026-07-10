"""
PocketBot Enterprise X

Trading decision recorder tests.
"""

from __future__ import annotations

from datetime import UTC, datetime

from pocketbot.trading.models.trade_decision import (
    TradeDecision,
)
from pocketbot.trading.services.trading_decision_recorder import (
    TradingDecisionRecorder,
)
from pocketbot.trading.repositories.in_memory_trade_decision_repository import (
    InMemoryTradeDecisionRepository,
)


def test_recorder_persists_trade_decision() -> None:

    repository = InMemoryTradeDecisionRepository()

    recorder = TradingDecisionRecorder(
        repository,
    )

    decision = TradeDecision(
        asset="BTCUSDT",
        decision="BUY",
        strategy="momentum",
        score=0.90,
        timestamp=datetime.now(UTC),
    )

    recorder.record(
        decision,
    )

    result = repository.get_latest(
        "BTCUSDT",
    )

    assert result is not None
    assert result.asset == "BTCUSDT"
    assert result.decision == "BUY"
