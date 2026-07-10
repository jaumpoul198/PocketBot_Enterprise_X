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
        """
        Executes legacy analysis flow.

        TradingPipelineService is optional and does not
        replace the existing application contract yet.
        """

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

        confluence = self._confluence.calculate(
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
        """
        Executes modern trading pipeline flow.

        Keeps the TradingPipelineService optional
        for backwards compatibility.
        """

        if self._trading_pipeline is None:
            raise RuntimeError(
                "Trading pipeline is not available."
            )

        return self._trading_pipeline.execute(
            request,
        )
