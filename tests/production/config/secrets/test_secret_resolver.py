from pocketbot.production.config.secrets import (
    DockerSecretProvider,
    EnvironmentSecretProvider,
)
from pocketbot.production.config.secrets.resolver import (
    resolve_secret_provider,
)
from pocketbot.production.config.secrets.settings import (
    SecretSettings,
)


def test_resolver_returns_environment_provider() -> None:
    provider = resolve_secret_provider(
        SecretSettings(
            provider="environment",
        ),
    )

    assert isinstance(
        provider,
        EnvironmentSecretProvider,
    )


def test_resolver_returns_docker_provider() -> None:
    provider = resolve_secret_provider(
        SecretSettings(
            provider="docker",
        ),
    )

    assert isinstance(
        provider,
        DockerSecretProvider,
    )
