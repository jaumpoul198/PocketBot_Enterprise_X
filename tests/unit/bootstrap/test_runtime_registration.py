from pocketbot.bootstrap.service_registration import (
    register_services,
)

from pocketbot.enterprise.runtime.runtime_coordinator import (
    RuntimeCoordinator,
)

from pocketbot.infrastructure.container.service_collection import (
    ServiceCollection,
)


def test_runtime_coordinator_registered():

    services = ServiceCollection()

    register_services(
        services,
    )

    provider = services.build_provider()

    runtime = provider.get_service(
        RuntimeCoordinator,
    )

    assert isinstance(
        runtime,
        RuntimeCoordinator,
    )
