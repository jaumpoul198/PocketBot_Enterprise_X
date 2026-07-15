from pocketbot.production.api.health_models import (
    HealthResponse,
)
from pocketbot.production.bootstrap.context import (
    create_production_context,
)
from pocketbot.production.bootstrap.runtime import (
    ProductionRuntime,
)
from pocketbot.production.bootstrap.runtime_context import (
    ProductionRuntimeContext,
)
from pocketbot.production.config.settings import (
    ProductionSettings,
)
from pocketbot.production.health.service import (
    ProductionHealthService,
)


def create_health_service() -> ProductionHealthService:
    context = create_production_context()

    runtime = ProductionRuntime(
        ProductionSettings(),
    )

    runtime_context = ProductionRuntimeContext(
        runtime,
        context,
    )

    runtime_context.start()

    return ProductionHealthService(
        runtime_context,
    )


def test_health_service_health() -> None:
    service = create_health_service()

    result = service.health()

    response = HealthResponse(
        status="ok",
        service=result.service,
        healthy=result.healthy,
        ready=result.ready,
        alive=result.alive,
        uptime_seconds=result.uptime_seconds,
    )

    assert response.status == "ok"
    assert response.healthy is True
    assert response.ready is True
    assert response.alive is True


def test_health_service_liveness() -> None:
    service = create_health_service()

    result = service.liveness()

    assert result.alive is True


def test_health_service_readiness() -> None:
    service = create_health_service()

    result = service.readiness()

    assert result.ready is True
