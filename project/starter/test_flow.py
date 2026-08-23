import boto3
import json

REGION = "us-east-1"
FLOW_ID = "4C8AU1HTOD"
FLOW_ALIAS_ID = "7XQB8SPSUP"

client = boto3.client(
    "bedrock-agent-runtime",
    region_name=REGION
)


TEST_CASES = [
    {
        "name": "Bug Report",
        "input": "The checkout page crashes when I click Pay."
    },
    {
        "name": "Covered FAQ Question",
        "input": "What payment methods do you accept?"
    },
    {
        "name": "Uncovered Question",
        "input": "What is the weather like today?"
    },
    {
        "name": "Other Request",
        "input": "I want to speak with someone about a business partnership."
    }
]


def invoke_flow(customer_message):

    response = client.invoke_flow(
        flowIdentifier=FLOW_ID,
        flowAliasIdentifier=FLOW_ALIAS_ID,
        inputs=[
            {
                "content": {
                    "document": customer_message
                },
                "nodeName": "FlowInputNode",
                "nodeOutputName": "document"
            }
        ],
        enableTrace=True
    )

    events = []

    for event in response["responseStream"]:
        events.append(event)

    return events


def extract_output(events):

    for event in events:

        if "flowOutputEvent" in event:

            content = event["flowOutputEvent"].get("content", {})

            return content.get("document", "")

    return ""


def main():

    results = []

    print("=" * 70)
    print("BEDROCK FLOW AUTOMATED TEST")
    print("=" * 70)

    for test in TEST_CASES:

        print("\nTEST:", test["name"])
        print("INPUT:", test["input"])

        try:

            events = invoke_flow(test["input"])

            output = extract_output(events)

            print("OUTPUT:")
            print(output)

            results.append(
                {
                    "test": test["name"],
                    "input": test["input"],
                    "output": output,
                    "status": "PASS" if output else "FAIL"
                }
            )

        except Exception as e:

            print("ERROR:", str(e))

            results.append(
                {
                    "test": test["name"],
                    "input": test["input"],
                    "output": "",
                    "status": "FAIL",
                    "error": str(e)
                }
            )

    print("\n" + "=" * 70)
    print("TEST SUMMARY")
    print("=" * 70)

    passed = 0

    for result in results:

        print(
            f"{result['test']}: {result['status']}"
        )

        if result["status"] == "PASS":
            passed += 1

    print(
        f"\nPassed: {passed}/{len(results)}"
    )

    with open(
        "flow-test-results.json",
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            results,
            file,
            indent=2,
            ensure_ascii=False
        )

    print(
        "\nResults saved to flow-test-results.json"
    )


if __name__ == "__main__":
    main()