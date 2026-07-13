"""
PocketBot Enterprise X

Market Connection Hosted Service.
"""

from __future__ import annotations

from pocketbot.application.hosting.interfaces import (
    HostedService,
)
from pocketbot.market.interfaces import (
    MarketProvider,
)


class MarketConnectionService(HostedService):
    """
    Manages market provider lifecycle.
    """

    def __init__(
        self,
        market_provider: MarketProvider,
    ) -> None:

        if market_provider is None:
            raise ValueError(
                "market_provider cannot be None",
            )

        required_methods = (
            "is_connected",
            "connect",
            "disconnect",
        )

        if not all(
            callable(
                getattr(
                    market_provider,
                    method,
                    None,
                )
            )
            for method in required_methods
        ):
            raise TypeError(
                "invalid market provider",
            )

        self._market_provider = market_provider

    def start(self) -> None:
        """
        Starts market connection.
        """

        if not self._market_provider.is_connected():
            self._market_provider.connect()

    def stop(self) -> None:
        """
        Stops market connection.
        """

        if self._market_provider.is_connected():
            self._market_provider.disconnect()
