from pocketbot.production.config.secrets.factory import (
    load_secret_settings,
)


def test_secret_factory_defaults_to_environment() -> None:
    settings = load_secret_settings(None)

    assert settings.provider == "environment"


def test_secret_factory_loads_docker_provider() -> None:
    settings = load_secret_settings(
        "docker",
    )

    assert settings.provider == "docker"


def test_secret_factory_falls_back_for_unknown_provider() -> None:
    settings = load_secret_settings(
        "unknown",
    )

    assert settings.provider == "environment"
