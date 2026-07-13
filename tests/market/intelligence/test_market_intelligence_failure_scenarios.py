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

def test_market_analysis_rejects_none_analytics_service() -> None:
    with pytest.raises(
        ValueError,
        match="analytics_service cannot be None",
    ):
        MarketAnalysisService(
            None,
        )


def test_market_analysis_rejects_invalid_analytics_service_contract() -> None:
    class InvalidAnalyticsService:
        pass

    with pytest.raises(
        TypeError,
        match="analytics_service must provide analyze",
    ):
        MarketAnalysisService(
            InvalidAnalyticsService(),
        )


def test_market_analysis_rejects_none_candles() -> None:
    service = MarketAnalysisService(
        Mock(),
    )

    with pytest.raises(
        ValueError,
        match="candles cannot be None",
    ):
        service.analyze(
            None,
        )


def test_market_analysis_rejects_invalid_candles_type() -> None:
    service = MarketAnalysisService(
        Mock(),
    )

    with pytest.raises(
        TypeError,
        match="candles must be a list",
    ):
        service.analyze(
            "invalid",
        )


def test_market_analysis_rejects_invalid_analytics_result() -> None:
    analytics = Mock()

    analytics.analyze.return_value = None

    service = MarketAnalysisService(
        analytics,
    )

    with pytest.raises(
        TypeError,
        match="analytics result must be AnalyticsSnapshot",
    ):
        service.analyze([])

def test_market_state_rejects_none_repository() -> None:
    with pytest.raises(
        ValueError,
        match="repository cannot be None",
    ):
        MarketStateService(
            None,
        )


def test_market_state_rejects_invalid_repository_contract() -> None:
    class InvalidRepository:
        pass

    with pytest.raises(
        TypeError,
        match="repository must provide get_last_n",
    ):
        MarketStateService(
            InvalidRepository(),
        )


def test_market_state_rejects_none_asset() -> None:
    repository = Mock()

    service = MarketStateService(
        repository,
    )

    with pytest.raises(
        ValueError,
        match="asset cannot be None",
    ):
        service.get_current_state(
            None,
            60,
        )


def test_market_state_rejects_invalid_timeframe_bool() -> None:
    repository = Mock()

    service = MarketStateService(
        repository,
    )

    with pytest.raises(
        TypeError,
        match="timeframe must be an integer",
    ):
        service.get_current_state(
            "BTCUSDT",
            True,
        )


def test_market_state_rejects_zero_previous_price() -> None:
    repository = Mock()

    previous = Mock()
    previous.last_candle.close.value = 0

    latest = Mock()
    latest.last_candle.close.value = 100

    repository.get_last_n.return_value = [
        latest,
        previous,
    ]

    service = MarketStateService(
        repository,
    )

    with pytest.raises(
        ValueError,
        match="previous price cannot be zero",
    ):
        service.get_current_state(
            "BTCUSDT",
            60,
        )

def test_market_state_rejects_nan_price() -> None:
    repository = Mock()

    repository.get_last_n.return_value = [
        create_snapshot(float("nan")),
        create_snapshot(100),
    ]

    service = MarketStateService(
        repository,
    )

    with pytest.raises(
        ValueError,
        match="price must be finite",
    ):
        service.get_current_state(
            "BTCUSDT",
            60,
        )

def test_market_history_rejects_none_repository() -> None:
    with pytest.raises(
        ValueError,
        match="repository cannot be None",
    ):
        MarketHistoryService(
            None,
        )


def test_market_history_rejects_invalid_repository_contract() -> None:
    class InvalidRepository:
        pass

    with pytest.raises(
        TypeError,
        match="repository must provide market history methods",
    ):
        MarketHistoryService(
            InvalidRepository(),
        )


def test_market_history_rejects_none_asset() -> None:
    service = MarketHistoryService(
        Mock(),
    )

    with pytest.raises(
        ValueError,
        match="asset cannot be None",
    ):
        service.get_last_n(
            None,
            60,
            10,
        )


def test_market_history_rejects_invalid_timeframe_bool() -> None:
    service = MarketHistoryService(
        Mock(),
    )

    with pytest.raises(
        TypeError,
        match="timeframe must be an integer",
    ):
        service.get_last_n(
            "BTCUSDT",
            True,
            10,
        )


def test_market_history_rejects_invalid_limit_bool() -> None:
    service = MarketHistoryService(
        Mock(),
    )

    with pytest.raises(
        TypeError,
        match="limit must be an integer",
    ):
        service.get_last_n(
            "BTCUSDT",
            60,
            True,
        )


def test_market_history_rejects_negative_limit() -> None:
    service = MarketHistoryService(
        Mock(),
    )

    with pytest.raises(
        ValueError,
        match="limit must be greater than zero",
    ):
        service.get_last_n(
            "BTCUSDT",
            60,
            -1,
        )


def test_market_history_rejects_invalid_date_range() -> None:
    service = MarketHistoryService(
        Mock(),
    )

    end = datetime.now(UTC)

    with pytest.raises(
        ValueError,
        match="start must be before end",
    ):
        service.get_between(
            "BTCUSDT",
            60,
            end,
            end.replace(
                year=end.year - 1,
            ),
        )
