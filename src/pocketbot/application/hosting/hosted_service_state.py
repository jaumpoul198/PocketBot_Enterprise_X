"""
PocketBot Enterprise X

Hosted Service State.
"""

from enum import Enum


class HostedServiceState(Enum):
    """
    Hosted service lifecycle state.
    """

    CREATED = "created"
    STARTING = "starting"
    RUNNING = "running"
    STOPPING = "stopping"
    STOPPED = "stopped"
    FAILED = "failed"