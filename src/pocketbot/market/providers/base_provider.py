"""
PocketBot Enterprise X
Base Market Provider
"""

from __future__ import annotations

from pocketbot.market.interfaces import MarketProvider


class BaseProvider(MarketProvider):
    """
    Classe base para todos os provedores.
    """

    def __init__(self) -> None:
        self._connected = False

    def connect(self) -> None:
        self._connected = True

    def disconnect(self) -> None:
        self._connected = False

    def is_connected(self) -> bool:
        return self._connected
