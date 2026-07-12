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
from pocketbot.production.config.secrets.settings import (
    SecretSettings,
)


def resolve_secret_provider(
    settings: SecretSettings | None = None,
) -> SecretProvider:
    """
    Resolve enterprise secret provider.

    Explicit strategy has priority.
    Automatic detection is fallback.
    """

    if settings is not None:
        if settings.provider == "docker":
            return DockerSecretProvider()

        return EnvironmentSecretProvider()

    docker_path = Path("/run/secrets")

    if docker_path.exists() and any(
        docker_path.iterdir()
    ):
        return DockerSecretProvider(
            secrets_path=str(docker_path),
        )

    return EnvironmentSecretProvider()
