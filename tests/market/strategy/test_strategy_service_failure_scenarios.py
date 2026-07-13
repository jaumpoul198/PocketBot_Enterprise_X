import pytest

from pocketbot.market.strategy.base import BaseStrategy
from pocketbot.market.strategy.models import StrategyResult
from pocketbot.market.strategy.service import StrategyService
from pocketbot.market.strategy.selector.models import StrategyScore


class FailingStrategy(BaseStrategy):

    @property
    def name(self) -> str:
        return "failing"

    def analyze(
        self,
        market_data,
    ) -> StrategyResult:
        raise RuntimeError(
            "strategy analysis failed",
        )


class EmptyStrategy(BaseStrategy):

    @property
    def name(self) -> str:
        return "empty"

    def analyze(
        self,
        market_data,
    ) -> StrategyResult:
        raise ValueError(
            "invalid market data",
        )


def test_analyze_propagates_strategy_failure() -> None:
    service = StrategyService(
        strategies=[
            FailingStrategy(),
        ],
    )

    with pytest.raises(
        RuntimeError,
        match="strategy analysis failed",
    ):
        service.analyze({})


def test_analyze_stops_when_strategy_execution_fails() -> None:
    service = StrategyService(
        strategies=[
            FailingStrategy(),
        ],
    )

    with pytest.raises(RuntimeError):
        service.analyze(
            None,
        )


def test_select_best_strategy_propagates_selector_failure() -> None:
    service = StrategyService(
        strategies=[],
    )

    with pytest.raises(
        IndexError,
    ):
        service.select_best_strategy(
            [],
        )

def test_analyze_with_no_strategies_returns_empty_list() -> None:
    service = StrategyService(
        strategies=[],
    )

    result = service.analyze(
        {},
    )

    assert result == []
