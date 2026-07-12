from pocketbot.production.config.secrets.settings import (
    SecretSettings,
)


def load_secret_settings(
    secret_provider_value: str | None,
) -> SecretSettings:
    """
    Load secret provider strategy settings.

    Supported providers:
    - environment
    - docker

    Unknown values fallback to environment.
    """

    if secret_provider_value == "docker":
        return SecretSettings(
            provider="docker",
        )

    return SecretSettings(
        provider="environment",
    )
