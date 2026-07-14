"""
PocketBot Enterprise X

Trading Decision Recorder Service.
"""

from __future__ import annotations

from pocketbot.trading.interfaces.trade_decision_repository import (
    TradeDecisionRepository,
)
from pocketbot.trading.models.trade_decision import (
    TradeDecision,
)


class TradingDecisionRecorder:
    """
    Application service responsible for recording
    generated trading decisions.
    """

    def __init__(
        self,
        repository: TradeDecisionRepository,
    ) -> None:

        if repository is None:
            raise TypeError(
                "repository cannot be None",
            )

        self._repository = repository

    def record(
        self,
        decision: TradeDecision,
    ) -> None:

        if decision is None:
            raise TypeError(
                "trade decision cannot be None",
            )

        self._repository.save(
            decision,
        )