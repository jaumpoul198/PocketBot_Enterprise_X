"""
PocketBot Enterprise X
Application Service

Main application orchestration service.
"""

from __future__ import annotations

from pocketbot.application.pipeline.models import (
    TradingRequest,
    TradingResult,
)
from pocketbot.application.pipeline.service import (
    TradingPipelineService,
)
from pocketbot.application.services.market_service import (
    MarketService,
)
from pocketbot.confluence.engine import (
    ConfluenceEngine,
)
from pocketbot.indicators.pipeline import (
    IndicatorPipeline,
)
from pocketbot.score.engine import (
    ScoreEngine,
)
from pocketbot.trading.engine import (
    TradeEngine,
)
from pocketbot.trading.result import (
    TradeResult,
)


class ApplicationService:
    """
    Main application orchestration service.
    """

    def __init__(
        self,
        market: MarketService,
        pipeline: IndicatorPipeline,
        confluence: ConfluenceEngine,
        score_engine: ScoreEngine,
        trade_engine: TradeEngine,
        trading_pipeline: TradingPipelineService | None = None,
    ) -> None:

        dependencies = {
            "market": market,
            "pipeline": pipeline,
            "confluence": confluence,
            "score_engine": score_engine,
            "trade_engine": trade_engine,
        }

        for name, dependency in dependencies.items():
            if dependency is None:
                raise TypeError(
                    f"{name} cannot be None",
                )

        self._market = market
        self._pipeline = pipeline
        self._confluence = confluence
        self._score = score_engine
        self._trade = trade_engine
        self._trading_pipeline = trading_pipeline

    def analyse(
        self,
        asset: str,
        timeframe: int,
        candles: int,
    ) -> TradeResult:

        if not asset:
            raise ValueError(
                "asset cannot be empty",
            )

        if timeframe <= 0:
            raise ValueError(
                "timeframe must be positive",
            )

        if candles <= 0:
            raise ValueError(
                "candles must be positive",
            )

        market_candles = self._market.refresh_market(
            asset=asset,
            timeframe=timeframe,
            count=candles,
        )

        indicators = self._pipeline.execute(
            [
                "rsi",
                "ema",
                "macd",
            ],
            market_candles,
        )

        self._confluence.calculate(
            indicators,
        )

        score = self._score.calculate(
            indicators,
        )

        return self._trade.process(
            asset=asset,
            timeframe=timeframe,
            score=score,
        )

    def execute_pipeline(
        self,
        request: TradingRequest,
    ) -> TradingResult:

        if request is None:
            raise TypeError(
                "request cannot be None",
            )

        if self._trading_pipeline is None:
            raise RuntimeError(
                "Trading pipeline is not available."
            )

        return self._trading_pipeline.execute(
            request,
        )