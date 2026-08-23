import boto3
import requests
import json
from requests_aws4auth import AWS4Auth

REGION = "us-east-1"
SERVICE = "bedrock-agentcore"

GATEWAY_URL = "https://bugreports-157axdpgks.gateway.bedrock-agentcore.us-east-1.amazonaws.com/mcp"

MCP_PROTOCOL_VERSION = "2025-11-25"

session = boto3.Session(region_name=REGION)
credentials = session.get_credentials().get_frozen_credentials()

auth = AWS4Auth(
    credentials.access_key,
    credentials.secret_key,
    REGION,
    SERVICE,
    session_token=credentials.token
)

headers = {
    "Content-Type": "application/json",
    "Accept": "application/json, text/event-stream",
    "MCP-Protocol-Version": MCP_PROTOCOL_VERSION
}

payload = {
    "jsonrpc": "2.0",
    "id": 2,
    "method": "tools/call",
    "params": {
        "name": "create-bug-report___create_bug_report",
        "arguments": {
            "description": "The checkout page crashes when I click the Pay button.",
            "stepsToReproduce": "1. Add an item to the cart. 2. Go to checkout. 3. Click the Pay button.",
            "environment": "Windows 11, Microsoft Edge"
        }
    }
}

response = requests.post(
    GATEWAY_URL,
    auth=auth,
    headers=headers,
    json=payload
)

print("HTTP Status:", response.status_code)
print()
print(response.text)
