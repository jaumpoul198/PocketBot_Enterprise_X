from pocketbot.enterprise.runtime.runtime_coordinator import (
    RuntimeCoordinator,
)


class FakeAutonomy:

    def __init__(self):
        self.running = False

    def start(self):
        self.running = True

    def stop(self):
        self.running = False


def test_runtime_coordinator_start():

    autonomy = FakeAutonomy()

    runtime = RuntimeCoordinator(
        autonomy=autonomy
    )

    runtime.start()

    assert runtime.running is True
    assert autonomy.running is True


def test_runtime_coordinator_stop():

    autonomy = FakeAutonomy()

    runtime = RuntimeCoordinator(
        autonomy=autonomy
    )

    runtime.start()
    runtime.stop()

    assert runtime.running is False
    assert autonomy.running is False
