"""
PocketBot Enterprise X

In Memory Market Repository.
"""

from __future__ import annotations

from pocketbot.market.interfaces.market_repository import MarketRepository
from pocketbot.market.models.market_snapshot import MarketSnapshot


class InMemoryMarketRepository(MarketRepository):
    """
    Stores market snapshots in memory.
    """

    def __init__(self) -> None:
        self._snapshots: dict[tuple[str, int], MarketSnapshot] = {}

    def save(
        self,
        snapshot: MarketSnapshot,
    ) -> None:
        key = (
            snapshot.asset,
            snapshot.timeframe,
        )

        self._snapshots[key] = snapshot

    def get_latest(
        self,
        asset: str,
        timeframe: int,
    ) -> MarketSnapshot | None:

        key = (
            asset,
            timeframe,
        )

        return self._snapshots.get(key)

    def clear(self) -> None:
        self._snapshots.clear()
