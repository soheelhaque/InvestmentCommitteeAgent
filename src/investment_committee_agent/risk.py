from .llm import run_llm


def run_risk(topic: str) -> dict:
    prompt = f"""
You are a risk analyst in an investment committee.

Your job is to critically evaluate the downside risks of investing in {topic}.

Think in terms of:
- Market risks
- Competitive risks
- Technology risks
- Execution risks
- Valuation risks

Also identify any missing information needed to make a decision.

Return in this format:

RISKS:
1.
2.
3.

UNKNOWNS / DATA GAPS:
1.
2.
"""

    response = run_llm(prompt)

    return {
        "raw": response
    }
