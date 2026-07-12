from __future__ import annotations

from pocketbot.indicators.registry import IndicatorRegistry


class FakeIndicator:
    pass


def test_indicator_registry_iterator_isolated_from_internal_state() -> None:
    registry = IndicatorRegistry()

    registry.register(
        "FAKE",
        FakeIndicator,
    )

    values = iter(registry)

    registry.register(
        "SECOND",
        FakeIndicator,
    )

    assert list(values) == [
        FakeIndicator,
    ]
