from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class ProductionError:
    message: str
    recoverable: bool = False


def handle_production_error(
    error: Exception,
) -> ProductionError:
    return ProductionError(
        message=str(error),
        recoverable=False,
    )
