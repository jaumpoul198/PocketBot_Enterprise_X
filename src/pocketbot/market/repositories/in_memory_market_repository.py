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

    def save(
        self,
        snapshot: MarketSnapshot,
    ) -> None:
        """
        Stores an isolated snapshot copy.
        """

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
