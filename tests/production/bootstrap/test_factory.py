from pocketbot.production.bootstrap.factory import (
    create_production_runtime_context,
)


def test_create_production_runtime_context() -> None:
    runtime_context = create_production_runtime_context()

    assert runtime_context.context.logger.name == "pocketbot"
    assert runtime_context.context.metrics.get("missing") == 0
