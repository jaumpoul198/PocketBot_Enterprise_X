"""
PocketBot Enterprise X

Market Provider Factory.
"""

from __future__ import annotations

from pocketbot.market.interfaces import MarketProvider


class ProviderFactory:
    """
    Factory responsible for providing the active
    market provider implementation.
    """

    def __init__(
        self,
        provider: MarketProvider,
    ) -> None:
        self._provider = provider

    def build(self) -> MarketProvider:
        """
        Returns the configured provider.
        """
        return self._provider