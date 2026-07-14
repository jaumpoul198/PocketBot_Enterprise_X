"""
PocketBot Enterprise X

Trade Decision Repository Interface.
"""

from __future__ import annotations

from abc import ABC, abstractmethod

from pocketbot.trading.models.trade_decision import (
    TradeDecision,
)


class TradeDecisionRepository(ABC):
    """
    Repository contract for trade decisions.
    """

    @abstractmethod
    def save(
        self,
        decision: TradeDecision,
    ) -> None:
        """
        Persist a trade decision.
        """

        raise NotImplementedError

    @abstractmethod
    def get_latest(
        self,
        asset: str,
    ) -> TradeDecision | None:
        """
        Retrieve latest decision for asset.
        """

        raise NotImplementedError