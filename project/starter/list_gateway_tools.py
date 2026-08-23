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
    "id": 1,
    "method": "tools/list",
    "params": {}
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
