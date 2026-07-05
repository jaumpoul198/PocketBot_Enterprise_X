"""
PocketBot Enterprise X

Application Service Bootstrap.
"""

from __future__ import annotations

from pocketbot.application.services.application_service import ApplicationService
from pocketbot.bootstrap.application import build_indicator_pipeline
from pocketbot.confluence.engine import ConfluenceEngine
from pocketbot.decision.engine import DecisionEngine
from pocketbot.market.interfaces import MarketProvider
from pocketbot.score.engine import ScoreEngine


def build_application_service(
    market: MarketProvider,
) -> ApplicationService:
    """
    Builds the complete application service.
    """

    pipeline = build_indicator_pipeline()

    confluence = ConfluenceEngine()

    score = ScoreEngine()

    decision = DecisionEngine()

    return ApplicationService(
        market=market,
        pipeline=pipeline,
        confluence=confluence,
        score_engine=score,
        decision_engine=decision,
    )