
from datetime import datetime, timezone


class IncidentResponder:

    def __init__(self):
        self.quarantined_agents = set()
        self.incidents = []

    def quarantine(
        self,
        agent_name: str,
        reason: str = "Repeated security blocks detected.",
    ) -> str:
        self.quarantined_agents.add(agent_name)

        incident = {
            "agent": agent_name,
            "reason": reason,
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "action": "QUARANTINE",
        }
        self.incidents.append(incident)

        return f"AGENT QUARANTINED: {agent_name}"

    def is_quarantined(self, agent_name: str) -> bool:
        return agent_name in self.quarantined_agents

    def get_incidents(self):
        return [incident.copy() for incident in self.incidents]
