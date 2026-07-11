from pocketbot.infrastructure.container.service_collection import ServiceCollection


class Logger:
    pass


def test_factory_registration() -> None:
    services = ServiceCollection()

    services.add_singleton(
        Logger,
        factory=lambda provider: Logger(),
    )

    provider = services.build_provider()

    first = provider.get_service(Logger)
    second = provider.get_service(Logger)

    assert isinstance(first, Logger)
    assert first is second


def test_factory_transient() -> None:
    services = ServiceCollection()

    services.add_transient(
        Logger,
        factory=lambda provider: Logger(),
    )

    provider = services.build_provider()

    first = provider.get_service(Logger)
    second = provider.get_service(Logger)

    assert first is not second