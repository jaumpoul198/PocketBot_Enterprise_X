from unittest.mock import Mock

import pytest

from pocketbot.domain.candle import Candle
from pocketbot.market.collectors.default_market_collector import (
    DefaultMarketCollector,
)


def build_candle() -> Candle:
    return Mock(spec=Candle)


def build_collector(
    provider=None,
    validator=None,
    cache=None,
    repository=None,
) -> DefaultMarketCollector:

    return DefaultMarketCollector(
        provider or Mock(),
        validator or Mock(),
        cache or Mock(),
        repository or Mock(),
    )


def test_collector_propagates_provider_failure() -> None:
    provider = Mock()

    provider.get_candles.side_effect = RuntimeError(
        "provider unavailable",
    )

    collector = build_collector(
        provider=provider,
    )

    with pytest.raises(
        RuntimeError,
        match="provider unavailable",
    ):
        collector.collect(
            "BTCUSDT",
            60,
            10,
        )


def test_collector_propagates_validator_failure() -> None:
    provider = Mock()
    validator = Mock()

    provider.get_candles.return_value = [
        build_candle(),
    ]

    validator.validate.side_effect = RuntimeError(
        "validator unavailable",
    )

    collector = build_collector(
        provider=provider,
        validator=validator,
    )

    with pytest.raises(
        RuntimeError,
        match="validator unavailable",
    ):
        collector.collect(
            "BTCUSDT",
            60,
            10,
        )


def test_collector_propagates_cache_failure() -> None:
    provider = Mock()
    validator = Mock()
    cache = Mock()

    provider.get_candles.return_value = [
        build_candle(),
    ]

    validator.validate.return_value = True

    cache.save.side_effect = RuntimeError(
        "cache unavailable",
    )

    collector = build_collector(
        provider=provider,
        validator=validator,
        cache=cache,
    )

    with pytest.raises(
        RuntimeError,
        match="cache unavailable",
    ):
        collector.collect(
            "BTCUSDT",
            60,
            10,
        )


def test_collector_propagates_repository_failure() -> None:
    provider = Mock()
    validator = Mock()
    repository = Mock()

    provider.get_candles.return_value = [
        build_candle(),
    ]

    validator.validate.return_value = True

    repository.save.side_effect = RuntimeError(
        "repository unavailable",
    )

    collector = build_collector(
        provider=provider,
        validator=validator,
        repository=repository,
    )

    with pytest.raises(
        RuntimeError,
        match="repository unavailable",
    ):
        collector.collect(
            "BTCUSDT",
            60,
            10,
        )


def test_collector_persists_valid_market_data() -> None:
    provider = Mock()
    validator = Mock()
    cache = Mock()
    repository = Mock()

    candles = [
        build_candle(),
    ]

    provider.get_candles.return_value = candles
    validator.validate.return_value = True

    collector = build_collector(
        provider=provider,
        validator=validator,
        cache=cache,
        repository=repository,
    )

    result = collector.collect(
        "BTCUSDT",
        60,
        10,
    )

    assert result == candles

    cache.save.assert_called_once()
    repository.save.assert_called_once()
