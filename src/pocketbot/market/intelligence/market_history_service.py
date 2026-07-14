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
        if repository is None:
            raise ValueError(
                "repository cannot be None",
            )

        if (
            not hasattr(repository, "get_last_n")
            or not hasattr(repository, "get_between")
        ):
            raise TypeError(
                "repository must provide market history methods",
            )

        self._repository = repository

    def _validate_asset(
        self,
        asset: str,
    ) -> None:

        if asset is None:
            raise ValueError(
                "asset cannot be None",
            )

        if not isinstance(
            asset,
            str,
        ):
            raise TypeError(
                "asset must be a string",
            )

    def _validate_timeframe(
        self,
        timeframe: int,
    ) -> None:

        if (
            not isinstance(
                timeframe,
                int,
            )
            or isinstance(
                timeframe,
                bool,
            )
        ):
            raise TypeError(
                "timeframe must be an integer",
            )

    def get_last_n(
        self,
        asset: str,
        timeframe: int,
        limit: int,
    ) -> list[MarketSnapshot]:
        """
        Returns the last N market snapshots.
        """

        self._validate_asset(
            asset,
        )

        self._validate_timeframe(
            timeframe,
        )

        if (
            not isinstance(
                limit,
                int,
            )
            or isinstance(
                limit,
                bool,
            )
        ):
            raise TypeError(
                "limit must be an integer",
            )

        if limit <= 0:
            raise ValueError(
                "limit must be greater than zero",
            )

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

        self._validate_asset(
            asset,
        )

        self._validate_timeframe(
            timeframe,
        )

        if start is None:
            raise ValueError(
                "start cannot be None",
            )

        if end is None:
            raise ValueError(
                "end cannot be None",
            )

        if start > end:
            raise ValueError(
                "start must be before end",
            )

        return self._repository.get_between(
            asset,
            timeframe,
            start,
            end,
        )
