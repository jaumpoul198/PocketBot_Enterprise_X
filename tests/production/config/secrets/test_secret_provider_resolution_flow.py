  GNU nano 9.0                                                tests/production/config/secrets/test_secret_provider_resolution_flow.py                                                 Modified
from pocketbot.production.config.secrets.docker import DockerSecretProvider
from pocketbot.production.config.secrets.environment import EnvironmentSecretProvider
from pocketbot.production.config.secrets.resolver import resolve_secret_provider
from pocketbot.production.config.secrets.provider import SecretProvider
from pocketbot.production.config.secrets.settings import SecretSettings


def test_resolver_returns_default_provider() -> None:
    provider = resolve_secret_provider()

    assert isinstance(provider, SecretProvider)


def test_resolver_explicit_environment_provider() -> None:
    settings = SecretSettings(provider="environment")

    provider = resolve_secret_provider(settings)

    assert isinstance(provider, EnvironmentSecretProvider)


def test_resolver_explicit_docker_provider() -> None:
    settings = SecretSettings(provider="docker")

    provider = resolve_secret_provider(settings)


