from django.http import JsonResponse
import json

def api_home(request,*args,**kwargs):
    # print(request)
    body = request.body #byte string of JSON data
    values = request.GET
    print(values)
    # print(body)
    data={}
    try:
        data= json.loads(body) #string of JSON data -> python dict
        # print(data)
    except Exception as e:
        print(e)
    print(request.headers)
    data['headers'] =  dict(request.headers)
    data['params'] = dict(request.GET)
    return JsonResponse(data)

"""
{'Content-Length': '24', 'Content-Type': 'application/json', 'Host': 'localhost:8000', 'User-Agent': 'python-requests/2.31.0', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive'}
"""