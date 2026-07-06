from pocketbot.infrastructure.container.service_collection import ServiceCollection


class Logger:
    pass


def test_transient_returns_different_instances() -> None:
    services = ServiceCollection()

    services.add_transient(Logger)

    provider = services.build_provider()

    first = provider.get_service(Logger)
    second = provider.get_service(Logger)

    assert first is not second


def test_transient_creates_new_instance_every_time() -> None:
    counter = 0

    class Service:
        def __init__(self) -> None:
            nonlocal counter
            counter += 1

    services = ServiceCollection()

    services.add_transient(Service)

    provider = services.build_provider()

    provider.get_service(Service)
    provider.get_service(Service)
    provider.get_service(Service)

    assert counter == 3