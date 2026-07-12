from pathlib import Path

from pocketbot.production.config.secrets.provider import SecretProvider


class DockerSecretProvider(SecretProvider):
    """
    Secret provider backed by Docker secrets.

    Docker mounts secrets by default under:
    /run/secrets/<secret_name>
    """

    def __init__(
        self,
        secrets_path: str = "/run/secrets",
    ) -> None:
        self._secrets_path = Path(secrets_path)

    def get_secret(self, key: str) -> str | None:
        secret_file = self._secrets_path / key

        if not secret_file.exists():
            return None

        return secret_file.read_text(
            encoding="utf-8",
        ).strip()
