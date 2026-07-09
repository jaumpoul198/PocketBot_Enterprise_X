from pocketbot.application.pipeline.service import (
    TradingPipelineService,
)
from pocketbot.bootstrap.builder import (
    ApplicationBuilder,
)


def test_trading_pipeline_service_resolves_from_container() -> None:
    provider = (
        ApplicationBuilder()
        .build()
    )

    service = provider.get_service(
        TradingPipelineService,
    )

    assert isinstance(
        service,
        TradingPipelineService,
    )
