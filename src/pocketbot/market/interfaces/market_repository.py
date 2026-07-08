"""
PocketBot Enterprise X

Market Repository Interface.
"""

from __future__ import annotations

from abc import ABC, abstractmethod

from pocketbot.market.models.market_snapshot import MarketSnapshot


class MarketRepository(ABC):
    """
    Contract for market snapshot persistence.
    """

    @abstractmethod
    def save(
        self,
        snapshot: MarketSnapshot,
    ) -> None:
        """
        Stores a market snapshot.
        """
        raise NotImplementedError

    @abstractmethod
    def get_latest(
        self,
        asset: str,
        timeframe: int,
    ) -> MarketSnapshot | None:
        """
        Retrieves the latest market snapshot.
        """
        raise NotImplementedError

    @abstractmethod
    def clear(self) -> None:
        """
        Clears stored market data.
        """
        raise NotImplementedError
