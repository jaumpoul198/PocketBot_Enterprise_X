from pocketbot.production.config.secrets.docker import DockerSecretProvider
from pocketbot.production.config.secrets.environment import EnvironmentSecretProvider


def test_environment_and_docker_providers_are_independent() -> None:
    environment_provider = EnvironmentSecretProvider()
    docker_provider = DockerSecretProvider()

    assert environment_provider is not docker_provider


def test_providers_do_not_share_internal_state() -> None:
    environment_provider = EnvironmentSecretProvider()
    docker_provider = DockerSecretProvider()

    assert environment_provider.__dict__ != docker_provider.__dict__
