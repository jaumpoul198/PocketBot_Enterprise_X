"""
PocketBot Enterprise X

Market State Intelligence Service.
"""

from __future__ import annotations

from dataclasses import dataclass

from pocketbot.market.interfaces.market_repository import (
    MarketRepository,
)


@dataclass(slots=True)
class MarketState:
    """
    Representa o estado atual do mercado.
    """

    asset: str

    timeframe: int

    trend: str

    last_price: float

    previous_price: float

    change_percent: float


class MarketStateService:
    """
    Serviço responsável por interpretar o estado atual do mercado.
    """

    def __init__(
        self,
        repository: MarketRepository,
    ) -> None:
        self._repository = repository


    def get_current_state(
        self,
        asset: str,
        timeframe: int,
    ) -> MarketState | None:

        snapshots = self._repository.get_last_n(
            asset,
            timeframe,
            2,
        )

        if len(snapshots) < 2:
            return None

        latest = snapshots[0]
        previous = snapshots[1]

        latest_candle = latest.last_candle
        previous_candle = previous.last_candle

        if (
            latest_candle is None
            or previous_candle is None
        ):
            return None

        last_price = latest_candle.close.value
        previous_price = previous_candle.close.value

        if last_price > previous_price:
            trend = "UP"

        elif last_price < previous_price:
            trend = "DOWN"

        else:
            trend = "SIDEWAYS"


        change_percent = (
            (
                last_price - previous_price
            )
            /
            previous_price
        ) * 100


        return MarketState(
            asset=asset,
            timeframe=timeframe,
            trend=trend,
            last_price=last_price,
            previous_price=previous_price,
            change_percent=change_percent,
        )
