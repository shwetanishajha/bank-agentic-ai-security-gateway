from agents.customer_service_agent import CustomerServiceAgent


def test_normal_request():
    agent = CustomerServiceAgent()

    result = agent.process_request("What is my account balance?")

    assert "Agent response" in result


def test_transfer_request():
    agent = CustomerServiceAgent()

    result = agent.process_request(
        "Transfer £100 to account 12345"
    )

    assert result == "TRANSFER BLOCKED: Additional approval required."