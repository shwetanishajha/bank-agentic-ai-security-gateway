from security.policy.policy_engine import PolicyEngine, Decision
from security.guardrails.prompt_injection_detector import PromptInjectionDetector
from forensic.security_logger import SecurityLogger
from security.response.incident_responder import IncidentResponder


class CustomerServiceAgent:

    def __init__(self, responder=None):
        self.name = "customer-service-agent"
        self.policy = PolicyEngine()
        self.detector = PromptInjectionDetector()
        self.logger = SecurityLogger()
        self.responder = responder or IncidentResponder()

    def process_request(self, user_input: str):

        # Layer 0: Incident containment
        if self.responder.is_quarantined(self.name):
            self.logger.log(
                agent=self.name,
                action="process_request",
                decision="QUARANTINED",
            )
            return "REQUEST BLOCKED: Agent is quarantined."

        # Layer 1: Prompt-injection detection
        if self.detector.detect(user_input):
            self.logger.log(
                agent=self.name,
                action="process_request",
                decision="BLOCK",
            )
            return "REQUEST BLOCKED: Potential prompt injection detected."

        # Layer 2: Financial policy enforcement
        if "transfer" in user_input.lower():
            decision = self.policy.evaluate("transfer", 10000)

            if decision == Decision.REQUIRE_APPROVAL:
                self.logger.log(
                    agent=self.name,
                    action="transfer",
                    decision="REQUIRE_APPROVAL",
                    tool="banking_tools",
                )
                return "TRANSFER BLOCKED: Additional approval required."

            if decision == Decision.DENY:
                self.logger.log(
                    agent=self.name,
                    action="transfer",
                    decision="DENY",
                    tool="banking_tools",
                )
                return "TRANSFER BLOCKED: Security policy denied the action."

            return self.execute_transfer(user_input)

        self.logger.log(
            agent=self.name,
            action="process_request",
            decision="ALLOW",
        )
        return f"Agent response: {user_input}"

    def execute_transfer(self, request: str):
        return f"TRANSFER EXECUTED: {request}"