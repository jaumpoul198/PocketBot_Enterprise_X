"""
PocketBot Enterprise X

In Memory Trade Decision Repository.
"""

from __future__ import annotations

from copy import deepcopy

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

    Repository state is isolated from external references.
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

        if decision is None:
            raise TypeError(
                "trade decision cannot be None",
            )

        if not isinstance(decision, TradeDecision):
            raise TypeError(
                "invalid trade decision type",
            )

        copied_decision = deepcopy(
            decision,
        )

        if not isinstance(
            copied_decision,
            TradeDecision,
        ):
            raise TypeError(
                "invalid copied trade decision type",
            )

        if copied_decision.asset not in self._decisions:
            self._decisions[
                copied_decision.asset
            ] = []

        self._decisions[
            copied_decision.asset
        ].append(
            copied_decision,
        )

    def get_latest(
        self,
        asset: str,
    ) -> TradeDecision | None:

        if not isinstance(asset, str):
            raise TypeError(
                "asset must be a string",
            )

        if not asset.strip():
            raise ValueError(
                "asset cannot be empty",
            )

        decisions = self._decisions.get(
            asset,
        )

        if not decisions:
            return None

        latest = max(
            decisions,
            key=lambda item: item.timestamp,
        )

        copied_latest = deepcopy(
            latest,
        )

        if not isinstance(
            copied_latest,
            TradeDecision,
        ):
            raise TypeError(
                "invalid copied latest trade decision type",
            )

        return copied_latest