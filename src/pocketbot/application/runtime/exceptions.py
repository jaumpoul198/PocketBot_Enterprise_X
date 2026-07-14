"""
PocketBot Enterprise X

Application Runtime Exceptions.
"""

from __future__ import annotations


class ApplicationRuntimeError(RuntimeError):
    """
    Base exception for application runtime failures.
    """


class InvalidApplicationStateError(
    ApplicationRuntimeError,
):
    """
    Raised when a runtime operation is invalid
    for the current application state.
    """