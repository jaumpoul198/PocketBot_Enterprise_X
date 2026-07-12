from pocketbot.production.bootstrap.factory import (
    create_production_runtime_context,
)
from pocketbot.production.entrypoint.error_boundary import (
    ProductionErrorBoundary,
)


def test_error_boundary_success() -> None:
    runtime_context = create_production_runtime_context()

    boundary = ProductionErrorBoundary(
        runtime_context,
    )

    assert boundary.execute(
        lambda: True,
    ) is True


def test_error_boundary_failure() -> None:
    runtime_context = create_production_runtime_context()

    boundary = ProductionErrorBoundary(
        runtime_context,
    )

    assert boundary.execute(
        lambda: 1 / 0,
    ) is False

    assert (
        runtime_context.context.metrics.get("errors")
        == 1
    )
