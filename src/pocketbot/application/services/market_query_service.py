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

        if repository is None:
            raise TypeError(
                "repository cannot be None",
            )

        self._repository = repository

    def get_latest_market(
        self,
        asset: str,
        timeframe: int,
    ) -> MarketSnapshot | None:

        if not asset:
            raise ValueError(
                "asset cannot be empty",
            )

        if timeframe <= 0:
            raise ValueError(
                "timeframe must be positive",
            )

        return self._repository.get_latest(
            asset,
            timeframe,
        )