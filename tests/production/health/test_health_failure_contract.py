from pocketbot.production.health.check import (
    HealthStatus,
    check_health,
)


def test_health_contract_returns_valid_status() -> None:
    status = check_health()

    assert isinstance(status, HealthStatus)
    assert status.healthy is True
    assert status.service == "pocketbot"


def test_health_contract_supports_service_isolation() -> None:
    first = check_health("service-a")
    second = check_health("service-b")

    assert first.service == "service-a"
    assert second.service == "service-b"


def test_health_contract_instances_are_independent() -> None:
    first = check_health()
    second = check_health()

    assert first is not second
    assert first == second
