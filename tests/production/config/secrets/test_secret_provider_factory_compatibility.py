from pocketbot.production.config.secrets.docker import DockerSecretProvider
from pocketbot.production.config.secrets.environment import EnvironmentSecretProvider
from pocketbot.production.config.secrets.factory import load_secret_settings
from pocketbot.production.config.secrets.provider import SecretProvider


def test_factory_returns_secret_provider() -> None:
    settings = load_secret_settings()

    assert isinstance(settings.provider, SecretProvider)


def test_registered_providers_are_factory_compatible() -> None:
    providers = [
        EnvironmentSecretProvider(),
        DockerSecretProvider(),
    ]

    for provider in providers:
        assert isinstance(provider, SecretProvider)

        value = provider.get_secret("factory-test")

        assert value is None or isinstance(value, str)
