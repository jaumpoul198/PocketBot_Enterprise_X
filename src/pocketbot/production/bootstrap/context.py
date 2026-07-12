from __future__ import annotations

from dataclasses import dataclass

from pocketbot.production.logging.logger import create_production_logger
from pocketbot.production.observability.metrics import ProductionMetrics


@dataclass
class ProductionContext:
    logger: object
    metrics: ProductionMetrics


def create_production_context() -> ProductionContext:
    return ProductionContext(
        logger=create_production_logger(),
        metrics=ProductionMetrics(),
    )
