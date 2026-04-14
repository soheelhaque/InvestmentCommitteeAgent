from investment_committee_agent.cio import run_cio


def test_run_cio_returns_structured_output():
    topic = "NVIDIA stock"

    analyst_output = {
        "thesis": "Strong growth driven by AI demand",
        "queries": ["NVIDIA earnings", "AI chip demand forecast"]
    }

    risk_output = {
        "risks": ["Valuation is high", "Competition from AMD"],
        "unknowns": ["Sustainability of AI demand"]
    }

    result = run_cio(topic, analyst_output, risk_output)

    assert isinstance(result, dict)
    assert "decision" in result
    assert "rationale" in result
    assert "confidence" in result

    assert result["decision"] in ["APPROVE", "REJECT", "WATCHLIST"]
    