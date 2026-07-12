import pytest

from pocketbot.production.config.secrets.docker import DockerSecretProvider
from pocketbot.production.config.secrets.environment import EnvironmentSecretProvider
from pocketbot.production.config.secrets.provider import SecretProvider


@pytest.mark.parametrize(
    "provider",
    [
        EnvironmentSecretProvider(),
        DockerSecretProvider(),
    ],
)
def test_provider_get_secret_contract(provider: SecretProvider) -> None:
    result = provider.get_secret("missing-key")

    assert result is None or isinstance(result, str)


@pytest.mark.parametrize(
    "provider",
    [
        EnvironmentSecretProvider(),
        DockerSecretProvider(),
    ],
)
def test_provider_can_handle_empty_key(provider: SecretProvider) -> None:
    result = provider.get_secret("")

    assert result is None or isinstance(result, str)
