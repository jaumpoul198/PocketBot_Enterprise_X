from pocketbot.domain.candle import Candle
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
from pocketbot.market.models.market_snapshot import (
    MarketSnapshot,
)


class MarketService:
    def __init__(
        self,
        collector: MarketCollector,
        cache: MarketCache,
        repository: MarketRepository,
        validator: MarketValidator,
    ) -> None:
        self._collector = collector
        self._cache = cache
        self._repository = repository
        self._validator = validator

    def refresh_market(
        self,
        asset: str,
        timeframe: int,
        count: int,
    ) -> list[Candle]:

        candles = self._cache.load(
            asset,
            timeframe,
        )

        if not candles:
            candles = self._collector.collect(
                asset,
                timeframe,
                count,
            )

            if not self._validator.validate(
                candles,
            ):
                return []

            self._cache.save(
                asset,
                timeframe,
                candles,
            )

        snapshot = MarketSnapshot(
            asset=asset,
            timeframe=timeframe,
            candles=candles,
        )

        self._repository.save(
            snapshot,
        )

        return candles