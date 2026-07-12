from pocketbot.production.config.settings import ProductionSettings


def test_production_settings_defaults() -> None:
    settings = ProductionSettings()

    assert settings.environment == "production"
    assert settings.debug is False
    assert settings.service_name == "pocketbot"
