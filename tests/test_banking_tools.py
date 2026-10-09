
from security.policy.tool_authorizer import ToolAuthorizer
from tools.banking_tools import BankingTools


def test_agent_can_read_balance():
    authorizer = ToolAuthorizer()
    banking = BankingTools(authorizer)

    result = banking.get_account_balance(
        agent_name="customer-service-agent",
        customer_id="customer-001",
        account_id="A123",
    )

    assert result == "Account balance: £25,000"


def test_agent_cannot_transfer_money():
    authorizer = ToolAuthorizer()
    banking = BankingTools(authorizer)

    result = banking.transfer_money(
        "customer-service-agent",
        10000,
        "99999",
    )

    assert result == "TOOL DENIED: Agent is not authorized."

def test_transfer_requires_authorized_tool_access():
    authorizer = ToolAuthorizer()
    banking = BankingTools(authorizer)

    result = banking.transfer_money(
        "customer-service-agent",
        100,
        "99999",
    )

    assert result == "TOOL DENIED: Agent is not authorized."
    assert not result.startswith("TRANSFER EXECUTED:")

