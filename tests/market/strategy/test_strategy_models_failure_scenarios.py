import pytest

from pocketbot.market.strategy.models import (
    StrategyResult,
    StrategySignal,
)


def test_strategy_result_rejects_invalid_confidence_above_range() -> None:
    with pytest.raises(ValueError):
        StrategyResult(
            signal=StrategySignal.BUY,
            confidence=1.5,
            reason="invalid",
        )


def test_strategy_result_rejects_negative_confidence() -> None:
    with pytest.raises(ValueError):
        StrategyResult(
            signal=StrategySignal.BUY,
            confidence=-0.1,
            reason="invalid",
        )


def test_strategy_result_rejects_non_numeric_confidence() -> None:
    with pytest.raises(TypeError):
        StrategyResult(
            signal=StrategySignal.BUY,
            confidence="0.8",
            reason="invalid",
        )


def test_strategy_result_rejects_empty_reason() -> None:
    with pytest.raises(ValueError):
        StrategyResult(
            signal=StrategySignal.BUY,
            confidence=0.8,
            reason="",
        )


def test_strategy_result_rejects_invalid_signal() -> None:
    with pytest.raises(TypeError):
        StrategyResult(
            signal="BUY",
            confidence=0.8,
            reason="invalid",
        )
