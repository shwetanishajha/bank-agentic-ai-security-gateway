
from security.policy.tool_authorizer import ToolAuthorizer
from tools.banking_tools import BankingTools


def test_customer_can_access_own_account():
    tools = BankingTools(ToolAuthorizer())

    result = tools.get_account_balance(
        "customer-service-agent",
        "customer-001",
        "A123",
    )

    assert result == "Account balance: £25,000"


def test_customer_cannot_access_another_customers_account():
    tools = BankingTools(ToolAuthorizer())

    result = tools.get_account_balance(
        "customer-service-agent",
        "customer-001",
        "B456",
    )

    assert result.startswith("ACCESS DENIED:")


def test_unknown_account_is_not_disclosed():
    tools = BankingTools(ToolAuthorizer())

    result = tools.get_account_balance(
        "customer-service-agent",
        "customer-001",
        "UNKNOWN",
    )

    assert result == "ACCESS DENIED: Customer is not authorized for this account."
