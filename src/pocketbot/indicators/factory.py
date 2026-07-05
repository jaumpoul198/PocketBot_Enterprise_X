"""
PocketBot Enterprise X

Indicator Factory.
"""

from __future__ import annotations

from pocketbot.indicators.base.indicator import Indicator
from pocketbot.indicators.registry import IndicatorRegistry


class IndicatorFactory:
    """
    Responsável por criar instâncias de indicadores registrados.
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
        Cria uma instância de um indicador.
        """

        indicator_class = self._registry.get(name)

        instance = indicator_class(**kwargs)

        return instance
