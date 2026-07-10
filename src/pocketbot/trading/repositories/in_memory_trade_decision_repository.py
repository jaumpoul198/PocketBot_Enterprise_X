"""
PocketBot Enterprise X

In Memory Trade Decision Repository.
"""

from __future__ import annotations

from pocketbot.trading.interfaces.trade_decision_repository import (
    TradeDecisionRepository,
)
from pocketbot.trading.models.trade_decision import (
    TradeDecision,
)


class InMemoryTradeDecisionRepository(
    TradeDecisionRepository,
):
    """
    Stores trade decisions in memory.
    """

    def __init__(self) -> None:

        self._decisions: dict[
            str,
            list[TradeDecision],
        ] = {}

    def save(
        self,
        decision: TradeDecision,
    ) -> None:

        if decision.asset not in self._decisions:
            self._decisions[
                decision.asset
            ] = []

        self._decisions[
            decision.asset
        ].append(
            decision,
        )

    def get_latest(
        self,
        asset: str,
    ) -> TradeDecision | None:

        decisions = self._decisions.get(
            asset,
        )

        if not decisions:
            return None

        return max(
            decisions,
            key=lambda item: item.timestamp,
        )
