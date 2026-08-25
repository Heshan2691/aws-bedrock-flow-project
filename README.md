# Customer Support Chatbot with Amazon Bedrock Flows

An AI-powered customer support message classification workflow built using **Amazon Bedrock Flows**, **Amazon Bedrock foundation models**, **AWS Lambda**, and **Amazon S3**.

The project processes incoming customer support messages and classifies each message into exactly one of three categories:

* `BUG_REPORT`
* `PLATFORM_QUESTION`
* `OTHER`

The project was developed as part of the **AWS AI & ML Scholars program** in collaboration with **Udacity**.

---

## 📌 Project Overview

Customer support teams receive large numbers of messages describing different types of issues and questions. Manually categorizing these messages can be time-consuming and inconsistent.

This project demonstrates how a generative-AI workflow can automatically analyze customer messages and determine the most appropriate support category.

The solution uses **Amazon Bedrock Flows** to orchestrate the AI workflow.

### Example

**Customer message:**

> The checkout page crashes when I click Pay.

**Classification:**

```text
BUG_REPORT
```

Another example:

**Customer message:**

> How can I change the email address associated with my account?

**Classification:**

```text
PLATFORM_QUESTION
```

---

# 🎯 Project Objectives

The main objectives of this project were to:

1. Build a customer support classification workflow using Amazon Bedrock.
2. Create a reliable classification prompt.
3. Integrate the prompt into an Amazon Bedrock Flow.
4. Connect AWS Lambda with the flow where required.
5. Create flow versions and aliases.
6. Test the workflow with representative customer messages.
7. Create an evaluation dataset using Amazon S3.
8. Evaluate the performance of the AI workflow.
9. Debug and improve the flow when output wiring or configuration issues occurred.
10. Build an end-to-end AWS generative-AI application.

---

# 🏗️ Architecture

The overall workflow can be represented as:

```text
                    ┌─────────────────────┐
                    │   Customer Message  │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ Amazon Bedrock Flow │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │  Prompt / LLM Node  │
                    │                     │
                    │ Classify message    │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │    Lambda / Logic   │
                    │       Node          │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ Classification      │
                    │ Result              │
                    └─────────────────────┘


       Evaluation
            │
            ▼
┌────────────────────────┐
│ Amazon S3 Evaluation   │
│ Dataset (.jsonl)       │
└────────────┬───────────┘
             │
             ▼
┌────────────────────────┐
│ Bedrock Evaluation     │
└────────────────────────┘
```

---

# ☁️ AWS Services Used

## Amazon Bedrock

Used as the core generative-AI service for interacting with foundation models and building the AI workflow.

Responsibilities include:

* Prompt execution
* Foundation model inference
* AI-powered classification
* Flow orchestration
* Flow versions and aliases
* Evaluation

---

## Amazon Bedrock Flows

Amazon Bedrock Flows is used to visually orchestrate the application logic.

The flow connects different components together to process a customer message and generate the final classification.

The flow contains components responsible for:

* Receiving input
* Processing the customer message
* Applying the classification prompt
* Executing supporting logic
* Returning the classification result

---

## AWS Lambda

AWS Lambda is used as part of the workflow to execute supporting application logic without managing servers.

Lambda integration also demonstrates how Bedrock workflows can be extended with custom application logic.

---

## Amazon S3

Amazon S3 is used to store the evaluation dataset.

The dataset contains customer support examples and their expected classifications.

Example structure:

```text
evaluation-dataset.jsonl
```

---

# 🧠 Classification Categories

The chatbot classifies every customer message into exactly one of the following categories.

## 1. BUG_REPORT

Use this category when the customer reports that something is:

* Broken
* Crashing
* Failing
* Malfunctioning
* Not working
* Behaving incorrectly

### Examples

```text
The checkout page crashes when I click Pay.
```

```text
The payment button doesn't do anything.
```

```text
I can't complete my checkout because the page keeps failing.
```

Expected classification:

```text
BUG_REPORT
```

---

## 2. PLATFORM_QUESTION

Use this category when the customer is asking how something works or how to use a feature of the platform.

### Examples

```text
How can I change my account email?
```

```text
Where can I view my previous orders?
```

```text
How do I update my profile information?
```

Expected classification:

```text
PLATFORM_QUESTION
```

---

## 3. OTHER

Use this category when the message does not clearly fit either of the previous categories.

### Examples

```text
Thank you for your help!
```

```text
I would like to provide some feedback about the service.
```

Expected classification:

```text
OTHER
```

---

# ✍️ Prompt Design

The core prompt instructs the foundation model to act as a customer support message classifier.

The model is explicitly instructed to:

1. Analyze the customer message.
2. Determine which category best matches the message.
3. Select exactly one category.
4. Return the expected classification format.

The classification categories are clearly defined inside the prompt to reduce ambiguity.

### Prompt Structure

```text
Role
  ↓
Task definition
  ↓
Category definitions
  ↓
Classification rules
  ↓
Examples
  ↓
Customer message
  ↓
Expected output
```

This structure helps make the model's behavior more consistent across different inputs.

---

# 🔄 Bedrock Flow

The Bedrock Flow provides the orchestration layer for the application.

The high-level process is:

```text
Input
  │
  ▼
Customer Support Message
  │
  ▼
Prompt / Model Processing
  │
  ▼
Classification
  │
  ▼
Additional Processing / Lambda
  │
  ▼
Final Output
```

The flow was tested and iteratively corrected during development to ensure that the output from each node was correctly connected to the following node.

---

# 🧩 Flow Versioning

The project uses Amazon Bedrock Flow versioning to manage stable versions of the workflow.

A flow version represents a specific configuration of the workflow.

This allows changes to the flow to be tested and published without losing track of previous configurations.

The project also uses a **flow alias** to reference the appropriate flow version.

Conceptually:

```text
Flow
 │
 ├── Version 1
 │
 ├── Version 2
 │
 └── Version 3
        ▲
        │
      Alias
```

This approach provides a cleaner way to manage changes to the workflow.

---

# 🧪 Testing

The chatbot was tested using representative customer support messages.

### Test Case 1 — Bug Report

**Input**

```text
The checkout page crashes when I click Pay.
```

**Expected output**

```text
BUG_REPORT
```

---

### Test Case 2 — Platform Question

**Input**

```text
How can I change my account information?
```

**Expected output**

```text
PLATFORM_QUESTION
```

---

### Test Case 3 — Other

**Input**

```text
Thank you for helping me with my order.
```

**Expected output**

```text
OTHER
```

---

# 📊 Evaluation

An evaluation dataset was created to test the classification workflow.

The dataset was stored in Amazon S3 in JSONL format.

Example:

```json
{"input":"The checkout page crashes when I click Pay.","expected":"BUG_REPORT"}
{"input":"How can I change my account email?","expected":"PLATFORM_QUESTION"}
{"input":"Thank you for your support.","expected":"OTHER"}
```

The evaluation process provides a structured way to determine whether the workflow correctly classifies previously prepared examples.

---

# 📁 Project Structure

The repository can be organized as follows:

```text
customer-support-chatbot-bedrock-flows/
│
├── README.md
│
├── evaluation/
│   └── evaluation-dataset.jsonl
│
├── lambda/
│   └── ...
│
├── prompts/
│   └── customer-support-classifier.txt
│
├── screenshots/
│   ├── bedrock-flow.png
│   ├── prompt-configuration.png
│   ├── lambda-integration.png
│   ├── evaluation.png
│   └── test-result.png
│
└── docs/
    └── architecture.md
```

> Adjust the folder names above to match the actual files in your repository.

---

# 🖼️ Screenshots

## Amazon Bedrock Flow

![Amazon Bedrock Flow](<Screenshots/Implement%20Classification%20and%20Routing/full%20flow%20diagram.png>)

The complete Bedrock Flow showing the connected workflow components.


# 🚀 Getting Started

## Prerequisites

Before working with this project, you should have:

* An AWS account
* Access to Amazon Bedrock
* Access to the required foundation model
* AWS CLI installed
* AWS credentials configured
* Appropriate IAM permissions
* An Amazon S3 bucket
* An AWS Lambda function where required

---

# ⚙️ AWS CLI Configuration

Configure your AWS credentials:

```bash
aws configure
```

You will be prompted for:

```text
AWS Access Key ID
AWS Secret Access Key
Default region name
Default output format
```

The project was developed using the:

```text
us-east-1
```

AWS region.

Make sure the required Bedrock model and features are available in the selected region.

---

# 🪣 Evaluation Dataset

The evaluation dataset is stored as a JSONL file.

Example:

```text
evaluation/
└── evaluation-dataset.jsonl
```

Each line represents an individual evaluation example.

Example:

```json
{"input":"The checkout page crashes when I click Pay.","expected":"BUG_REPORT"}
{"input":"Where can I find my order history?","expected":"PLATFORM_QUESTION"}
{"input":"Thanks for your assistance.","expected":"OTHER"}
```

The dataset can then be uploaded to the configured Amazon S3 bucket.

---

# 🔐 IAM Permissions

The AWS resources used by the project require appropriate IAM permissions.

Depending on the exact implementation, permissions may be required for:

* Amazon Bedrock
* Amazon Bedrock Flows
* AWS Lambda
* Amazon S3
* CloudWatch Logs

For production applications, permissions should follow the **principle of least privilege**.

Avoid using overly broad permissions such as:

```text
Action: *
Resource: *
```

unless absolutely necessary for temporary development or testing.

---

# 🧪 Example Workflow

A typical request passes through the system as follows:

### Step 1 — Customer submits a message

```text
"The checkout page crashes when I click Pay."
```

### Step 2 — Bedrock Flow receives the message

The input is passed into the configured flow.

### Step 3 — Prompt processes the message

The foundation model analyzes the customer message according to the classification instructions.

### Step 4 — Classification is generated

```text
BUG_REPORT
```

### Step 5 — Supporting logic processes the result

The workflow can pass the result through the configured Lambda or other processing node.

### Step 6 — Final response

```text
BUG_REPORT
```

---

# 🐛 Debugging and Development

During development, several workflow configuration issues were identified and corrected.

One important part of the development process was ensuring that the output of one flow node was correctly connected to the expected input of the next node.

The workflow was subsequently versioned and an alias was configured to reference the appropriate flow version.

This iterative process helped validate the complete end-to-end workflow.

---

# 📈 Key Learning Outcomes

Through this project, I gained practical experience with:

### Generative AI

* Foundation models
* Prompt engineering
* LLM-based classification
* Structured AI workflows

### Amazon Bedrock

* Bedrock Flows
* Flow nodes
* Model configuration
* Flow versions
* Flow aliases
* Testing
* Evaluation

### AWS Lambda

* Serverless functions
* Integrating custom logic into AI workflows
* Connecting Lambda with Bedrock workflows

### Amazon S3

* Dataset storage
* JSONL evaluation datasets
* Connecting cloud storage with AI evaluation workflows

### AI Evaluation

* Creating test datasets
* Comparing model output with expected results
* Validating classification behavior

---

# 💡 Why Bedrock Flows?

Amazon Bedrock Flows provides a visual approach to designing and orchestrating generative-AI workflows.

Instead of implementing every connection manually in application code, the workflow can be represented as connected components.

This makes it easier to:

* Visualize the AI pipeline
* Connect different AWS services
* Experiment with workflow logic
* Modify individual components
* Version workflows
* Deploy controlled versions using aliases

---

# 🔮 Possible Future Improvements

The current project focuses on three-category customer support classification.

Possible future enhancements include:

### 1. More Support Categories

Add categories such as:

```text
PAYMENT_ISSUE
ORDER_STATUS
ACCOUNT_ISSUE
REFUND_REQUEST
PRODUCT_QUESTION
```

---

### 2. Automatic Routing

After classification, automatically route the request to the appropriate support team.

For example:

```text
BUG_REPORT
     ↓
Engineering Team
```

```text
PAYMENT_ISSUE
     ↓
Payments Team
```

---

### 3. Customer Support Response Generation

Extend the workflow so that the system not only classifies the message but also generates an appropriate response.

```text
Customer Message
       ↓
Classification
       ↓
Support Team
       ↓
Response Generation
```

---

### 4. Confidence-Based Routing

Introduce confidence thresholds so that uncertain messages can be sent to a human support agent.

```text
High Confidence
      ↓
Automated Processing
```

```text
Low Confidence
      ↓
Human Review
```

---

### 5. Monitoring

Integrate CloudWatch monitoring and logging to track:

* Request volume
* Classification results
* Errors
* Latency
* Model behavior

---

# 🔒 Security Considerations

This project is intended for educational and development purposes.

When deploying a similar system in production:

* Do not commit AWS credentials to GitHub.
* Use IAM roles where possible.
* Follow least-privilege IAM policies.
* Avoid storing sensitive customer information unnecessarily.
* Protect S3 buckets from public access.
* Configure appropriate CloudWatch logging.
* Review model and data privacy requirements.
* Use environment variables or AWS-managed configuration for secrets.

Never commit files containing credentials such as:

```text
.env
credentials
access keys
secret keys
private keys
```

---

# 💰 Cost Considerations

AWS services used in this project may incur charges depending on usage.

Potentially billable services include:

* Amazon Bedrock model inference
* Amazon Bedrock evaluations
* AWS Lambda
* Amazon S3
* CloudWatch

Before running the project extensively, review the current AWS pricing and monitor your AWS account usage.

---

# 📚 Technologies

| Technology           | Purpose                            |
| -------------------- | ---------------------------------- |
| Amazon Bedrock       | Foundation model and generative AI |
| Amazon Bedrock Flows | AI workflow orchestration          |
| AWS Lambda           | Serverless custom logic            |
| Amazon S3            | Evaluation dataset storage         |
| AWS CLI              | AWS resource management            |
| JSONL                | Evaluation dataset format          |

---

# 🏆 Project Completion

This project was successfully completed and passed as part of the:

**AWS AI & ML Scholars Program**

with:

**Udacity**

The project provided hands-on experience in designing, implementing, testing, evaluating, and debugging an AI-powered workflow using AWS services.

---

# 👨‍💻 Author

**Heshan Yatigammana**

BSc (Hons) in Information Technology
University of Moratuwa

---

# 📜 License

This project was created for educational and learning purposes as part of the AWS AI & ML Scholars program.

If a specific license is required for the repository, add the appropriate license file and update this section accordingly.

---

# ⭐ Acknowledgements

Special thanks to:

* **AWS AI & ML Scholars**
* **Udacity**
* **Amazon Web Services**
* The instructors and learning community supporting the program

---

## 🔗 Related Resources

* Amazon Bedrock documentation
* Amazon Bedrock Flows documentation
* AWS Lambda documentation
* Amazon S3 documentation

---

## ⭐ If You Found This Project Useful

If this repository helped you understand Amazon Bedrock Flows or AWS generative-AI workflows, consider giving the repository a ⭐.

Feedback and suggestions are always welcome!
