from integrations import fetch_policy_info, fetch_claim_status

def generate_response(intent, message):
    if "policy" in intent.lower():
        policy_info = fetch_policy_info(message)
        return f"Here's your policy info: {policy_info}"
    elif "claim" in intent.lower():
        claim_status = fetch_claim_status(message)
        return f"Claim status: {claim_status}"
    else:
        return "I'm here to help with your insurance needs. Could you clarify your request?"
