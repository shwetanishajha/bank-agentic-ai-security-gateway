from security.policy.policy_engine import PolicyEngine, Decision


def test_transfer_requires_approval():
    policy = PolicyEngine()

    decision = policy.evaluate("transfer", 10000)

    assert decision == Decision.REQUIRE_APPROVAL


def test_non_financial_action_is_allowed():
    policy = PolicyEngine()

    decision = policy.evaluate("view_balance")

    assert decision == Decision.ALLOW