from pocketbot.production.config.settings import ProductionSettings


def test_production_settings_contains_environment_config() -> None:
    settings = ProductionSettings()

    assert settings.environment_config is not None


def test_environment_config_matches_environment() -> None:
    settings = ProductionSettings()

    assert settings.environment_config.name == settings.environment


def test_environment_config_debug_is_consistent() -> None:
    settings = ProductionSettings()

    assert settings.environment_config.debug == settings.debug
