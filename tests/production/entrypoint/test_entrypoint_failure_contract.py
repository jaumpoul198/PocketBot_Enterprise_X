import pytest

from pocketbot.production.bootstrap.factory import (
    create_production_runtime_context,
)
from pocketbot.production.entrypoint.error_boundary import (
    ProductionErrorBoundary,
)


def test_error_boundary_preserves_failure_isolation() -> None:
    runtime_context = create_production_runtime_context()

    boundary = ProductionErrorBoundary(
        runtime_context,
    )

    result = boundary.execute(
        lambda: (_ for _ in ()).throw(
            RuntimeError("startup failure"),
        ),
    )

    assert result is False

    assert (
        runtime_context.context.metrics.get("errors")
        == 1
    )


def test_error_boundary_handles_runtime_failure() -> None:
    runtime_context = create_production_runtime_context()

    boundary = ProductionErrorBoundary(
        runtime_context,
    )

    def broken_operation() -> bool:
        raise ValueError("broken runtime")

    assert (
        boundary.execute(
            broken_operation,
        )
        is False
    )
