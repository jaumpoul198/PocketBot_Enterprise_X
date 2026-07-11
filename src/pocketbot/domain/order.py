from __future__ import annotations

from dataclasses import dataclass, field
from datetime import UTC, datetime
from uuid import uuid4

from pocketbot.domain.value_objects.money import Money
from pocketbot.domain.value_objects.price import Price


@dataclass(slots=True)
class Order:
    """
    Representa uma ordem enviada ao broker.
    """

    symbol: str

    direction: str

    amount: Money

    timeframe: str

    id: str = field(default_factory=lambda: str(uuid4()))

    created_at: datetime = field(default_factory=lambda: datetime.now(UTC))

    status: str = "PENDING"

    broker_order_id: str | None = None

    entry_price: Price | None = None

    exit_price: Price | None = None

    profit: Money = field(default_factory=lambda: Money(0))

    error_message: str = ""

    @property
    def opened(self) -> bool:
        return self.status == "OPEN"

    @property
    def closed(self) -> bool:
        return self.status == "CLOSED"

    @property
    def rejected(self) -> bool:
        return self.status == "REJECTED"
