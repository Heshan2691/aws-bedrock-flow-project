import json
import os
import uuid
from datetime import datetime, timezone

import boto3

table = boto3.resource("dynamodb").Table(os.environ["TABLE_NAME"])


def lambda_handler(event, context):
    print("EVENT:", json.dumps(event, indent=2, default=str))

    inputs = event.get("node", {}).get("inputs", [])

    values = {}

    for item in inputs:
        name = item.get("name")
        value = item.get("value")

        if name:
            values[name] = value

    # Direct Lambda testing support
    if not values:
        values = event.get("data", event)

    description = str(values.get("description") or "").strip()
    steps = str(values.get("stepsToReproduce") or "").strip()
    environment = str(values.get("environment") or "").strip()

    print("DESCRIPTION:", description)
    print("STEPS:", steps)
    print("ENVIRONMENT:", environment)

    if not description:
        result = {
            "error": "missing",
            "field": "description"
        }
    else:
        ticket_id = str(uuid.uuid4())

        item = {
            "ticketId": ticket_id,
            "description": description,
            "stepsToReproduce": steps,
            "environment": environment,
            "status": "OPEN",
            "createdAt": datetime.now(timezone.utc).isoformat()
        }

        table.put_item(Item=item)

        print("CREATED TICKET:", json.dumps(item, indent=2))

        result = {
            "ticketId": ticket_id,
            "status": "OPEN",
            "message": "Bug report created successfully"
        }

    # Bedrock Flow Lambda output
    response = json.dumps(result)

    print("FLOW FUNCTION RESPONSE:", response)

    return response
