from pocketbot.enterprise.intelligence.context.storage.context_repository import (
    ContextRepository,
)

from pocketbot.enterprise.intelligence.context.context_models import (
    DecisionContext,
)


def test_context_repository_save():

    repository = ContextRepository()

    context = DecisionContext(
        decision_id="ctx-001",
        score=0.95,
    )

    repository.save(context)

    assert repository.count() == 1


def test_context_repository_find():

    repository = ContextRepository()

    repository.save(
        DecisionContext(
            decision_id="ctx-002",
            score=0.80,
        )
    )

    result = repository.find("ctx-002")

    assert len(result) == 1
    assert result[0].score == 0.80


def test_context_repository_clear():

    repository = ContextRepository()

    repository.save(
        DecisionContext(
            decision_id="ctx-003",
            score=0.70,
        )
    )

    repository.clear()

    assert repository.count() == 0
