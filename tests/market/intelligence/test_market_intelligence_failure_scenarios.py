from datetime import UTC, datetime

import pytest
from unittest.mock import Mock

from pocketbot.domain.candle import Candle
from pocketbot.domain.value_objects.price import Price
from pocketbot.market.intelligence.market_analysis_service import (
    MarketAnalysisService,
)
from pocketbot.market.intelligence.market_history_service import (
    MarketHistoryService,
)
from pocketbot.market.intelligence.market_state_service import (
    MarketStateService,
)
from pocketbot.market.models.market_snapshot import (
    MarketSnapshot,
)


def create_snapshot(
    price: float,
) -> MarketSnapshot:

    candle = Candle(
        symbol="BTCUSDT",
        timeframe="60",
        open=Price(price),
        high=Price(price),
        low=Price(price),
        close=Price(price),
        volume=100,
        timestamp=datetime.now(UTC),
    )

    return MarketSnapshot(
        asset="BTCUSDT",
        timeframe=60,
        candles=[candle],
    )


def test_market_analysis_propagates_analytics_failure() -> None:
    analytics = Mock()

    analytics.analyze.side_effect = RuntimeError(
        "analytics unavailable",
    )

    service = MarketAnalysisService(
        analytics,
    )

    with pytest.raises(
        RuntimeError,
        match="analytics unavailable",
    ):
        service.analyze([])


def test_market_history_propagates_last_n_failure() -> None:
    repository = Mock()

    repository.get_last_n.side_effect = RuntimeError(
        "history unavailable",
    )

    service = MarketHistoryService(
        repository,
    )

    with pytest.raises(
        RuntimeError,
        match="history unavailable",
    ):
        service.get_last_n(
            "BTCUSDT",
            60,
            10,
        )


def test_market_history_propagates_between_failure() -> None:
    repository = Mock()

    repository.get_between.side_effect = RuntimeError(
        "range unavailable",
    )

    service = MarketHistoryService(
        repository,
    )

    with pytest.raises(
        RuntimeError,
        match="range unavailable",
    ):
        service.get_between(
            "BTCUSDT",
            60,
            datetime.now(UTC),
            datetime.now(UTC),
        )


def test_market_state_returns_sideways_when_prices_equal() -> None:
    repository = Mock()

    repository.get_last_n.return_value = [
        create_snapshot(100),
        create_snapshot(100),
    ]

    service = MarketStateService(
        repository,
    )

    result = service.get_current_state(
        "BTCUSDT",
        60,
    )

    assert result is not None
    assert result.trend == "SIDEWAYS"
    assert result.change_percent == 0


def test_market_state_propagates_repository_failure() -> None:
    repository = Mock()

    repository.get_last_n.side_effect = RuntimeError(
        "repository unavailable",
    )

    service = MarketStateService(
        repository,
    )

    with pytest.raises(
        RuntimeError,
        match="repository unavailable",
    ):
        service.get_current_state(
            "BTCUSDT",
            60,
        )

def test_market_state_returns_none_when_latest_candle_missing() -> None:
    repository = Mock()

    latest = Mock()
    latest.last_candle = None

    previous = create_snapshot(100)

    repository.get_last_n.return_value = [
        latest,
        previous,
    ]

    service = MarketStateService(
        repository,
    )

    result = service.get_current_state(
        "BTCUSDT",
        60,
    )

    assert result is None


def test_market_state_returns_none_when_previous_candle_missing() -> None:
    repository = Mock()

    latest = create_snapshot(100)

    previous = Mock()
    previous.last_candle = None

    repository.get_last_n.return_value = [
        latest,
        previous,
    ]

    service = MarketStateService(
        repository,
    )

    result = service.get_current_state(
        "BTCUSDT",
        60,
    )

    assert result is None
