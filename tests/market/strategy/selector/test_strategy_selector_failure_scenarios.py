from dataclasses import FrozenInstanceError

import pytest

from pocketbot.market.strategy.selector.models import (
    StrategyRanking,
    StrategyScore,
)
from pocketbot.market.strategy.selector.ranking import (
    StrategyRankingEngine,
)
from pocketbot.market.strategy.selector.selector import (
    StrategySelectorEngine,
)


def test_ranking_handles_empty_scores() -> None:
    engine = StrategyRankingEngine()

    result = engine.rank([])

    assert result == []


def test_ranking_does_not_mutate_original_collection() -> None:
    engine = StrategyRankingEngine()

    scores = [
        StrategyScore(
            strategy_name="slow",
            win_rate=0.50,
        ),
        StrategyScore(
            strategy_name="fast",
            win_rate=0.90,
        ),
    ]

    original = list(scores)

    engine.rank(scores)

    assert scores == original


def test_selector_propagates_empty_selection_failure() -> None:
    selector = StrategySelectorEngine()

    with pytest.raises(
        IndexError,
    ):
        selector.select([])


def test_strategy_score_is_immutable() -> None:
    score = StrategyScore(
        strategy_name="momentum",
        win_rate=0.80,
    )

    with pytest.raises(
        FrozenInstanceError,
    ):
        score.win_rate = 0.90


def test_strategy_ranking_is_immutable() -> None:
    ranking = StrategyRanking(
        scores=[],
    )

    with pytest.raises(
        FrozenInstanceError,
    ):
        ranking.scores = []
def test_selector_rejects_none_ranking_engine() -> None:
    with pytest.raises(
        ValueError,
        match="ranking_engine cannot be None",
    ):
        StrategySelectorEngine(
            ranking_engine=None,
        )


def test_selector_rejects_invalid_ranking_engine_contract() -> None:

    class InvalidRankingEngine:
        pass

    with pytest.raises(
        TypeError,
        match="ranking_engine must provide rank",
    ):
        StrategySelectorEngine(
            ranking_engine=InvalidRankingEngine(),
        )


def test_selector_rejects_none_scores() -> None:
    selector = StrategySelectorEngine()

    with pytest.raises(
        ValueError,
        match="scores cannot be None",
    ):
        selector.select(
            None,
        )


def test_ranking_rejects_none_scores() -> None:
    engine = StrategyRankingEngine()

    with pytest.raises(
        ValueError,
        match="scores cannot be None",
    ):
        engine.rank(
            None,
        )
