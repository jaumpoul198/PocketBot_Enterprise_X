from pocketbot.production.config.secrets.factory import load_secret_settings
from pocketbot.production.config.secrets.provider import SecretProvider
from pocketbot.production.config.secrets.resolver import resolve_secret_provider


def test_secret_provider_end_to_end_flow() -> None:
    settings = load_secret_settings("environment")

    provider = resolve_secret_provider(settings)

    assert isinstance(provider, SecretProvider)

    result = provider.get_secret("integration-test")

    assert result is None or isinstance(result, str)


def test_factory_strategy_matches_resolved_provider() -> None:
    settings = load_secret_settings("docker")

    provider = resolve_secret_provider(settings)

    assert isinstance(provider, SecretProvider)
