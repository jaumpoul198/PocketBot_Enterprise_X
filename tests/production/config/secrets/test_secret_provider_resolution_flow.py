import pytest

from pocketbot.production.config.secrets.resolver import resolve_secret_provider
from pocketbot.production.config.secrets.settings import SecretSettings


def test_resolver_rejects_unknown_provider() -> None:
    settings = SecretSettings(provider="unknown")

    with pytest.raises(ValueError):
        resolve_secret_provider(settings)
