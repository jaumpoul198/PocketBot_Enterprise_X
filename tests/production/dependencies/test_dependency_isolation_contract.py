from pocketbot.production.dependencies.check import check_dependency


def test_dependency_checks_are_independent() -> None:
    database = check_dependency("database")
    cache = check_dependency("cache")

    assert database.name == "database"
    assert cache.name == "cache"

    assert database is not cache


def test_dependency_status_instances_do_not_share_state() -> None:
    first = check_dependency("runtime")
    second = check_dependency("runtime")

    assert first is not second
