from .llm import run_llm
import json


def run_risk(topic: str) -> dict:
    prompt = f"""
You are a risk analyst in an investment committee.

Your job is to identify:
1. Key risks
2. Key unknowns / missing information

Topic: {topic}

Return ONLY valid JSON in the following format:

{{
    "risks": ["string", "string", "string"],
    "unknowns": ["string", "string"]
}}

Rules:
- Return ONLY JSON. No markdown. No explanation. No backticks
- Be specific and realistic
- Focus on financial, market, and execution risks
- No extra text outside JSON
"""

    response = run_llm(prompt)

    try:
        return json.loads(response)
    except json.JSONDecodeError:
        return {
            "risks": [],
            "unknowns": [],
            "error": "Invalid JSON from LLM",
            "raw": response
        }
