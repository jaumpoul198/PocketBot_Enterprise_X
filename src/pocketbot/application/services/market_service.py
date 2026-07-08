from pocketbot.domain.candle import Candle
from pocketbot.market.interfaces.market_collector import MarketCollector


class MarketService:
    def __init__(
        self,
        collector: MarketCollector,
    ) -> None:
        self._collector = collector

    def refresh_market(
        self,
        asset: str,
        timeframe: int,
        count: int,
    ) -> list[Candle]:
        return self._collector.collect(
            asset,
            timeframe,
            count,
        )