from datetime import datetime

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

        return [
            Candle(
                symbol=asset,
                timeframe=str(timeframe),
                open=Price(100.0),
                high=Price(105.0),
                low=Price(95.0),
                close=Price(102.0),
                volume=1000.0,
                timestamp=datetime.now(),
            )
        ]


class MockCache(MarketCache):
    def __init__(self) -> None:
        self.saved = False

    def save(
        self,
        asset: str,
        timeframe: int,
        candles: list[Candle],
    ) -> None:
        self.saved = True

    def load(
        self,
        asset: str,
        timeframe: int,
    ) -> list[Candle]:
        return []

    def clear(self) -> None:
        pass


class MockRepository(MarketRepository):
    def __init__(self) -> None:
        self.saved = False

    def save(
        self,
        snapshot,
    ) -> None:
        self.saved = True

    def get_latest(
        self,
        asset: str,
        timeframe: int,
    ):
        return None

    def clear(self) -> None:
        pass


class MockValidator(MarketValidator):
    def validate(
        self,
        candles: list[Candle],
    ) -> bool:
        return True


def test_market_service_refreshes_when_cache_is_empty() -> None:
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
    assert collector.called is True
    assert cache.saved is True
    assert repository.saved is True