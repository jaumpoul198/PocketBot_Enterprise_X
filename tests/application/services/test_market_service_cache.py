from datetime import datetime

from pocketbot.market.models.market_snapshot import MarketSnapshot

from pocketbot.application.services.market_service import (
    MarketService,
)
from pocketbot.domain.candle import Candle
from pocketbot.domain.value_objects.price import Price
from pocketbot.market.interfaces.market_cache import (
    MarketCache,
)
from pocketbot.market.interfaces.market_collector import (
    MarketCollector,
)
from pocketbot.market.interfaces.market_repository import (
    MarketRepository,
)
from pocketbot.market.interfaces.market_validator import (
    MarketValidator,
)


class MockCollector(MarketCollector):
    def __init__(self) -> None:
        self.called = False

    def collect(
        self,
        asset: str,
        timeframe: int,
        count: int,
    ) -> list[Candle]:
        self.called = True

        return []


class MockCache(MarketCache):
    def __init__(self) -> None:
        self.candles = [
            Candle(
                symbol="BTCUSDT",
                timeframe="60",
                open=Price(100.0),
                high=Price(105.0),
                low=Price(95.0),
                close=Price(102.0),
                volume=1000.0,
                timestamp=datetime.now(),
            )
        ]

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
        return self.candles

    def clear(
        self,
    ) -> None:
        pass


class MockRepository(MarketRepository):
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

    def clear(
        self,
    ) -> None:
        pass


class MockValidator(MarketValidator):
    def validate(
        self,
        candles: list[Candle],
    ) -> bool:
        return True


def test_market_service_returns_cached_candles_without_collecting() -> None:
    collector = MockCollector()
    cache = MockCache()
    repository = MockRepository()
    validator = MockValidator()

    service = MarketService(
        collector,
        cache,
        repository,
        validator,
    )

    result = service.refresh_market(
        "BTCUSDT",
        60,
        1,
    )

    assert len(result) == 1
    assert collector.called is False