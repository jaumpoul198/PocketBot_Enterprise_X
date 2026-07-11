"""
PocketBot Enterprise X

Bootstrap package.

The bootstrap package is the composition root of the application.
It is responsible for configuring services, infrastructure, and
building the application instance.
"""

from .application import build_application

__all__ = [
    "build_application",
]