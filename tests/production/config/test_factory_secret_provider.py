from pocketbot.production.config.factory import (
    load_production_settings,
)
from pocketbot.production.config.secrets import (
    SecretProvider,
)


class FakeSecretProvider(SecretProvider):
    def __init__(self) -> None:
        self.secrets = {
            "POCKETBOT_ENV": "development",
            "POCKETBOT_DEBUG": "true",
            "POCKETBOT_SERVICE_NAME": "secret-service",
        }

    def get_secret(self, key: str) -> str | None:
        return self.secrets.get(key)


def test_factory_uses_injected_secret_provider() -> None:
    provider = FakeSecretProvider()

    settings = load_production_settings(
        secret_provider=provider,
    )

    assert settings.environment == "development"
    assert settings.debug is True
    assert settings.service_name == "secret-service"
