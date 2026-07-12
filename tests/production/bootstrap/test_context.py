from pocketbot.production.bootstrap.context import (
    create_production_context,
)


def test_create_production_context() -> None:
    context = create_production_context()

    assert context.logger.name == "pocketbot"
    assert context.metrics.get("missing") == 0
