
from security.policy.tool_authorizer import ToolAuthorizer
from tools.banking_tools import BankingTools


class TransferAllowedAuthorizer:
    def is_allowed(self, agent_name, tool_name):
        return tool_name in {
            "get_account_balance",
            "transfer_money",
        }


def test_transfer_is_blocked_without_approval():
    banking = BankingTools(TransferAllowedAuthorizer())

    result = banking.transfer_money(
        "approved-transfer-agent",
        100,
        "99999",
    )

    assert result == "TRANSFER BLOCKED: Additional approval required."


def test_transfer_executes_after_approval_in_simulation():
    banking = BankingTools(TransferAllowedAuthorizer())

    result = banking.transfer_money(
        "approved-transfer-agent",
        100,
        "99999",
        approval_granted=True,
    )

    assert result == "TRANSFER EXECUTED: £100 to account 99999"


def test_invalid_transfer_amount_is_rejected():
    banking = BankingTools(TransferAllowedAuthorizer())

    result = banking.transfer_money(
        "approved-transfer-agent",
        -100,
        "99999",
        approval_granted=True,
    )

    assert result == "TRANSFER DENIED: Invalid amount."
