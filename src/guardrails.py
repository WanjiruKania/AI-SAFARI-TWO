import re

class UjimaGuardrails:
    @staticmethod
    def process_dignity_filter(message: str) -> str:
        """
        Enforces the Dignity Filter: Rejects predatory language or terms that trigger shame.
        Replaces them with actionable, respectful alternatives.
        """
        forbidden_terms = {
            r"\brisky\b": "subject to seasonal cash flow variances",
            r"\bunreliable\b": "requiring liquidity cycle adaptation",
            r"\bdefault danger\b": "undergoing alternative buffer review"
        }
        
        filtered_message = message
        for pattern, replacement in forbidden_terms.items():
            filtered_message = re.sub(pattern, replacement, filtered_message, flags=re.IGNORECASE)
        
        return filtered_message

    @staticmethod
    def check_demographic_proxy(query: str) -> bool:
        """
        Hard block on using direct demographic indicators or explicit proxies 
        as justification for automated lending decisions.
        """
        proxies = ["gender", "tribe", "ethnicity", "sub-county origin"]
        for proxy in proxies:
            if proxy in query.lower():
                return False
        return True