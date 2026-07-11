from pocketbot.market.strategy.mean_reversion import MeanReversionStrategy
from pocketbot.market.strategy.models import StrategySignal


def test_mean_reversion_buy_signal() -> None:
    strategy = MeanReversionStrategy()

    result = strategy.analyze(
        {
            "price": 95.0,
            "bollinger_lower": 95.0,
            "bollinger_upper": 105.0,
        }
    )

    assert result.signal == StrategySignal.BUY
    assert result.confidence == 0.8
    assert result.reason == "Price reached lower Bollinger Band"


def test_mean_reversion_sell_signal() -> None:
    strategy = MeanReversionStrategy()

    result = strategy.analyze(
        {
            "price": 105.0,
            "bollinger_lower": 95.0,
            "bollinger_upper": 105.0,
        }
    )

    assert result.signal == StrategySignal.SELL
    assert result.confidence == 0.8
    assert result.reason == "Price reached upper Bollinger Band"


def test_mean_reversion_hold_signal() -> None:
    strategy = MeanReversionStrategy()

    result = strategy.analyze(
        {
            "price": 100.0,
            "bollinger_lower": 95.0,
            "bollinger_upper": 105.0,
        }
    )

    assert result.signal == StrategySignal.HOLD
    assert result.confidence == 0.5
    assert result.reason == "Price within Bollinger Bands"


def test_mean_reversion_missing_indicators() -> None:
    strategy = MeanReversionStrategy()

    result = strategy.analyze(
        {
            "price": 100.0,
        }
    )

    assert result.signal == StrategySignal.HOLD
    assert result.confidence == 0.0
    assert result.reason == "Missing Bollinger Band indicators"
