from pocketbot.production.config.profiles.defaults import get_default_profile
from pocketbot.production.config.settings import ProductionSettings


def test_default_profile_exists() -> None:
    profile = get_default_profile()

    assert profile is not None


def test_default_profile_can_create_settings() -> None:
    profile = get_default_profile()

    settings = ProductionSettings(**profile)

    assert settings is not None


def test_default_profile_environment_is_valid() -> None:
    profile = get_default_profile()

    assert "environment" in profile
    assert isinstance(profile["environment"], str)
