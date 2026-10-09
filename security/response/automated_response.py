
from security.detection.anomaly_detector import AnomalyDetector
from security.response.incident_responder import IncidentResponder


class AutomatedResponse:

    def __init__(self, responder=None, threshold=3):
        self.responder = responder or IncidentResponder()
        self.detector = AnomalyDetector()
        self.threshold = threshold

    def evaluate(self, agent_name: str, events: list) -> str:
        if self.detector.detect_repeated_blocks(
            events,
            threshold=self.threshold,
            agent_name=agent_name,
        ):
            reason = (
                f"Repeated BLOCK/DENY events reached "
                f"the threshold of {self.threshold}."
            )
            return self.responder.quarantine(
                agent_name,
                reason=reason,
            )

        return "NO ACTION: Threshold not reached."
