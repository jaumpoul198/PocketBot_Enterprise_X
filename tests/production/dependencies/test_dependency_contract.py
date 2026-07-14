from pocketbot.production.dependencies.check import (
    DependencyStatus,
    check_dependency,
    check_dependencies,
)


def test_dependency_status_contract() -> None:
    status = DependencyStatus(
        name="database",
        available=True,
    )

    assert status.name == "database"
    assert status.available is True


def test_dependency_check_returns_status_contract() -> None:
    status = check_dependency("database")

    assert isinstance(status, DependencyStatus)
    assert status.name == "database"


def test_dependency_health_contract() -> None:
    assert check_dependencies() is True
