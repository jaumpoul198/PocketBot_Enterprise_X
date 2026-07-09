import pytest

from pocketbot.market.strategy.base import BaseStrategy
from pocketbot.market.strategy.models import (
    StrategyResult,
    StrategySignal,
)


def test_base_strategy_cannot_be_instantiated():
    with pytest.raises(TypeError):
        BaseStrategy()


class DummyStrategy(BaseStrategy):

    @property
    def name(self) -> str:
        return "dummy"


    def analyze(self, market_data) -> StrategyResult:
        return StrategyResult(
            signal=StrategySignal.HOLD,
            confidence=0.5,
            reason="test",
        )


def test_strategy_implementation():

    strategy = DummyStrategy()

    result = strategy.analyze({})

    assert strategy.name == "dummy"
    assert result.signal == StrategySignal.HOLD