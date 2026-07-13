from unittest.mock import Mock

import pytest

from pocketbot.trading.services.trading_decision_recorder import (
    TradingDecisionRecorder,
)


def test_record_propagates_repository_failure() -> None:
    repository = Mock()

    repository.save.side_effect = RuntimeError(
        "repository unavailable",
    )

    recorder = TradingDecisionRecorder(
        repository,
    )

    with pytest.raises(
        RuntimeError,
        match="repository unavailable",
    ):
        recorder.record(Mock())
