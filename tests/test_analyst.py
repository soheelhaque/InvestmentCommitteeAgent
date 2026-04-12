from investment_committee_agent.analyst import run_analyst


def test_run_analyst_returns_text():
    result = run_analyst("Nvidia")

    assert "raw" in result
    assert isinstance(result["raw"], str)
    assert len(result["raw"]) > 50
