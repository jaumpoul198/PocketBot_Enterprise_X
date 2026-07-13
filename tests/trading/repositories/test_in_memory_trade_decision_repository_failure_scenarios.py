from datetime import UTC, datetime
from unittest.mock import patch

from pocketbot.trading.models.trade_decision import TradeDecision
from pocketbot.trading.repositories.in_memory_trade_decision_repository import (
    InMemoryTradeDecisionRepository,
)


def create_decision(asset: str = "BTCUSDT") -> TradeDecision:
    return TradeDecision(
        asset=asset,
        decision="BUY",
        strategy="momentum",
        score=0.85,
        timestamp=datetime.now(UTC),
    )

def test_get_latest_returns_none_when_repository_is_empty() -> None:
    repository = InMemoryTradeDecisionRepository()

    assert repository.get_latest("BTCUSDT") is None


def test_get_latest_returns_none_for_unknown_asset() -> None:
    repository = InMemoryTradeDecisionRepository()

    repository.save(create_decision())

    assert repository.get_latest("ETHUSDT") is None


def test_save_propagates_deepcopy_failure() -> None:
    repository = InMemoryTradeDecisionRepository()

    decision = create_decision()

    with patch(
        "pocketbot.trading.repositories.in_memory_trade_decision_repository.deepcopy",
        side_effect=RuntimeError("deepcopy failure"),
    ):
        try:
            repository.save(decision)
            assert False
        except RuntimeError as exc:
            assert str(exc) == "deepcopy failure"
