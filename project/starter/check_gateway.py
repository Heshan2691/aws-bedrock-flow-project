import boto3
import json

region = "us-east-1"
gateway_url = "https://bugreports-157axdpgks.gateway.bedrock-agentcore.us-east-1.amazonaws.com/mcp"

session = boto3.Session(region_name=region)
credentials = session.get_credentials()

print("Gateway URL:")
print(gateway_url)
print()
print("Credentials available:", credentials is not None)
