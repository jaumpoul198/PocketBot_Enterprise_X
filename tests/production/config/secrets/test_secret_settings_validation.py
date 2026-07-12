import pytest

from pocketbot.production.config.secrets.settings import SecretSettings


def test_secret_settings_rejects_empty_provider() -> None:
    with pytest.raises(ValueError):
        SecretSettings(provider="")


def test_secret_settings_rejects_none_provider() -> None:
    with pytest.raises(ValueError):
        SecretSettings(provider=None)


def test_secret_settings_preserves_valid_provider() -> None:
    settings = SecretSettings(provider="docker")

    assert settings.provider == "docker"
