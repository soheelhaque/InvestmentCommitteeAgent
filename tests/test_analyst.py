from investment_committee_agent.analyst import run_analyst


def test_run_analyst_returns_structured_output():
    result = run_analyst("NVIDIA stock")

    # Basic structure checks
    assert isinstance(result, dict)

    assert "thesis" in result
    assert "queries" in result

    # Type checks
    assert isinstance(result["thesis"], str)
    assert isinstance(result["queries"], list)

    # Content sanity checks
    assert len(result["thesis"]) > 0
    assert len(result["queries"]) > 0
