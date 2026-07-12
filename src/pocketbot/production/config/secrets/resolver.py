from pathlib import Path

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

    docker_path = Path("/run/secrets")

    if docker_path.exists() and any(
        docker_path.iterdir()
    ):
        return DockerSecretProvider(
            secrets_path=str(docker_path),
        )

    return EnvironmentSecretProvider()
