"""
PocketBot Enterprise X

Market History Intelligence Service.
"""

from __future__ import annotations

from datetime import datetime

from pocketbot.market.interfaces.market_repository import (
    MarketRepository,
)
from pocketbot.market.models.market_snapshot import (
    MarketSnapshot,
)


class MarketHistoryService:
    """
    Provides historical market analysis queries.
    """

    def __init__(
        self,
        repository: MarketRepository,
    ) -> None:
        self._repository = repository

    def get_last_n(
        self,
        asset: str,
        timeframe: int,
        limit: int,
    ) -> list[MarketSnapshot]:
        """
        Returns the last N market snapshots.
        """

        return self._repository.get_last_n(
            asset,
            timeframe,
            limit,
        )

    def get_between(
        self,
        asset: str,
        timeframe: int,
        start: datetime,
        end: datetime,
    ) -> list[MarketSnapshot]:
        """
        Returns snapshots between two dates.
        """

        return self._repository.get_between(
            asset,
            timeframe,
            start,
            end,
        )
