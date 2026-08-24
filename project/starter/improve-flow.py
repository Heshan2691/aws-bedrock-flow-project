import json

FLOW_FILE = "flow-aws-current.json"
OUTPUT_FILE = "flow-definition-improved.json"

NEW_PROMPT = """You are a customer support assistant for a fictional online shop.

The customer has reported a bug.

Your task is to collect the information required to create a complete bug report.

A complete bug report requires exactly these three pieces of information:

1. Description of the bug
2. Steps to reproduce the bug
3. Customer environment, including browser, operating system, or device

Use information already provided by the customer.

IMPORTANT:
- Never invent information.
- Determine which of the three required pieces of information are already present in the customer's message.
- Ask for only ONE missing piece of information at a time.
- Ask for the first missing item in this order:
  1. Description
  2. Steps to reproduce
  3. Environment
- If the description is already present, do not ask for it again.
- If the description is present but steps are missing, ask only for the steps to reproduce.
- If the description and steps are present but environment is missing, ask only for the environment.
- Do not ask for multiple missing items in one response.
- Do not invent error messages, browser information, operating system information, device information, or reproduction steps.
- Be concise and professional.

Customer message:

{{customer_message}}
"""

with open(FLOW_FILE, "r", encoding="utf-16") as f:
    flow = json.load(f)

found = False

for node in flow["definition"]["nodes"]:
    if node["name"] == "BugReportResponse":
        node["configuration"]["prompt"]["sourceConfiguration"]["inline"][
            "templateConfiguration"
        ]["text"]["text"] = NEW_PROMPT
        found = True
        break

if not found:
    raise RuntimeError("BugReportResponse node was not found.")

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    json.dump(flow["definition"], f, indent=2, ensure_ascii=False)

print("Created:", OUTPUT_FILE)
print("Updated node: BugReportResponse")