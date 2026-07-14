from pathlib import Path

from pocketbot.production.config.secrets import (
    DockerSecretProvider,
)


def test_docker_secret_provider_reads_secret_file(
    tmp_path: Path,
) -> None:
    secret_file = tmp_path / "DATABASE_PASSWORD"
    secret_file.write_text(
        "docker-secret\n",
        encoding="utf-8",
    )

    provider = DockerSecretProvider(
        secrets_path=str(tmp_path),
    )

    assert (
        provider.get_secret("DATABASE_PASSWORD")
        == "docker-secret"
    )


def test_docker_secret_provider_returns_none_when_missing(
    tmp_path: Path,
) -> None:
    provider = DockerSecretProvider(
        secrets_path=str(tmp_path),
    )

    assert provider.get_secret("UNKNOWN") is None
