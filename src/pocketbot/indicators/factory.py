"""
PocketBot Enterprise X

Indicator Factory.
"""

from __future__ import annotations

from pocketbot.indicators.base.indicator import Indicator
from pocketbot.indicators.registry import IndicatorRegistry


class IndicatorFactory:
    """
    Factory responsável por criar instâncias
    dos indicadores registrados.
    """

    def __init__(
        self,
        registry: IndicatorRegistry,
    ) -> None:
        self._registry = registry

    def create(
        self,
        name: str,
        **kwargs: object,
    ) -> Indicator:
        """
        Cria uma instância do indicador.
        """

        indicator_class = self._registry.get(name)

        return indicator_class(**kwargs)
