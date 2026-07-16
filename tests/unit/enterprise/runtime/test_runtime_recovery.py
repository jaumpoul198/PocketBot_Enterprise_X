from pocketbot.enterprise.runtime.runtime_recovery import (
    RuntimeRecoveryPolicy,
)


def test_runtime_recovery_until_exhausted():
    policy = RuntimeRecoveryPolicy(max_attempts=2)

    result1 = policy.recover()
    result2 = policy.recover()
    result3 = policy.recover()

    assert result1.recovered is True
    assert result2.recovered is True
    assert result3.recovered is False
    assert policy.exhausted is True
    assert policy.attempts == 2


def test_runtime_recovery_reset():
    policy = RuntimeRecoveryPolicy(max_attempts=2)

    policy.recover()
    policy.recover()

    assert policy.exhausted is True

    policy.reset()

    assert policy.attempts == 0
    assert policy.exhausted is False
