from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class RuntimeSnapshot:
    """
    Enterprise runtime snapshot.
    """

    running: bool
    autonomy_running: bool
