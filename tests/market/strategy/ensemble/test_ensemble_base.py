import pytest

from pocketbot.market.strategy.ensemble.base import BaseStrategyEnsemble


def test_base_strategy_ensemble_is_abstract() -> None:
    with pytest.raises(TypeError):
        BaseStrategyEnsemble()
