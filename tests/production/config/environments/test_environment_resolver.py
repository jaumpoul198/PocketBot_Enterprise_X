from pocketbot.production.config.environments.development import (
    development_environment,
)
from pocketbot.production.config.environments.production import (
    production_environment,
)
from pocketbot.production.config.environments.resolver import (
    resolve_environment,
)


def test_resolve_default_environment() -> None:
    environment = resolve_environment(None)

    assert environment == production_environment


def test_resolve_development_environment() -> None:
    environment = resolve_environment("development")

    assert environment == development_environment
    assert environment.debug is True
    assert environment.testing is True


def test_resolve_unknown_environment_uses_safe_config() -> None:
    environment = resolve_environment("unknown")

    assert environment.name == "unknown"
    assert environment.debug is False
    assert environment.testing is False
