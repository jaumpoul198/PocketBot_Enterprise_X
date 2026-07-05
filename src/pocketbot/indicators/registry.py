"""
PocketBot Enterprise X

Indicator Registry.
"""

from __future__ import annotations

from collections.abc import Iterator

from pocketbot.indicators.base.indicator import Indicator


class IndicatorRegistry:
    """
    Stores all available indicator classes.
    """

    def __init__(self) -> None:
        self._registry: dict[str, type[Indicator]] = {}

    def register(
        self,
        name: str,
        indicator: type[Indicator],
    ) -> None:
        """
        Registers an indicator class.
        """

        key = name.upper()

        if key in self._registry:
            raise ValueError(
                f"Indicator '{name}' is already registered."
            )

        self._registry[key] = indicator

    def get(
        self,
        name: str,
    ) -> type[Indicator]:
        """
        Returns an indicator class.
        """

        key = name.upper()

        try:
            return self._registry[key]

        except KeyError as exc:
            raise KeyError(
                f"Indicator '{name}' is not registered."
            ) from exc

    def exists(
        self,
        name: str,
    ) -> bool:
        """
        Checks whether an indicator is registered.
        """

        return name.upper() in self._registry

    def names(self) -> list[str]:
        """
        Returns all registered indicator names.
        """

        return sorted(self._registry.keys())

    def __len__(self) -> int:
        return len(self._registry)

    def __iter__(self) -> Iterator[type[Indicator]]:
        return iter(self._registry.values())