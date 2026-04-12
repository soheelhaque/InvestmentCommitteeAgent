from investment_committee_agent.llm import run_llm


def test_run_llm_returns_output():
    result = run_llm("Say hello in one word")

    assert isinstance(result, str)
    assert len(result) > 0