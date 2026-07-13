from pocketbot.domain.candle import (
    Candle,
)
from pocketbot.market.interfaces import (
    MarketProvider,
)
from pocketbot.market.providers.base_provider import (
    BaseProvider,
)
from pocketbot.market.providers.default_provider import (
    DefaultMarketProvider,
)
from pocketbot.market.providers.provider_factory import (
    ProviderFactory,
)


class FakeProvider(BaseProvider):
    def get_candles(
        self,
        asset: str,
        timeframe: int,
        count: int,
    ) -> list[Candle]:
        return []


def test_base_provider_connection_lifecycle() -> None:
    provider = FakeProvider()

    assert provider.is_connected() is False

    provider.connect()

    assert provider.is_connected() is True

    provider.disconnect()

    assert provider.is_connected() is False


def test_default_market_provider_returns_empty_candles() -> None:
    provider = DefaultMarketProvider()

    candles = provider.get_candles(
        "BTCUSDT",
        60,
        10,
    )

    assert candles == []


def test_provider_factory_returns_configured_provider() -> None:
    provider = DefaultMarketProvider()

    factory = ProviderFactory(
        provider,
    )

    result = factory.build()

    assert result is provider
