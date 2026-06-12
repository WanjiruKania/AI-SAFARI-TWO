from crewai.tools import BaseTool
from pydantic import Field
from typing import Type

class ObservatoryInput(BaseTool):
    name: str = "Kenya Agricultural Observatory"
    description: str = "Look up hyper-local regional crop harvest timelines and market trends."

class KenyaAgriculturalObservatoryTool(BaseTool):
    name: str = "Kenya Agricultural Observatory Tool"
    description: str = (
        "Useful for searching regional agricultural realities, cash crop cycles, "
        "and harvest-driven income indicators in East African sub-counties."
    )

    def _run(self, query: str) -> str:
        query_lower = query.lower()
        if "busia" in query_lower or "maize" in query_lower:
            return (
                "Busia County Context: Maize planting concluded in April. Major green maize "
                "harvest cycles peak from July to August. Current localized trading capacity "
                "is steady but cash-constrained due to input investments."
            )
        elif "matooke" in query_lower or "kisii" in query_lower:
            return (
                "Kisii/Western Region Context: Matooke harvest cycles are continuous but peak "
                "bi-annually. Localized cooperative aggregation is high, showing consistent baseline volumes."
            )
        else:
            return (
                "General East African Agricultural Context: Production cycles remain robust with "
                "regional variations based on localized long-rains distributions."
            )