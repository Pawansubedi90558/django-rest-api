import requests

endpoint="http://localhost:8000/api/"

get_response = requests.get(endpoint,params={"data1":"data2"},json={"query":"hello world"})

# print(get_response.text)
# print(get_response.status_code)
print(get_response.json())
