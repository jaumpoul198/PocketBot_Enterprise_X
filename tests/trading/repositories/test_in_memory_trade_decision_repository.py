"""
PocketBot Enterprise X

Trade decision repository tests.
"""

from __future__ import annotations

from datetime import UTC, datetime

from pocketbot.trading.models.trade_decision import (
    TradeDecision,
)
from pocketbot.trading.repositories.in_memory_trade_decision_repository import (
    InMemoryTradeDecisionRepository,
)


def test_save_and_get_latest_trade_decision() -> None:

    repository = InMemoryTradeDecisionRepository()

    decision = TradeDecision(
        asset="BTCUSDT",
        decision="BUY",
        strategy="momentum",
        score=0.85,
        timestamp=datetime.now(UTC),
    )

    repository.save(
        decision,
    )

    result = repository.get_latest(
        "BTCUSDT",
    )

    assert result is not None
    assert result.asset == "BTCUSDT"
    assert result.decision == "BUY"
    assert result.strategy == "momentum"
