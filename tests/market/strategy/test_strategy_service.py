from pocketbot.market.strategy.base import BaseStrategy
from pocketbot.market.strategy.models import (
    StrategyResult,
    StrategySignal,
)
from pocketbot.market.strategy.service import StrategyService


class BuyStrategy(BaseStrategy):

    @property
    def name(self) -> str:
        return "buy"


    def analyze(self, market_data) -> StrategyResult:
        return StrategyResult(
            signal=StrategySignal.BUY,
            confidence=0.9,
            reason="buy signal",
        )


class SellStrategy(BaseStrategy):

    @property
    def name(self) -> str:
        return "sell"


    def analyze(self, market_data) -> StrategyResult:
        return StrategyResult(
            signal=StrategySignal.SELL,
            confidence=0.8,
            reason="sell signal",
        )


def test_strategy_service_executes_all_strategies():

    service = StrategyService(
        strategies=[
            BuyStrategy(),
            SellStrategy(),
        ]
    )

    results = service.analyze({})

    assert len(results) == 2
    assert results[0].signal == StrategySignal.BUY
    assert results[1].signal == StrategySignal.SELL
