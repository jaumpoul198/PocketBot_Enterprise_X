"""
PocketBot Enterprise X

Trade Decision Repository Interface.
"""

from __future__ import annotations

from pocketbot.trading.models.trade_decision import (
    TradeDecision,
)


class TradeDecisionRepository:
    """
    Repository contract for trade decisions.
    """

    def save(
        self,
        decision: TradeDecision,
    ) -> None:
        raise NotImplementedError

    def get_latest(
        self,
        asset: str,
    ) -> TradeDecision | None:
        raise NotImplementedError
