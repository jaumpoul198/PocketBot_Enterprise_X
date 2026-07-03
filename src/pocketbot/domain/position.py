from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass(slots=True)
class Position:
    """
    Representa uma posição aberta no mercado.
    """

    symbol: str

    direction: str

    amount: float

    entry_price: float

    opened_at: datetime

    expiration: datetime

    current_price: Optional[float] = None

    profit: float = 0.0

    closed: bool = False

    win: bool = False

    loss: bool = False

    @property
    def active(self) -> bool:
        return not self.closed

    def update(
        self,
        current_price: float,
        profit: float,
    ) -> None:
        self.current_price = current_price
        self.profit = profit

    def close(
        self,
        current_price: float,
        profit: float,
    ) -> None:
        self.current_price = current_price
        self.profit = profit
        self.closed = True

        self.win = profit > 0
        self.loss = profit < 0
