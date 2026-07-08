from datetime import UTC, datetime
from unittest.mock import Mock

from pocketbot.application.services.market_service import (
    MarketService,
)
from pocketbot.domain.candle import Candle
from pocketbot.domain.value_objects.price import Price
from pocketbot.market.models.market_snapshot import (
    MarketSnapshot,
)


def create_candle() -> Candle:
    return Candle(
        symbol="BTCUSDT",
        timeframe="60",
        open=Price(100.0),
        high=Price(110.0),
        low=Price(90.0),
        close=Price(105.0),
        volume=1000.0,
        timestamp=datetime.now(UTC),
    )


def create_service(
    candles: list[Candle],
) -> tuple[MarketService, Mock]:

    collector = Mock()
    cache = Mock()
    repository = Mock()
    validator = Mock()

    cache.load.return_value = []
    collector.collect.return_value = candles
    validator.validate.return_value = True

    service = MarketService(
        collector=collector,
        cache=cache,
        repository=repository,
        validator=validator,
    )

    return service, repository


def test_market_service_persists_snapshot_after_refresh() -> None:
    candles = [
        create_candle(),
    ]

    service, repository = create_service(
        candles,
    )

    result = service.refresh_market(
        asset="BTCUSDT",
        timeframe=60,
        count=1,
    )

    assert result == candles

    repository.save.assert_called_once()

    snapshot = repository.save.call_args.args[0]

    assert isinstance(
        snapshot,
        MarketSnapshot,
    )

    assert snapshot.asset == "BTCUSDT"
    assert snapshot.timeframe == 60
    assert snapshot.candles == candles


def test_market_service_persists_snapshot_when_using_cache() -> None:
    candles = [
        create_candle(),
    ]

    collector = Mock()
    cache = Mock()
    repository = Mock()
    validator = Mock()

    cache.load.return_value = candles

    service = MarketService(
        collector=collector,
        cache=cache,
        repository=repository,
        validator=validator,
    )

    result = service.refresh_market(
        asset="BTCUSDT",
        timeframe=60,
        count=1,
    )

    assert result == candles

    collector.collect.assert_not_called()

    repository.save.assert_called_once()


def test_market_service_does_not_persist_invalid_market_data() -> None:
    candles = [
        create_candle(),
    ]

    collector = Mock()
    cache = Mock()
    repository = Mock()
    validator = Mock()

    cache.load.return_value = []
    collector.collect.return_value = candles
    validator.validate.return_value = False

    service = MarketService(
        collector=collector,
        cache=cache,
        repository=repository,
        validator=validator,
    )

    result = service.refresh_market(
        asset="BTCUSDT",
        timeframe=60,
        count=1,
    )

    assert result == []

    repository.save.assert_not_called()