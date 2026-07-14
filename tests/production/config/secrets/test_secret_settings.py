from pocketbot.production.config.secrets.settings import (
    SecretSettings,
)


def test_secret_settings_default_provider() -> None:
    settings = SecretSettings()

    assert settings.provider == "environment"


def test_secret_settings_accepts_custom_provider() -> None:
    settings = SecretSettings(
        provider="docker",
    )

    assert settings.provider == "docker"
