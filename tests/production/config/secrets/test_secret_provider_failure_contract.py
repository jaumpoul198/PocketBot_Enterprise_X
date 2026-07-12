from __future__ import annotations

import pytest

from pocketbot.production.config.secrets.factory import (
    resolve_secret_provider,
)


def test_secret_provider_rejects_unknown_provider() -> None:
    with pytest.raises(ValueError):
        resolve_secret_provider(
            "unknown"
        )


def test_secret_provider_rejects_empty_provider() -> None:
    with pytest.raises(ValueError):
        resolve_secret_provider(
            ""
        )
