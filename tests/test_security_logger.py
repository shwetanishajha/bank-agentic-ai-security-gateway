
from forensic.security_logger import SecurityLogger


def test_security_event_is_logged():
    logger = SecurityLogger()

    logger.log(
        agent="customer-service-agent",
        action="transfer",
        decision="REQUIRE_APPROVAL",
        tool="banking_tools",
        reason="Additional approval required.",
    )

    events = logger.get_events()

    assert len(events) == 1

    event = events[0]

    assert event["event_id"]
    assert event["timestamp"]
    assert event["agent"] == "customer-service-agent"
    assert event["action"] == "transfer"
    assert event["tool"] == "banking_tools"
    assert event["decision"] == "REQUIRE_APPROVAL"
    assert event["reason"] == "Additional approval required."


def test_each_event_has_a_unique_id():
    logger = SecurityLogger()

    logger.log("customer-service-agent", "transfer", "DENY")
    logger.log("customer-service-agent", "transfer", "BLOCK")

    events = logger.get_events()

    assert events[0]["event_id"] != events[1]["event_id"]


def test_get_events_returns_a_copy():
    logger = SecurityLogger()
    logger.log("customer-service-agent", "transfer", "DENY")

    events = logger.get_events()
    events.clear()

    assert len(logger.get_events()) == 1
