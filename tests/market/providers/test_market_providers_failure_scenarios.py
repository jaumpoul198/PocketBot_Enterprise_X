from unittest.mock import Mock

import pytest

from pocketbot.domain.candle import Candle
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


def test_provider_connect_is_idempotent() -> None:
    provider = FakeProvider()

    provider.connect()
    provider.connect()

    assert provider.is_connected() is True


def test_provider_disconnect_is_idempotent() -> None:
    provider = FakeProvider()

    provider.disconnect()
    provider.disconnect()

    assert provider.is_connected() is False


def test_provider_factory_propagates_configured_provider() -> None:
    provider = Mock()

    factory = ProviderFactory(
        provider,
    )

    assert factory.build() is provider


def test_default_provider_returns_empty_collection_without_failure() -> None:
    provider = DefaultMarketProvider()

    candles = provider.get_candles(
        asset="BTCUSDT",
        timeframe=60,
        count=10,
    )

    assert candles == []


def test_provider_connection_failure_is_propagated() -> None:
    provider = Mock()

    provider.connect.side_effect = RuntimeError(
        "connection failure",
    )

    with pytest.raises(
        RuntimeError,
        match="connection failure",
    ):
        provider.connect()
