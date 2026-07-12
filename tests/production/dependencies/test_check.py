from pocketbot.production.dependencies.check import check_dependency


def test_dependency_available() -> None:
    status = check_dependency("database")

    assert status.name == "database"
    assert status.available is True


def test_dependency_custom_name() -> None:
    status = check_dependency("cache")

    assert status.name == "cache"
