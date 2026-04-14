import json
from .llm import run_llm


def run_analyst(topic: str) -> dict:
    """
    Generates an investment thesis and search queries for a given topic.
    """

    prompt = f"""
You are an equity research analyst.

Your job is to produce:
1. A concise investment thesis
2. A list of search queries to gather more information

Topic: {topic}

Return ONLY valid JSON in the following format:

{{
    "thesis": "string - short investment view",
    "queries": ["string", "string", "string"]
}}

Rules:
- Return ONLY JSON. No markdown. No explanation. No backticks
- Be specific and grounded in financial reasoning
- Queries should be useful for real research (earnings, risks, competitors, macro factors)
- Do not include any extra text outside JSON
"""

    response = run_llm(prompt)

    try:
        return json.loads(response)
    except json.JSONDecodeError:
        return {
            "thesis": "",
            "queries": [],
            "error": "Invalid JSON from LLM",
            "raw": response
        }