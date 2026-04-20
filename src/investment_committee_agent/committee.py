from investment_committee_agent.analyst import run_analyst
from investment_committee_agent.risk import run_risk
from investment_committee_agent.cio import run_cio


def run_committee(topic: str, trace: bool = False) -> dict:
    if trace:
        print(f"\n[START] Topic: {topic}\n")

    if trace:
        print("[Analyst] running...")
    analyst_output = run_analyst(topic)
    if trace:
        print("[Analyst] done\n")

    if trace:
        print("[Risk] running...")
    risk_output = run_risk(topic)
    if trace:
        print("[Risk] done\n")

    if trace:
        print("[CIO] running...")
    cio_output = run_cio(topic, analyst_output, risk_output)
    if trace:
        print("[CIO] done\n")

    result = {
        "topic": topic,
        "analyst": analyst_output,
        "risk": risk_output,
        "cio": cio_output
    }

    return result