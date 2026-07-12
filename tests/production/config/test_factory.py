from pocketbot.production.config.factory import load_production_settings


def test_load_production_settings_defaults(monkeypatch) -> None:
    monkeypatch.delenv("POCKETBOT_ENV", raising=False)
    monkeypatch.delenv("POCKETBOT_DEBUG", raising=False)
    monkeypatch.delenv("POCKETBOT_SERVICE_NAME", raising=False)

    settings = load_production_settings()

    assert settings.environment == "production"
    assert settings.debug is False
    assert settings.service_name == "pocketbot"


def test_load_production_settings_from_environment(monkeypatch) -> None:
    monkeypatch.setenv("POCKETBOT_ENV", "staging")
    monkeypatch.setenv("POCKETBOT_DEBUG", "true")
    monkeypatch.setenv("POCKETBOT_SERVICE_NAME", "enterprise")

    settings = load_production_settings()

    assert settings.environment == "staging"
    assert settings.debug is True
    assert settings.service_name == "enterprise"
