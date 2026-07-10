from pocketbot.application.flows.trading_flow import (
    TradingApplicationFlow,
)
from pocketbot.bootstrap.builder import (
    ApplicationBuilder,
)


def test_trading_application_flow_resolves_from_container() -> None:

    provider = (
        ApplicationBuilder()
        .build()
    )

    flow = provider.get_service(
        TradingApplicationFlow,
    )

    assert isinstance(
        flow,
        TradingApplicationFlow,
    )
