from enum import Enum


class Decision(Enum):
    ALLOW = "ALLOW"
    DENY = "DENY"
    REQUIRE_APPROVAL = "REQUIRE_APPROVAL"


class PolicyEngine:

    def evaluate(self, action: str, amount: float = 0) -> Decision:

        if action == "transfer" and amount > 0:
            return Decision.REQUIRE_APPROVAL

        return Decision.ALLOW