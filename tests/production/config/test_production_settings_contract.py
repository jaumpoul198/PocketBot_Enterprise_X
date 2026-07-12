from pocketbot.production.config.settings import ProductionSettings


def test_production_settings_can_be_created() -> None:
    settings = ProductionSettings()

    assert settings is not None


def test_production_settings_exposes_environment() -> None:
    settings = ProductionSettings()

    assert hasattr(settings, "environment")


def test_production_settings_environment_is_string() -> None:
    settings = ProductionSettings()

    assert isinstance(settings.environment, str)
