"""
PocketBot Enterprise X

Application Service.
"""

from __future__ import annotations

from pocketbot.confluence.engine import ConfluenceEngine
from pocketbot.indicators.pipeline import IndicatorPipeline
from pocketbot.market.interfaces import MarketCollector
from pocketbot.score.engine import ScoreEngine
from pocketbot.trading.engine import TradeEngine
from pocketbot.trading.result import TradeResult


class ApplicationService:
    """
    Main application orchestration service.
    """

    def __init__(
        self,
        market: MarketCollector,
        pipeline: IndicatorPipeline,
        confluence: ConfluenceEngine,
        score_engine: ScoreEngine,
        trade_engine: TradeEngine,
    ) -> None:
        self._market = market
        self._pipeline = pipeline
        self._confluence = confluence
        self._score = score_engine
        self._trade = trade_engine

    def analyse(
        self,
        asset: str,
        timeframe: int,
        candles: int,
    ) -> TradeResult:

        market_data = self._market.collect(
            asset=asset,
            timeframe=timeframe,
            count=candles,
        )

        indicator_results = self._pipeline.execute(
            indicators=[
                "EMA",
                "SMA",
                "MACD",
                "ATR",
                "BOLLINGER",
                "RSI",
                "STOCHASTIC",
            ],
            candles=market_data,
        )

        confluence = self._confluence.calculate(
            indicator_results,
        )

        score = self._score.calculate(
            indicator_results,
        )

        score.metadata["confluence"] = confluence

        return self._trade.process(
            asset=asset,
            timeframe=timeframe,
            score=score,
        )
