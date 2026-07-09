from pocketbot.application.pipeline.protocols import (
    TradingPipelineProtocol,
)


def test_protocol_exists() -> None:
    assert TradingPipelineProtocol is not None
