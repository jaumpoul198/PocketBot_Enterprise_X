import os

from pocketbot.production.config.secrets.provider import SecretProvider


class EnvironmentSecretProvider(SecretProvider):
    """
    Secret provider backed by environment variables.

    Keeps compatibility with current runtime while
    preparing enterprise secret backends.
    """

    def get_secret(self, key: str) -> str | None:
        return os.getenv(key)
