"""
PocketBot Enterprise X
Infrastructure Container

Container-specific exceptions.
"""

from __future__ import annotations


class ContainerError(Exception):
    """
    Base exception for all container-related errors.
    """


class ServiceRegistrationError(ContainerError):
    """
    Raised when a service cannot be registered.
    """


class ServiceResolutionError(ContainerError):
    """
    Raised when a service cannot be resolved.
    """


class CircularDependencyError(ServiceResolutionError):
    """
    Raised when a circular dependency is detected.
    """


class ScopeDisposedError(ContainerError):
    """
    Raised when attempting to use a disposed scope.
    """


class ServiceNotRegisteredError(ServiceResolutionError):
    """
    Raised when a requested service has not been registered.
    """