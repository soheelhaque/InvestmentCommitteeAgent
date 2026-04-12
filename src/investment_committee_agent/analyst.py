from .llm import run_llm


def run_analyst(topic: str) -> dict:
    prompt = f"""
You are an investment analyst in an investment committee. 

Your job:
1. Write a short investment thesis on {topic}
2. Generate 3 web search queries to validate your thesis

Return in this format:

THESIS:
<your thesis>

SEARCH QUERIES:
1.
2.
3.
"""

    response = run_llm(prompt)
    return {
        "raw": response
    }
