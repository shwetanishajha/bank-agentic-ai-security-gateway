
class AnomalyDetector:

    def detect_repeated_blocks(
        self,
        events,
        threshold=3,
        agent_name=None,
    ):
        blocked_events = [
            event for event in events
            if event.get("decision") in ("BLOCK", "DENY")
            and (
                agent_name is None
                or event.get("agent") == agent_name
            )
        ]

        return len(blocked_events) >= threshold
