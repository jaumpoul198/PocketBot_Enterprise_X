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

        self._repository = repository

    def record(
        self,
        decision: TradeDecision,
    ) -> None:

        self._repository.save(
            decision,
        )
