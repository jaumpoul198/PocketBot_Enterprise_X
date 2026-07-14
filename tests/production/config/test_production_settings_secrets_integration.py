from pocketbot.production.config.settings import ProductionSettings
from pocketbot.production.config.secrets.factory import load_secret_settings


def test_production_settings_can_load_secret_configuration() -> None:
    settings = ProductionSettings()

    secret_settings = load_secret_settings("environment")

    assert settings.environment == "production"
    assert secret_settings.provider == "environment"


def test_production_settings_keeps_secret_configuration_external() -> None:
    settings = ProductionSettings()

    assert not hasattr(settings, "secret_provider")
