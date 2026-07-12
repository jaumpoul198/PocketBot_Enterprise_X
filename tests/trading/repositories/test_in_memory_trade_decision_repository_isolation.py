from __future__ import annotations

from datetime import UTC, datetime

from pocketbot.trading.models.trade_decision import TradeDecision
from pocketbot.trading.repositories.in_memory_trade_decision_repository import (
    InMemoryTradeDecisionRepository,
)


def create_decision() -> TradeDecision:
    return TradeDecision(
        asset="BTC",
        decision="BUY",
        strategy="momentum",
        score=0.95,
        timestamp=datetime.now(UTC),
    )


def test_saved_trade_decision_is_isolated_from_external_reference() -> None:
    repository = InMemoryTradeDecisionRepository()

    decision = create_decision()

    repository.save(decision)

    latest = repository.get_latest("BTC")

    assert latest is not None
    assert latest is not decision


def test_retrieved_trade_decision_is_isolated_from_repository_state() -> None:
    repository = InMemoryTradeDecisionRepository()

    repository.save(
        create_decision()
    )

    first = repository.get_latest("BTC")

    assert first is not None

    second = repository.get_latest("BTC")

    assert second is not None
    assert first is not second
