import math

from pocketbot.market.strategy.mean_reversion import MeanReversionStrategy
from pocketbot.market.strategy.models import StrategySignal


def test_mean_reversion_rejects_none_data() -> None:
    strategy = MeanReversionStrategy()

    result = strategy.analyze(None)

    assert result.signal == StrategySignal.HOLD
    assert result.confidence == 0.0


def test_mean_reversion_rejects_non_dict_data() -> None:
    strategy = MeanReversionStrategy()

    result = strategy.analyze(["price", 100])

    assert result.signal == StrategySignal.HOLD
    assert result.confidence == 0.0


def test_mean_reversion_rejects_string_price() -> None:
    strategy = MeanReversionStrategy()

    result = strategy.analyze(
        {
            "price": "100",
            "bollinger_lower": 90.0,
            "bollinger_upper": 110.0,
        }
    )

    assert result.signal == StrategySignal.HOLD
    assert result.confidence == 0.0


def test_mean_reversion_rejects_boolean_price() -> None:
    strategy = MeanReversionStrategy()

    result = strategy.analyze(
        {
            "price": True,
            "bollinger_lower": 90.0,
            "bollinger_upper": 110.0,
        }
    )

    assert result.signal == StrategySignal.HOLD
    assert result.confidence == 0.0


def test_mean_reversion_rejects_nan_values() -> None:
    strategy = MeanReversionStrategy()

    result = strategy.analyze(
        {
            "price": math.nan,
            "bollinger_lower": 90.0,
            "bollinger_upper": 110.0,
        }
    )

    assert result.signal == StrategySignal.HOLD
    assert result.confidence == 0.0


def test_mean_reversion_rejects_infinite_values() -> None:
    strategy = MeanReversionStrategy()

    result = strategy.analyze(
        {
            "price": math.inf,
            "bollinger_lower": 90.0,
            "bollinger_upper": 110.0,
        }
    )

    assert result.signal == StrategySignal.HOLD
    assert result.confidence == 0.0
