from pocketbot.market.strategy.base import BaseStrategy
from pocketbot.market.strategy.models import (
    StrategyResult,
    StrategySignal,
)
from pocketbot.market.strategy.service import StrategyService
from pocketbot.market.strategy.selector.models import StrategyScore


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


def test_strategy_service_selects_best_strategy():

    service = StrategyService(
        strategies=[
            BuyStrategy(),
            SellStrategy(),
        ]
    )

    scores = [
        StrategyScore(
            strategy_name="buy",
            win_rate=0.60,
        ),
        StrategyScore(
            strategy_name="sell",
            win_rate=0.90,
        ),
    ]

    result = service.select_best_strategy(scores)

    assert result.strategy_name == "sell"
    assert result.win_rate == 0.90
