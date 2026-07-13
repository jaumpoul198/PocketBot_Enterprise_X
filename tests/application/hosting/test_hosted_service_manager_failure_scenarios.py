from pocketbot.application.hosting.hosted_service_manager import (
    HostedServiceManager,
)


class FakeHostedService:
    def __init__(self) -> None:
        self.calls: list[str] = []

    def start(self) -> None:
        self.calls.append("start")

    def stop(self) -> None:
        self.calls.append("stop")


class FailingStartHostedService:
    def start(self) -> None:
        raise RuntimeError("start failed")

    def stop(self) -> None:
        pass


class FailingStopHostedService:
    def start(self) -> None:
        pass

    def stop(self) -> None:
        raise RuntimeError("stop failed")


def test_hosted_service_manager_starts_all_services() -> None:
    manager = HostedServiceManager()

    service_a = FakeHostedService()
    service_b = FakeHostedService()

    manager.add(service_a)
    manager.add(service_b)

    manager.start()

    assert service_a.calls == ["start"]
    assert service_b.calls == ["start"]


def test_hosted_service_manager_stops_all_services() -> None:
    manager = HostedServiceManager()

    service_a = FakeHostedService()
    service_b = FakeHostedService()

    manager.add(service_a)
    manager.add(service_b)

    manager.stop()

    assert service_a.calls == ["stop"]
    assert service_b.calls == ["stop"]


def test_hosted_service_manager_propagates_start_failure() -> None:
    manager = HostedServiceManager()

    manager.add(FailingStartHostedService())

    try:
        manager.start()
        assert False
    except RuntimeError as exc:
        assert str(exc) == "start failed"


def test_hosted_service_manager_propagates_stop_failure() -> None:
    manager = HostedServiceManager()

    manager.add(FailingStopHostedService())

    try:
        manager.stop()
        assert False
    except RuntimeError as exc:
        assert str(exc) == "stop failed"
