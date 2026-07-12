from pocketbot.production.config.secrets.docker import (
    DockerSecretProvider,
)
from pocketbot.production.config.secrets.environment import (
    EnvironmentSecretProvider,
)
from pocketbot.production.config.secrets.provider import (
    SecretProvider,
)


def resolve_secret_provider() -> SecretProvider:
    """
    Resolve enterprise secret provider.

    Priority:
    1. Docker secrets
    2. Environment variables
    """

    docker_provider = DockerSecretProvider()

    if docker_provider.get_secret(
        "POCKETBOT_ENV"
    ) is not None:
        return docker_provider

    return EnvironmentSecretProvider()
