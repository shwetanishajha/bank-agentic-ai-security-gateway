
from security.response.automated_response import AutomatedResponse
from security.response.incident_responder import IncidentResponder


def test_repeated_blocks_trigger_quarantine():
    responder = IncidentResponder()
    response = AutomatedResponse(responder=responder, threshold=3)

    events = [
        {"agent": "customer-service-agent", "decision": "BLOCK"},
        {"agent": "customer-service-agent", "decision": "DENY"},
        {"agent": "customer-service-agent", "decision": "BLOCK"},
    ]

    result = response.evaluate("customer-service-agent", events)

    assert result == "AGENT QUARANTINED: customer-service-agent"
    assert responder.is_quarantined("customer-service-agent") is True


def test_insufficient_blocks_do_not_trigger_quarantine():
    responder = IncidentResponder()
    response = AutomatedResponse(responder=responder, threshold=3)

    events = [
        {"agent": "customer-service-agent", "decision": "BLOCK"},
        {"agent": "customer-service-agent", "decision": "ALLOW"},
    ]

    result = response.evaluate("customer-service-agent", events)

    assert result == "NO ACTION: Threshold not reached."
    assert responder.is_quarantined("customer-service-agent") is False


def test_other_agents_blocks_do_not_trigger_quarantine():
    responder = IncidentResponder()
    response = AutomatedResponse(responder=responder, threshold=3)

    events = [
        {"agent": "another-agent", "decision": "BLOCK"},
        {"agent": "another-agent", "decision": "DENY"},
        {"agent": "another-agent", "decision": "BLOCK"},
    ]

    result = response.evaluate("customer-service-agent", events)

    assert result == "NO ACTION: Threshold not reached."
    assert responder.is_quarantined("customer-service-agent") is False

def test_quarantine_records_detection_reason():
    responder = IncidentResponder()
    response = AutomatedResponse(responder=responder, threshold=3)

    events = [
        {"agent": "customer-service-agent", "decision": "BLOCK"},
        {"agent": "customer-service-agent", "decision": "DENY"},
        {"agent": "customer-service-agent", "decision": "BLOCK"},
    ]

    response.evaluate("customer-service-agent", events)

    incidents = responder.get_incidents()

    assert len(incidents) == 1
    assert incidents[0]["agent"] == "customer-service-agent"
    assert incidents[0]["action"] == "QUARANTINE"
    assert incidents[0]["reason"] == (
        "Repeated BLOCK/DENY events reached the threshold of 3."
    )
    assert incidents[0]["timestamp"]
