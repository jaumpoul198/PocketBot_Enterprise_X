"""
PocketBot Enterprise X

In Memory Market Repository.
"""

from __future__ import annotations

from datetime import datetime

from pocketbot.market.interfaces.market_repository import MarketRepository
from pocketbot.market.models.market_snapshot import MarketSnapshot


class InMemoryMarketRepository(MarketRepository):
    """
    Stores market snapshots in memory.
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
        key = (
            snapshot.asset,
            snapshot.timeframe,
        )

        if key not in self._snapshots:
            self._snapshots[key] = []

        self._snapshots[key].append(snapshot)

    def get_latest(
        self,
        asset: str,
        timeframe: int,
    ) -> MarketSnapshot | None:
        key = (
            asset,
            timeframe,
        )

        snapshots = self._snapshots.get(key)

        if not snapshots:
            return None

        return max(
            snapshots,
            key=lambda snapshot: snapshot.timestamp,
        )

    def get_last_n(
        self,
        asset: str,
        timeframe: int,
        limit: int,
    ) -> list[MarketSnapshot]:
        key = (
            asset,
            timeframe,
        )

        snapshots = self._snapshots.get(key, [])

        return sorted(
            snapshots,
            key=lambda snapshot: snapshot.timestamp,
            reverse=True,
        )[:limit]

    def get_between(
        self,
        asset: str,
        timeframe: int,
        start: datetime,
        end: datetime,
    ) -> list[MarketSnapshot]:
        key = (
            asset,
            timeframe,
        )

        snapshots = self._snapshots.get(key, [])

        return [
            snapshot
            for snapshot in snapshots
            if start <= snapshot.timestamp <= end
        ]

    def clear(self) -> None:
        self._snapshots.clear()