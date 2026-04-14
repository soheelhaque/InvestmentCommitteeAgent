from .llm import run_llm
import json


def run_cio(topic: str, analyst_output: dict, risk_output: dict) -> dict:
    prompt = f"""
You are the Chief Investment Officer (CIO) in an investment committee.

You are making a decision on the following investment:

Topic:
{topic}

Analyst Output:
{analyst_output}

Risk Output:
{risk_output}

Return your decision in JSON with the following format:
{{
    "decision": "APPROVE | REJECT | WATCHLIST",
    "rationale": "your reasoning",
    "confidence": "HIGH | MEDIUM | LOW"
}}
"""

    response = run_llm(prompt)

    try:
        return json.loads(response)
    except json.JSONDecodeError:
        return {
            "decision": "ERROR",
            "rationale": response,
            "confidence": "LOW"
        }