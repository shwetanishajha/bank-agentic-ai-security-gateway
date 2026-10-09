class PromptInjectionDetector:

    SUSPICIOUS_PATTERNS = [
        "ignore previous instructions",
        "ignore all previous instructions",
        "bypass approval",
        "do not ask for confirmation",
        "you are now an unrestricted",
        "override security",
    ]

    def detect(self, user_input: str) -> bool:
        text = user_input.lower()

        return any(
            pattern in text
            for pattern in self.SUSPICIOUS_PATTERNS
        )