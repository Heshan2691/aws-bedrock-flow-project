"""
Chat transcript demonstrating a complete bug-report interaction.

This transcript shows:
1. Customer reports a bug.
2. Assistant asks follow-up questions.
3. Customer provides the requested details.
4. Assistant creates the bug report using the bug-report tool.
"""

print("""
BUG REPORT CHAT TRANSCRIPT
==========================

Customer:
The checkout page crashes when I click Pay.

Assistant:
I'm sorry you're experiencing this issue. I can help create a bug report.
I need a few details first.

What happens when the checkout page crashes? Do you see an error
message, does the page reload, or does the browser become unresponsive?

Customer:
The page becomes unresponsive for a few seconds and then shows an
error message saying "Payment processing failed."

Assistant:
Thank you. What are the exact steps you followed before the crash?

Customer:
1. I added an item to the cart.
2. I went to the checkout page.
3. I entered my payment information.
4. I clicked the Pay button.
5. The checkout page became unresponsive and displayed the error.

Assistant:
Got it. What device, operating system, and browser are you using?

Customer:
I'm using a Windows 11 laptop with Microsoft Edge.

Assistant:
Thank you. I have all the information needed to create the bug report.

[tool call] bugreports___create_bug_report

Tool arguments:
{
    "description": "The checkout page becomes unresponsive and displays
    'Payment processing failed' when the customer clicks the Pay button.",
    "stepsToReproduce": "1. Add an item to the cart.
    2. Go to the checkout page.
    3. Enter payment information.
    4. Click the Pay button.
    5. The page becomes unresponsive and displays the error.",
    "environment": "Windows 11, Microsoft Edge"
}

Tool result:
{
    "status": "OPEN",
    "message": "Bug report created successfully"
}

Assistant:
Your bug report has been created successfully. The issue has been
recorded with an OPEN status for the support team to investigate.
""")