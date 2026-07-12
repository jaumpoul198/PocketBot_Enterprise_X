from pocketbot.production.dependencies.check import DependencyStatus


def test_dependency_failure_status_contract() -> None:
    status = DependencyStatus(
        name="database",
        available=False,
    )

    assert status.name == "database"
    assert status.available is False


def test_dependency_failure_is_not_available() -> None:
    status = DependencyStatus(
        name="cache",
        available=False,
    )

    assert status.available is False
