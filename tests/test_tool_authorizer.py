from security.policy.tool_authorizer import ToolAuthorizer


def test_allowed_tool():
    authorizer = ToolAuthorizer()

    assert authorizer.is_allowed(
        "customer-service-agent",
        "get_account_balance"
    ) is True


def test_transfer_tool_is_not_allowed():
    authorizer = ToolAuthorizer()

    assert authorizer.is_allowed(
        "customer-service-agent",
        "transfer_money"
    ) is False