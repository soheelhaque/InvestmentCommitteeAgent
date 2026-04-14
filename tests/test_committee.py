
from investment_committee_agent.committee import run_committee


def test_run_committee_returns_structured_output():
    result = run_committee("NVIDIA stock")

    assert isinstance(result, dict)

    assert "topic" in result
    assert "analyst" in result
    assert "risk" in result
    assert "cio" in result

    assert isinstance(result["analyst"], dict)
    assert isinstance(result["risk"], dict)
    assert isinstance(result["cio"], dict)

    assert "thesis" in result["analyst"]
    assert "risks" in result["risk"]
    assert "decision" in result["cio"]