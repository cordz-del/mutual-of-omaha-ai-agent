import requests

def fetch_policy_info(details):
    # Connect to Mutual of Omaha's API (mock example)
    response = requests.get("https://api.mutualofomaha.com/policies", params={"details": details})
    return response.json()

def fetch_claim_status(details):
    response = requests.get("https://api.mutualofomaha.com/claims", params={"details": details})
    return response.json()
