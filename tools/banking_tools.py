
from security.policy.policy_engine import PolicyEngine, Decision


class BankingTools:

    def __init__(self, authorizer, account_owners=None, policy=None):
        self.authorizer = authorizer
        self.policy = policy or PolicyEngine()

        self.account_owners = account_owners or {
            "A123": "customer-001",
            "B456": "customer-002",
        }

    def get_account_balance(
        self,
        agent_name: str,
        customer_id: str,
        account_id: str,
    ) -> str:

        if not self.authorizer.is_allowed(
            agent_name, "get_account_balance"
        ):
            return "TOOL DENIED: Agent is not authorized."

        if self.account_owners.get(account_id) != customer_id:
            return "ACCESS DENIED: Customer is not authorized for this account."

        balances = {"A123": 25000, "B456": 12000}

        if account_id not in balances:
            return "ACCOUNT NOT FOUND."

        return f"Account balance: £{balances[account_id]:,}"

    def transfer_money(
        self,
        agent_name: str,
        amount: float,
        destination: str,
        approval_granted: bool = False,
    ) -> str:

        # Layer 1: Agent must be permitted to call the transfer tool.
        if not self.authorizer.is_allowed(
            agent_name, "transfer_money"
        ):
            return "TOOL DENIED: Agent is not authorized."

        # Layer 2: Validate the transaction amount.
        if amount <= 0:
            return "TRANSFER DENIED: Invalid amount."

        # Layer 3: Enforce financial policy.
        decision = self.policy.evaluate("transfer", amount)

        if decision == Decision.DENY:
            return "TRANSFER DENIED: Security policy denied the action."

        if decision == Decision.REQUIRE_APPROVAL and not approval_granted:
            return "TRANSFER BLOCKED: Additional approval required."

        # Simulated execution only; no real money is moved.
        return f"TRANSFER EXECUTED: £{amount} to account {destination}"
