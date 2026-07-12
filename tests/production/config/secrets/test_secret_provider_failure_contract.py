from __future__ import annotations

import pytest

from pocketbot.production.config.secrets.factory import (
    resolve_secret_provider,
)
from pocketbot.production.config.secrets.settings import (
    SecretSettings,
)


def test_secret_provider_rejects_unknown_provider() -> None:
    settings = SecretSettings(
        provider="unknown",
    )

    with pytest.raises(ValueError):
        resolve_secret_provider(settings)


def test_secret_provider_rejects_empty_provider() -> None:
    settings = SecretSettings(
        provider="",
    )

    with pytest.raises(ValueError):
        resolve_secret_provider(settings)
