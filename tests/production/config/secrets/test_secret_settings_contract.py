from pocketbot.production.config.secrets.settings import SecretSettings


def test_secret_settings_accepts_environment_strategy() -> None:
    settings = SecretSettings(provider="environment")

    assert settings.provider == "environment"


def test_secret_settings_accepts_docker_strategy() -> None:
    settings = SecretSettings(provider="docker")

    assert settings.provider == "docker"


def test_secret_settings_defaults_are_defined() -> None:
    settings = SecretSettings()

    assert settings.provider is not None
    assert isinstance(settings.provider, str)
