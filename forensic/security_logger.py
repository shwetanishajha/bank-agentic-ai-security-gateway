
from datetime import datetime, timezone
from uuid import uuid4


class SecurityLogger:

    def __init__(self):
        self.events = []

    def log(
        self,
        agent: str,
        action: str,
        decision: str,
        tool: str | None = None,
        reason: str | None = None,
    ):
        event = {
            "event_id": str(uuid4()),
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "agent": agent,
            "action": action,
            "tool": tool,
            "decision": decision,
            "reason": reason,
        }

        self.events.append(event)

    def get_events(self):
        return list(self.events)
