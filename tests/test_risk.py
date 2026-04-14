from investment_committee_agent.risk import run_risk


def test_run_risk_returns_structured_output():
    result = run_risk("NVIDIA stock")

    assert isinstance(result, dict)

    assert "risks" in result
    assert "unknowns" in result

    assert isinstance(result["risks"], list)
    assert isinstance(result["unknowns"], list)

    assert len(result["risks"]) > 0
    assert len(result["unknowns"]) > 0
