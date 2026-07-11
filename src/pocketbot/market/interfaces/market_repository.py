"""
PocketBot Enterprise X

Market Repository Interface.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from datetime import datetime

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
    def get_last_n(
        self,
        asset: str,
        timeframe: int,
        limit: int,
    ) -> list[MarketSnapshot]:
        """
        Retrieves the latest N market snapshots.
        """
        raise NotImplementedError

    @abstractmethod
    def get_between(
        self,
        asset: str,
        timeframe: int,
        start: datetime,
        end: datetime,
    ) -> list[MarketSnapshot]:
        """
        Retrieves market snapshots between two dates.
        """
        raise NotImplementedError

    @abstractmethod
    def clear(self) -> None:
        """
        Clears stored market data.
        """
        raise NotImplementedError