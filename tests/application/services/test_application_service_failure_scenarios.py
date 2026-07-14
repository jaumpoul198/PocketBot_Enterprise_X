from datetime import datetime

import pytest

from pocketbot.application.services.market_service import MarketService
from pocketbot.domain.candle import Candle
from pocketbot.domain.value_objects.price import Price
from pocketbot.market.interfaces.market_cache import MarketCache
from pocketbot.market.interfaces.market_collector import MarketCollector
from pocketbot.market.interfaces.market_repository import MarketRepository
from pocketbot.market.interfaces.market_validator import MarketValidator
from pocketbot.market.models.market_snapshot import MarketSnapshot


class FailingCollector(MarketCollector):
    def collect(
        self,
        asset: str,
        timeframe: int,
        count: int,
    ) -> list[Candle]:
        raise RuntimeError("collector unavailable")


class RejectingValidator(MarketValidator):
    def validate(
        self,
        candles: list[Candle],
    ) -> bool:
        return False


class DummyCache(MarketCache):
    def save(
        self,
        asset: str,
        timeframe: int,
        candles: list[Candle],
    ) -> None:
        pass

    def load(
        self,
        asset: str,
        timeframe: int,
    ) -> list[Candle]:
        return []

    def clear(self) -> None:
        pass


class DummyRepository(MarketRepository):
    def save(
        self,
        snapshot: MarketSnapshot,
    ) -> None:
        pass

    def get_latest(
        self,
        asset: str,
        timeframe: int,
    ) -> MarketSnapshot | None:
        return None

    def get_last_n(
        self,
        asset: str,
        timeframe: int,
        limit: int,
    ) -> list[MarketSnapshot]:
        return []

    def get_between(
        self,
        asset: str,
        timeframe: int,
        start: datetime,
        end: datetime,
    ) -> list[MarketSnapshot]:
        return []

    def clear(self) -> None:
        pass


def test_market_service_propagates_collector_failure() -> None:
    service = MarketService(
        FailingCollector(),
        DummyCache(),
        DummyRepository(),
        RejectingValidator(),
    )

    with pytest.raises(RuntimeError, match="collector unavailable"):
        service.refresh_market(
            "BTCUSDT",
            60,
            10,
        )
