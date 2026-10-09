
from datetime import datetime

from security.response.incident_responder import IncidentResponder


def test_quarantines_agent():
    responder = IncidentResponder()

    result = responder.quarantine("customer-service-agent")

    assert result == "AGENT QUARANTINED: customer-service-agent"
    assert responder.is_quarantined("customer-service-agent") is True


def test_other_agents_remain_active():
    responder = IncidentResponder()
    responder.quarantine("customer-service-agent")

    assert responder.is_quarantined("reporting-agent") is False


def test_quarantine_records_incident_evidence():
    responder = IncidentResponder()

    responder.quarantine(
        "customer-service-agent",
        reason="Repeated security blocks detected.",
    )

    incidents = responder.get_incidents()

    assert len(incidents) == 1
    assert incidents[0]["agent"] == "customer-service-agent"
    assert incidents[0]["reason"] == "Repeated security blocks detected."
    assert incidents[0]["action"] == "QUARANTINE"

    # Confirm the timestamp is valid ISO-formatted date/time.
    timestamp = datetime.fromisoformat(incidents[0]["timestamp"])
    assert timestamp.tzinfo is not None


def test_returned_incident_cannot_modify_stored_record():
    responder = IncidentResponder()
    responder.quarantine("customer-service-agent")

    incidents = responder.get_incidents()
    incidents[0]["reason"] = "Modified externally"

    stored_incidents = responder.get_incidents()
    assert stored_incidents[0]["reason"] == "Repeated security blocks detected."
