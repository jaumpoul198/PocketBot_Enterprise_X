from __future__ import annotations

from .base import EnvironmentConfig
from .development import development_environment
from .production import production_environment


_ENVIRONMENTS: dict[str, EnvironmentConfig] = {
    development_environment.name: development_environment,
    production_environment.name: production_environment,
}


def resolve_environment(name: str | None) -> EnvironmentConfig:
    environment_name = (name or "production").lower()

    if environment_name in _ENVIRONMENTS:
        return _ENVIRONMENTS[environment_name]

    return EnvironmentConfig(
        name=environment_name,
        debug=False,
        testing=False,
    )
