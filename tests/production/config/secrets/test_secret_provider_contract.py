from abc import ABC

import pytest

from pocketbot.production.config.secrets.provider import SecretProvider
from pocketbot.production.config.secrets.environment import EnvironmentSecretProvider
from pocketbot.production.config.secrets.docker import DockerSecretProvider


@pytest.mark.parametrize(
    "provider_cls",
    [
        EnvironmentSecretProvider,
        DockerSecretProvider,
    ],
)
def test_secret_provider_contract(provider_cls: type[SecretProvider]) -> None:
    provider = provider_cls()

    assert isinstance(provider, SecretProvider)

    result = provider.get_secret("missing-secret")

    assert result is None or isinstance(result, str)


def test_secret_provider_is_abstract() -> None:
    assert issubclass(SecretProvider, ABC)
