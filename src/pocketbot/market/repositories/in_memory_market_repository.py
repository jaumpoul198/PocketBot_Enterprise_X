"""
PocketBot Enterprise X

In Memory Market Repository.
"""

from __future__ import annotations

from copy import deepcopy
from datetime import datetime

from pocketbot.market.interfaces.market_repository import MarketRepository
from pocketbot.market.models.market_snapshot import MarketSnapshot


class InMemoryMarketRepository(MarketRepository):
    """
    Stores market snapshots in memory with state isolation.
    """

    def __init__(self) -> None:
        self._snapshots: dict[
            tuple[str, int],
            list[MarketSnapshot],
        ] = {}

    def _validate_snapshot(
        self,
        snapshot: MarketSnapshot,
    ) -> None:

        if snapshot is None:
            raise ValueError(
                "snapshot cannot be None",
            )

        if not isinstance(
            snapshot,
            MarketSnapshot,
        ):
            raise TypeError(
                "snapshot must be a MarketSnapshot",
            )

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

        if not asset:
            raise ValueError(
                "asset cannot be empty",
            )

    def _validate_timeframe(
        self,
        timeframe: int,
    ) -> None:

        if timeframe is None:
            raise ValueError(
                "timeframe cannot be None",
            )

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

    def save(
        self,
        snapshot: MarketSnapshot,
    ) -> None:
        """
        Stores an isolated snapshot copy.
        """

        self._validate_snapshot(
            snapshot,
        )

        key = (
            snapshot.asset,
            snapshot.timeframe,
        )

        if key not in self._snapshots:
            self._snapshots[key] = []

        self._snapshots[key].append(
            deepcopy(snapshot),
        )

    def get_latest(
        self,
        asset: str,
        timeframe: int,
    ) -> MarketSnapshot | None:
        """
        Returns an isolated latest snapshot copy.
        """

        self._validate_asset(
            asset,
        )

        self._validate_timeframe(
            timeframe,
        )

        key = (
            asset,
            timeframe,
        )

        snapshots = self._snapshots.get(key)

        if not snapshots:
            return None

        latest = max(
            snapshots,
            key=lambda snapshot: snapshot.timestamp,
        )

        return deepcopy(latest)

    def get_last_n(
        self,
        asset: str,
        timeframe: int,
        limit: int,
    ) -> list[MarketSnapshot]:
        """
        Returns isolated snapshot copies.
        """

        self._validate_asset(
            asset,
        )

        self._validate_timeframe(
            timeframe,
        )

        if limit is None:
            raise ValueError(
                "limit cannot be None",
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

        key = (
            asset,
            timeframe,
        )

        snapshots = self._snapshots.get(key, [])

        return deepcopy(
            sorted(
                snapshots,
                key=lambda snapshot: snapshot.timestamp,
                reverse=True,
            )[:limit],
        )

    def get_between(
        self,
        asset: str,
        timeframe: int,
        start: datetime,
        end: datetime,
    ) -> list[MarketSnapshot]:
        """
        Returns isolated snapshots within a time range.
        """

        self._validate_asset(
            asset,
        )

        self._validate_timeframe(
            timeframe,
        )

        if start is None or end is None:
            raise ValueError(
                "date range cannot be None",
            )

        key = (
            asset,
            timeframe,
        )

        snapshots = self._snapshots.get(key, [])

        return deepcopy(
            [
                snapshot
                for snapshot in snapshots
                if start <= snapshot.timestamp <= end
            ],
        )

    def clear(self) -> None:
        """
        Clears stored snapshots.
        """

        self._snapshots.clear()