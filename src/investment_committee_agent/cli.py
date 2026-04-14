from investment_committee_agent.committee import run_committee


def main():
    print("\n=== Investment Committee Demo ===\n")

    topic = input("Enter investment topic: ").strip()

    if not topic:
        print("No topic provided. Exiting.")
        return

    result = run_committee(topic)

    print("\n=== RESULTS ===\n")

    print(f"Topic: {result['topic']}\n")

    print("Analyst Thesis:")
    print(result["analyst"]["thesis"], "\n")

    print("Risk Summary:")
    print(", ".join(result["risk"]["risks"]), "\n")

    print("CIO Decision:")
    print(result["cio"]["decision"])

    print("Rationale:")
    print(result["cio"]["rationale"])

    print(f"Confidence: {result['cio']['confidence']}\n")
