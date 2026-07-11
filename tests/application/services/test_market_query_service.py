from datetime import UTC, datetime
from unittest.mock import Mock

from pocketbot.application.services.market_query_service import (
    MarketQueryService,
)
from pocketbot.market.models.market_snapshot import MarketSnapshot


def create_snapshot() -> MarketSnapshot:
    return MarketSnapshot(
        asset="BTCUSDT",
        timeframe=5,
        timestamp=datetime.now(UTC),
        provider="test",
        connected=True,
    )


def test_market_query_service_returns_latest_snapshot() -> None:
    repository = Mock()

    snapshot = create_snapshot()

    repository.get_latest.return_value = snapshot

    service = MarketQueryService(
        repository=repository,
    )

    result = service.get_latest_market(
        asset="BTCUSDT",
        timeframe=5,
    )

    assert result == snapshot

    repository.get_latest.assert_called_once_with(
        "BTCUSDT",
        5,
    )


def test_market_query_service_returns_none_when_snapshot_missing() -> None:
    repository = Mock()

    repository.get_latest.return_value = None

    service = MarketQueryService(
        repository=repository,
    )

    result = service.get_latest_market(
        asset="BTCUSDT",
        timeframe=5,
    )

    assert result is None