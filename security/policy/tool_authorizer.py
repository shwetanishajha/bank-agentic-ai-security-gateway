class ToolAuthorizer:

    ALLOWED_TOOLS = {
        "customer-service-agent": [
            "get_account_balance",
        ]
    }

    def is_allowed(self, agent_name: str, tool_name: str) -> bool:
        allowed_tools = self.ALLOWED_TOOLS.get(agent_name, [])

        return tool_name in allowed_tools