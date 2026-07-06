from pocketbot.infrastructure.container.service_collection import ServiceCollection


class Config:
    def __init__(self) -> None:
        self.name = "PocketBot"


def test_existing_instance_registration() -> None:
    services = ServiceCollection()

    config = Config()

    services.add_instance(Config, config)

    provider = services.build_provider()

    resolved = provider.get_service(Config)

    assert resolved is config