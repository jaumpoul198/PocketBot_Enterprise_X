from datetime import UTC, datetime

from pocketbot.domain.candle import Candle
from pocketbot.market.validators.default_market_validator import (
    DefaultMarketValidator,
)


def create_candle() -> Candle:
    return Candle(
        symbol="BTCUSDT",
        timeframe=5,
        timestamp=datetime.now(UTC),
        open=100.0,
        high=110.0,
        low=90.0,
        close=105.0,
        volume=1000.0,
    )


def test_validate_returns_false_for_empty_candle_list() -> None:
    validator = DefaultMarketValidator()

    result = validator.validate(
        [],
    )

    assert result is False


def test_validate_returns_false_when_list_contains_none() -> None:
    validator = DefaultMarketValidator()

    candles = [
        create_candle(),
        None,
    ]

    result = validator.validate(
        candles,  # type: ignore[arg-type]
    )

    assert result is False


def test_validate_returns_true_for_valid_candles() -> None:
    validator = DefaultMarketValidator()

    result = validator.validate(
        [
            create_candle(),
            create_candle(),
        ],
    )

    assert result is True


def test_validate_does_not_mutate_input_collection() -> None:
    validator = DefaultMarketValidator()

    candles = [
        create_candle(),
    ]

    original = list(candles)

    validator.validate(
        candles,
    )

    assert candles == original
