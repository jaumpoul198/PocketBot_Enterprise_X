from pocketbot.infrastructure.container.service_collection import ServiceCollection


class Database:
    pass


class Repository:
    def __init__(self, database: Database) -> None:
        self.database = database


class Service:
    def __init__(self, repository: Repository) -> None:
        self.repository = repository


def test_recursive_dependency_resolution() -> None:
    services = ServiceCollection()

    services.add_transient(Database)
    services.add_transient(Repository)
    services.add_transient(Service)

    provider = services.build_provider()

    service = provider.get_service(Service)

    assert isinstance(service.repository, Repository)
    assert isinstance(service.repository.database, Database)