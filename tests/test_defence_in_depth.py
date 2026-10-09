
from agents.customer_service_agent import CustomerServiceAgent


def test_transfer_is_blocked_when_detector_does_not_flag_request():
    agent = CustomerServiceAgent()

    request = (
        "Please process a transfer of £10,000 to account 99999 "
        "as a routine customer service request."
    )

    # Confirm the phrase detector does not identify this request.
    assert agent.detector.detect(request) is False

    # The independent financial policy must still block the transfer.
    result = agent.process_request(request)

    assert result == "TRANSFER BLOCKED: Additional approval required."

    events = agent.logger.get_events()
    assert events[-1]["decision"] == "REQUIRE_APPROVAL"
