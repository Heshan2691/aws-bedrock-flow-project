def main(input):
    # Bedrock Lambda node returns:
    # {
    #   "messageVersion": "1.0",
    #   "response": {
    #       "functionResponse": {
    #           "responseBody": {
    #               "TEXT": {
    #                   "body": "..."
    #               }
    #           }
    #       }
    #   }
    # }

    try:
        body = input["response"]["functionResponse"]["responseBody"]["TEXT"]["body"]
        return body
    except Exception:
        return str(input)
