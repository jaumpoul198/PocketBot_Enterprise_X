"""
PocketBot Enterprise X

Enterprise Runtime Recovery Policy.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class RuntimeRecoveryResult:
    """
    Result of a runtime recovery attempt.
    """

    recovered: bool
    attempts: int


class RuntimeRecoveryPolicy:
    """
    Controls runtime recovery attempts.
    """

    def __init__(
        self,
        max_attempts: int = 3,
    ) -> None:
        if max_attempts < 1:
            raise ValueError(
                "max_attempts must be greater than zero."
            )

        self._max_attempts = max_attempts
        self._attempts = 0

    @property
    def attempts(self) -> int:
        return self._attempts

    @property
    def max_attempts(self) -> int:
        return self._max_attempts

    @property
    def exhausted(self) -> bool:
        return self._attempts >= self._max_attempts

    def reset(self) -> None:
        """
        Resets recovery attempts.
        """
        self._attempts = 0

    def recover(self) -> RuntimeRecoveryResult:
        """
        Executes one recovery attempt.
        """
        if self.exhausted:
            return RuntimeRecoveryResult(
                recovered=False,
                attempts=self._attempts,
            )

        self._attempts += 1

        return RuntimeRecoveryResult(
            recovered=True,
            attempts=self._attempts,
        )
