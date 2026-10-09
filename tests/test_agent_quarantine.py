from agents.customer_service_agent import CustomerServiceAgent
from security.response.incident_responder import IncidentResponder


def test_quarantined_agent_cannot_process_requests():
    responder = IncidentResponder()
    agent = CustomerServiceAgent(responder=responder)

    responder.quarantine("customer-service-agent")

    result = agent.process_request("What is my account balance?")

    assert result == "REQUEST BLOCKED: Agent is quarantined."