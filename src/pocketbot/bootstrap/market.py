"""
PocketBot Enterprise X

Market Bootstrap.
"""

from __future__ import annotations

from pocketbot.market.interfaces import MarketProvider
from pocketbot.market.providers.provider_factory import ProviderFactory


def build_market(
    provider: MarketProvider,
) -> MarketProvider:
    """
    Builds the market provider.
    """

    return ProviderFactory(provider).build()
