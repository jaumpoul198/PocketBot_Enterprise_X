from __future__ import annotations

from pocketbot.application.lifecycle.shutdown import Shutdown


class DisposableProvider:
    def __init__(self) -> None:
        self.dispose_calls = 0

    def dispose(self) -> None:
        self.dispose_calls += 1


class StubHostedServices:
    def __init__(self) -> None:
        self.stop_calls = 0

    def stop(self) -> None:
        self.stop_calls += 1


def test_shutdown_disposes_provider_after_stopping_services() -> None:
    provider = DisposableProvider()
    hosted_services = StubHostedServices()

    shutdown = Shutdown(
        hosted_services=hosted_services,
        provider=provider,
    )

    shutdown.execute()

    assert hosted_services.stop_calls == 1
    assert provider.dispose_calls == 1
