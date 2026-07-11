"""
PocketBot Enterprise X

Application Builder.
"""

from __future__ import annotations

from pocketbot.bootstrap.service_registration import (
    register_services,
)
from pocketbot.infrastructure.container.interfaces import (
    IServiceProvider,
)
from pocketbot.infrastructure.container.service_collection import (
    ServiceCollection,
)


class ApplicationBuilder:
    """
    Responsible for building the application dependency graph.
    """

    def __init__(self) -> None:
        self._services = ServiceCollection()

    def configure_services(self) -> ApplicationBuilder:
        """
        Register all application services.
        """

        register_services(
            self._services,
        )

        return self

    def build(self) -> IServiceProvider:
        """
        Build the service provider.
        """

        self.configure_services()

        return self._services.build_provider()