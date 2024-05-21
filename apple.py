import json

s='{"Content-Length": "24", "Content-Type": "application/json", "Host": "localhost:8000", "User-Agent": "python-requests/2.31.0", "Accept-Encoding": "gzip, deflate", "Accept": "*/*", "Connection": "keep-alive"}'

data= json.loads(s)
print(data)