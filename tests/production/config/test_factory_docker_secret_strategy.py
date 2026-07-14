from pathlib import Path

from pocketbot.production.config.factory import (
    load_production_settings,
)
from pocketbot.production.config.secrets import (
    DockerSecretProvider,
)


def test_factory_supports_docker_secret_strategy(
    monkeypatch,
    tmp_path: Path,
) -> None:
    secret_provider_path = tmp_path / "secrets"

    secret_provider_path.mkdir()

    (secret_provider_path / "POCKETBOT_ENV").write_text(
        "development",
        encoding="utf-8",
    )

    (secret_provider_path / "POCKETBOT_SERVICE_NAME").write_text(
        "docker-service",
        encoding="utf-8",
    )

    monkeypatch.setenv(
        "POCKETBOT_SECRET_PROVIDER",
        "docker",
    )

    provider = DockerSecretProvider(
        secrets_path=str(secret_provider_path),
    )

    settings = load_production_settings(
        secret_provider=provider,
    )

    assert settings.environment == "development"
    assert settings.service_name == "docker-service"
