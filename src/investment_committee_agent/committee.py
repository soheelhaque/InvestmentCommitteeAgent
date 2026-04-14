from investment_committee_agent.analyst import run_analyst
from investment_committee_agent.risk import run_risk
from investment_committee_agent.cio import run_cio

def run_committee(topic: str) -> dict:
    """
    Orchestrates the investment committee workflow:
    Analyst → Risk → CIO
    """

    # Step 1: Analyst
    analyst_output = run_analyst(topic)

    # Step 2: Risk
    risk_output = run_risk(topic)

    # Step 3: CIO
    cio_output = run_cio(
        topic=topic,
        analyst_output=analyst_output,
        risk_output=risk_output
    )

    return {
        "topic": topic,
        "analyst": analyst_output,
        "risk": risk_output,
        "cio": cio_output
    }