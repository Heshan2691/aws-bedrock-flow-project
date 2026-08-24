import json
import os
import uuid
from datetime import datetime, timezone
import boto3

table = boto3.resource("dynamodb").Table(os.environ["TABLE_NAME"])


def lambda_handler(event, context):
    print("EVENT:", json.dumps(event, indent=2, default=str))

    # AgentCore Gateway sends the MCP tool arguments directly
    description = (event.get("description") or "").strip()
    steps = (event.get("stepsToReproduce") or "").strip()
    environment = (event.get("environment") or "").strip()

    # Validate required field
    if not description:
        return {
            "error": "missing",
            "field": "description"
        }

    # Create ticket
    ticket_id = str(uuid.uuid4())

    item = {
        "ticketId": ticket_id,
        "description": description,
        "stepsToReproduce": steps,
        "environment": environment,
        "status": "OPEN",
        "createdAt": datetime.now(timezone.utc).isoformat(),
    }

    # Store in DynamoDB
    table.put_item(Item=item)

    print("CREATED TICKET:", json.dumps(item, indent=2))

    return {
        "ticketId": ticket_id,
        "status": "OPEN",
        "message": "Bug report created successfully"
    }