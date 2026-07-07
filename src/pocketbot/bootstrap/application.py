"""
PocketBot Enterprise X

Application Bootstrap.
"""

from __future__ import annotations

from pocketbot.bootstrap.builder import ApplicationBuilder
from pocketbot.bootstrap.indicator_loader import load_indicators
from pocketbot.indicators.engine import IndicatorEngine
from pocketbot.indicators.factory import IndicatorFactory
from pocketbot.indicators.manager import IndicatorManager
from pocketbot.indicators.pipeline import IndicatorPipeline
from pocketbot.infrastructure.container.interfaces import (
    IServiceProvider,
)


def build_application() -> IServiceProvider:
    """
    Builds the complete application container.
    """

    builder = ApplicationBuilder()

    return builder.build()


def build_indicator_pipeline() -> IndicatorPipeline:
    """
    Builds the complete indicator execution pipeline.
    """

    registry = load_indicators()

    factory = IndicatorFactory(registry)

    engine = IndicatorEngine(factory)

    manager = IndicatorManager(engine)

    return IndicatorPipeline(manager)