from pocketbot.production.config.factory import (
    load_production_settings,
)


def test_factory_uses_environment_secret_strategy(
    monkeypatch,
) -> None:
    monkeypatch.setenv(
        "POCKETBOT_SECRET_PROVIDER",
        "environment",
    )
    monkeypatch.setenv(
        "POCKETBOT_ENV",
        "development",
    )
    monkeypatch.setenv(
        "POCKETBOT_SERVICE_NAME",
        "strategy-test",
    )

    settings = load_production_settings()

    assert settings.environment == "development"
    assert settings.service_name == "strategy-test"


def test_factory_keeps_default_secret_strategy(
    monkeypatch,
) -> None:
    monkeypatch.delenv(
        "POCKETBOT_SECRET_PROVIDER",
        raising=False,
    )

    settings = load_production_settings()

    assert settings is not None
