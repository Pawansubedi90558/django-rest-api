from django.http import JsonResponse
import json

def api_home(request,*args,**kwargs):
    # print(request)
    body = request.body
    # print(body)
    data={}
    try:
        data= json.loads(body)
        # print(data)
    except Exception as e:
        print(e)
    return JsonResponse(data)