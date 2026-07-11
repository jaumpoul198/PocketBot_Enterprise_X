"""
PocketBot Enterprise X

Market Query Service.
"""

from __future__ import annotations

from pocketbot.market.interfaces.market_repository import (
    MarketRepository,
)
from pocketbot.market.models.market_snapshot import (
    MarketSnapshot,
)


class MarketQueryService:
    """
    Service responsible for querying persisted market snapshots.
    """

    def __init__(
        self,
        repository: MarketRepository,
    ) -> None:
        self._repository = repository

    def get_latest_market(
        self,
        asset: str,
        timeframe: int,
    ) -> MarketSnapshot | None:

        return self._repository.get_latest(
            asset,
            timeframe,
        )