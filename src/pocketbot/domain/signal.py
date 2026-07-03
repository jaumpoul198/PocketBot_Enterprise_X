from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime

from pocketbot.domain.value_objects.probability import Probability
from pocketbot.domain.value_objects.score import Score


@dataclass(slots=True)
class Signal:
    """
    Representa um sinal gerado pelo sistema.
    """

    symbol: str

    direction: str

    timeframe: str

    strategy: str

    score: Score

    confidence: Probability

    probability: Probability

    generated_at: datetime

    expiration: datetime

    reason: str = ""

    metadata: dict = field(default_factory=dict)

    @property
    def valid(self) -> bool:
        return self.score.high

    @property
    def is_call(self) -> bool:
        return self.direction.upper() == "CALL"

    @property
    def is_put(self) -> bool:
        return self.direction.upper() == "PUT"
