"""
PocketBot Enterprise X

Market analytics failure scenario tests.
"""

from __future__ import annotations

import pytest

from pocketbot.market.analytics.analytics_service import (
    AnalyticsService,
)


class FailingIndicator:
    """
    Indicator that raises an unexpected failure.
    """

    def calculate(
        self,
        candles,
    ):
        raise RuntimeError(
            "indicator failure"
        )


class NoneIndicator:
    """
    Indicator returning no value.
    """

    def calculate(
        self,
        candles,
    ):
        return None


class FirstIndicator:
    """
    First successful indicator.
    """

    def calculate(
        self,
        candles,
    ):
        return 100


class SecondIndicator:
    """
    Second successful indicator.
    """

    def calculate(
        self,
        candles,
    ):
        return 200


def test_empty_indicator_collection_returns_empty_snapshot() -> None:
    service = AnalyticsService(
        indicators=[],
    )

    result = service.analyze(
        candles=[],
    )

    assert result.values == {}


def test_indicator_failure_is_propagated() -> None:
    service = AnalyticsService(
        indicators=[
            FailingIndicator(),
        ],
    )

    with pytest.raises(
        RuntimeError,
        match="indicator failure",
    ):
        service.analyze(
            candles=[],
        )


def test_indicator_returning_none_is_preserved() -> None:
    service = AnalyticsService(
        indicators=[
            NoneIndicator(),
        ],
    )

    result = service.analyze(
        candles=[],
    )

    assert result.values[
        "NoneIndicator"
    ] is None


def test_multiple_indicators_are_executed_independently() -> None:
    service = AnalyticsService(
        indicators=[
            FirstIndicator(),
            SecondIndicator(),
        ],
    )

    result = service.analyze(
        candles=[],
    )

    assert result.values[
        "FirstIndicator"
    ] == 100

    assert result.values[
        "SecondIndicator"
    ] == 200


def test_empty_candles_are_supported_by_service() -> None:
    service = AnalyticsService(
        indicators=[
            FirstIndicator(),
        ],
    )

    result = service.analyze(
        candles=[],
    )

    assert result.values[
        "FirstIndicator"
    ] == 100
