from pocketbot.production.config.secrets import (
    EnvironmentSecretProvider,
    SecretProvider,
)


def test_environment_secret_provider_reads_environment_variable(
    monkeypatch,
) -> None:
    monkeypatch.setenv("POCKETBOT_TEST_SECRET", "secret-value")

    provider = EnvironmentSecretProvider()

    assert provider.get_secret("POCKETBOT_TEST_SECRET") == "secret-value"


def test_environment_secret_provider_returns_none_when_missing() -> None:
    provider = EnvironmentSecretProvider()

    assert provider.get_secret("UNKNOWN_SECRET") is None


def test_environment_secret_provider_implements_contract() -> None:
    provider = EnvironmentSecretProvider()

    assert isinstance(provider, SecretProvider)
