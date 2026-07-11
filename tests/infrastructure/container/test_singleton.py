from pocketbot.infrastructure.container.service_collection import ServiceCollection


class Logger:
    pass


def test_singleton_returns_same_instance() -> None:
    services = ServiceCollection()

    services.add_singleton(Logger)

    provider = services.build_provider()

    first = provider.get_service(Logger)
    second = provider.get_service(Logger)

    assert first is second


def test_singleton_created_only_once() -> None:
    counter = 0

    class Service:
        def __init__(self) -> None:
            nonlocal counter
            counter += 1

    services = ServiceCollection()

    services.add_singleton(Service)

    provider = services.build_provider()

    provider.get_service(Service)
    provider.get_service(Service)
    provider.get_service(Service)

    assert counter == 1