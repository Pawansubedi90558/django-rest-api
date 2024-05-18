import requests

endpoint="https://www.httpbin.org"

get_response = requests.get(endpoint)

print(get_response.text)