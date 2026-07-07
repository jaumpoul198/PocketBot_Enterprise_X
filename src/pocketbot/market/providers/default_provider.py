"""
PocketBot Enterprise X

Default Market Provider.
"""

from __future__ import annotations

from pocketbot.domain.candle import Candle
from pocketbot.market.providers.base_provider import BaseProvider


class DefaultMarketProvider(BaseProvider):
    """
    Default market provider implementation.

    This provider is a placeholder infrastructure provider
    that can later be replaced by exchange integrations.
    """

    def get_candles(
        self,
        asset: str,
        timeframe: int,
        count: int,
    ) -> list[Candle]:
        """
        Returns market candles.

        Currently returns an empty collection until a concrete
        market integration is configured.
        """

        return []