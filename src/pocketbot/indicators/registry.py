"""
PocketBot Enterprise X

Indicator Registry.
"""

from __future__ import annotations

from pocketbot.indicators.base.indicator import Indicator


class IndicatorRegistry:
    """
    Registry responsável por armazenar todos os indicadores
    disponíveis no sistema.
    """

    def __init__(self) -> None:
        self._registry: dict[str, type[Indicator]] = {}

    def register(
        self,
        indicator: type[Indicator],
    ) -> None:
        """
        Registra um indicador.
        """

        name = indicator.__name__

        if name in self._registry:
            raise ValueError(f"Indicator '{name}' already registered.")

        self._registry[name] = indicator

    def unregister(
        self,
        name: str,
    ) -> None:
        """
        Remove um indicador.
        """

        self._registry.pop(name, None)

    def get(
        self,
        name: str,
    ) -> type[Indicator]:
        """
        Obtém um indicador pelo nome.
        """

        try:
            return self._registry[name]
        except KeyError as exc:
            raise ValueError(f"Indicator '{name}' not found.") from exc

    def exists(
        self,
        name: str,
    ) -> bool:
        """
        Verifica se existe.
        """

        return name in self._registry

    def all(
        self,
    ) -> dict[str, type[Indicator]]:
        """
        Retorna todos os indicadores.
        """

        return dict(self._registry)

    def clear(self) -> None:
        """
        Limpa o registry.
        """

        self._registry.clear()

    def __len__(self) -> int:
        return len(self._registry)
