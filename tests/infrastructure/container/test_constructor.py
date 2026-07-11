from pocketbot.infrastructure.container.service_collection import ServiceCollection


class Repository:
    pass


class Service:
    def __init__(self, repository: Repository) -> None:
        self.repository = repository


def test_constructor_injection() -> None:
    services = ServiceCollection()

    services.add_transient(Repository)
    services.add_transient(Service)

    provider = services.build_provider()

    service = provider.get_service(Service)

    assert isinstance(service, Service)
    assert isinstance(service.repository, Repository)