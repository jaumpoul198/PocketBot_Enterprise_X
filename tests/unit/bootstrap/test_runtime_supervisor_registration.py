from pocketbot.bootstrap.service_registration import (
    register_services,
)
from pocketbot.enterprise.runtime.runtime_supervisor import (
    RuntimeSupervisor,
)
from pocketbot.infrastructure.container.service_collection import (
    ServiceCollection,
)


def test_runtime_supervisor_registered():

    services = ServiceCollection()

    register_services(
        services,
    )

    provider = services.build_provider()

    runtime = provider.get_service(
        RuntimeSupervisor,
    )

    assert isinstance(
        runtime,
        RuntimeSupervisor,
    )
