from pocketbot.production.config.settings import ProductionSettings


def test_production_settings_has_defaults() -> None:
    settings = ProductionSettings()

    assert settings.environment is not None
    assert isinstance(settings.environment, str)


def test_production_settings_accepts_explicit_environment() -> None:
    settings = ProductionSettings(environment="production")

    assert settings.environment == "production"


def test_production_settings_accepts_custom_environment() -> None:
    settings = ProductionSettings(environment="staging")

    assert settings.environment == "staging"
