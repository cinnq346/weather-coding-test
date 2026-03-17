import requests

def call_api():
    res = requests.get("https://api.weather.gov/alerts/active?status=actual&message_type=alert&urgency=Immediate&severity=Severe", timeout=3)
    # Add error handling to this function, raising a custom Exception if status is not 200. 
    # Write a unit test for this function. requests-mock has been installed for you.
    return res.json()

def extract_data_from_response(res):
    # Write a function which extracts XYZ attribute from the API response.
    # The actual attribute we are after will be provided DURING the interview.
    # Write a unit test for this function.
    extracted = ["nothing for now"]
    return extracted

result = call_api()
extracted = extract_data_from_response(result)

print(extracted)