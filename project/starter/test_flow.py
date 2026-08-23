import boto3
import json

client = boto3.client(
    "bedrock-agent-runtime",
    region_name="us-east-1"
)

response = client.invoke_flow(
    flowIdentifier="4C8AU1HTOD",
    flowAliasIdentifier="7XQB8SPSUP",
    inputs=[
        {
            "content": {
                "document": "The checkout page crashes when I click Pay."
            },
            "nodeName": "FlowInputNode",
            "nodeOutputName": "document"
        }
    ],
    enableTrace=True
)

for event in response["responseStream"]:
    print("\n--- EVENT ---")
    print(json.dumps(event, indent=2, default=str))
