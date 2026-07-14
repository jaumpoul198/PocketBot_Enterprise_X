from pocketbot.production.config.environments import (
    EnvironmentConfig,
    development_environment,
    production_environment,
)


def test_development_environment_configuration():
    assert isinstance(development_environment, EnvironmentConfig)
    assert development_environment.name == "development"
    assert development_environment.debug is True
    assert development_environment.testing is True


def test_production_environment_configuration():
    assert isinstance(production_environment, EnvironmentConfig)
    assert production_environment.name == "production"
    assert production_environment.debug is False
    assert production_environment.testing is False


def test_environment_configuration_is_immutable():
    try:
        production_environment.name = "invalid"
    except Exception:
        return

    raise AssertionError("EnvironmentConfig must be immutable")
