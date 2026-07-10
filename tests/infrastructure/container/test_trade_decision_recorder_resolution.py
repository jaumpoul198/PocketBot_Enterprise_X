"""
PocketBot Enterprise X

Trade decision recorder container resolution test.
"""

from pocketbot.bootstrap.builder import (
    ApplicationBuilder,
)
from pocketbot.trading.services.trading_decision_recorder import (
    TradingDecisionRecorder,
)


def test_trade_decision_recorder_resolves_from_container() -> None:

    provider = (
        ApplicationBuilder()
        .build()
    )

    recorder = provider.get_service(
        TradingDecisionRecorder,
    )

    assert isinstance(
        recorder,
        TradingDecisionRecorder,
    )
