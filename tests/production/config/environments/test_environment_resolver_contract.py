from __future__ import annotations

from pocketbot.production.config.environments import (
    resolve_environment,
)


def test_resolver_defaults_to_production_when_missing() -> None:
    environment = resolve_environment(None)

    assert environment.name == "production"
    assert environment.debug is False


def test_resolver_is_case_insensitive() -> None:
    environment = resolve_environment("PRODUCTION")

    assert environment.name == "production"


def test_resolver_returns_known_development_profile() -> None:
    environment = resolve_environment("development")

    assert environment.name == "development"
    assert environment.debug is True
    assert environment.testing is True


def test_resolver_handles_unknown_environment() -> None:
    environment = resolve_environment("staging")

    assert environment.name == "staging"
    assert environment.debug is False
    assert environment.testing is False
