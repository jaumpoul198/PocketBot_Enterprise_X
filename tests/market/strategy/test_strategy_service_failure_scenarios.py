import pytest

from pocketbot.market.strategy.base import BaseStrategy
from pocketbot.market.strategy.models import (
    StrategyResult,
    StrategySignal,
)
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

def test_analyze_handles_none_strategy_instance_failure() -> None:
    service = StrategyService(
        strategies=[
            None,
        ],
    )

    with pytest.raises(
        AttributeError,
    ):
        service.analyze(
            {},
        )


def test_analyze_preserves_strategy_result_order() -> None:
    class FirstStrategy(BaseStrategy):

        @property
        def name(self) -> str:
            return "first"

        def analyze(
            self,
            market_data,
        ) -> StrategyResult:
            return StrategyResult(
                signal=StrategySignal.BUY,
                confidence=0.8,
                reason="first",
            )


    class SecondStrategy(BaseStrategy):

        @property
        def name(self) -> str:
            return "second"

        def analyze(
            self,
            market_data,
        ) -> StrategyResult:
            return StrategyResult(
                signal=StrategySignal.SELL,
                confidence=0.6,
                reason="second",
            )


    service = StrategyService(
        strategies=[
            FirstStrategy(),
            SecondStrategy(),
        ],
    )

    result = service.analyze(
        {},
    )

    assert len(result) == 2
    assert result[0].reason == "first"
    assert result[1].reason == "second"


def test_analyze_allows_strategy_returning_none() -> None:

    class NoneReturningStrategy(BaseStrategy):

        @property
        def name(self) -> str:
            return "none"

        def analyze(
            self,
            market_data,
        ):
            return None


    service = StrategyService(
        strategies=[
            NoneReturningStrategy(),
        ],
    )

    result = service.analyze(
        {},
    )

    assert result == [None]
