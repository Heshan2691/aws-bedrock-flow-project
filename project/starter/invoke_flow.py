import boto3

REGION = "us-east-1"
FLOW_ID = "4C8AU1HTOD"
FLOW_ALIAS_ID = "7XQB8SPSUP"

client = boto3.client(
    "bedrock-agent-runtime",
    region_name=REGION
)

response = client.invoke_flow(
    flowIdentifier=FLOW_ID,
    flowAliasIdentifier=FLOW_ALIAS_ID,
    inputs=[
        {
            "nodeName": "FlowInputNode",
            "nodeOutputName": "document",
            "content": {
                "document": "The checkout page crashes when I click the Pay button."
            }
        }
    ],
    enableTrace=True
)

print("Flow execution ID:", response.get("executionId"))
print()

for event in response["responseStream"]:
    print(event)