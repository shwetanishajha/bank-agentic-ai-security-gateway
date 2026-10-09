
from security.detection.anomaly_detector import AnomalyDetector


def test_detects_repeated_security_blocks():
    events = [
        {"agent": "customer-service-agent", "decision": "BLOCK"},
        {"agent": "customer-service-agent", "decision": "DENY"},
        {"agent": "customer-service-agent", "decision": "BLOCK"},
    ]

    detector = AnomalyDetector()

    assert detector.detect_repeated_blocks(events, threshold=3) is True


def test_normal_activity_is_not_anomalous():
    events = [
        {"agent": "customer-service-agent", "decision": "ALLOW"},
        {"agent": "customer-service-agent", "decision": "ALLOW"},
    ]

    detector = AnomalyDetector()

    assert detector.detect_repeated_blocks(events, threshold=3) is False


def test_other_agents_events_are_not_counted_for_target_agent():
    events = [
        {"agent": "another-agent", "decision": "BLOCK"},
        {"agent": "another-agent", "decision": "DENY"},
        {"agent": "another-agent", "decision": "BLOCK"},
    ]

    detector = AnomalyDetector()

    assert detector.detect_repeated_blocks(
        events,
        threshold=3,
        agent_name="customer-service-agent",
    ) is False
