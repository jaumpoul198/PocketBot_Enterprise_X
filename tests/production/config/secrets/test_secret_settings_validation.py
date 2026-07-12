from pocketbot.production.config.secrets.settings import SecretSettings


def test_secret_settings_accepts_empty_provider() -> None:
    settings = SecretSettings(provider="")

    assert settings.provider == ""


def test_secret_settings_accepts_none_provider() -> None:
    settings = SecretSettings(provider=None)

    assert settings.provider is None


def test_secret_settings_preserves_valid_provider() -> None:
    settings = SecretSettings(provider="docker")

    assert settings.provider == "docker"
