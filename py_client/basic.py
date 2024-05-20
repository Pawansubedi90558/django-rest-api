import requests

endpoint="http://localhost:8000/api/"

get_response = requests.get(endpoint,json={"a":"b"})

# print(get_response.text)
# print(get_response.status_code)
print(get_response.json()["message"])
